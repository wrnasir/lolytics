from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

from .tasks import *

def run_player_linear_regression(request, gameName = 'Smib', tagLine = '6751'):
    """
    Runs random forest regression on player data from the Riot API based on the provided gameName and tagLine.

    Args:
        gameName (str): The gameName of the player.
        tagLine (str): The tagLine of the player.

    Returns:
        dict: The JSON response from the Riot API containing player data.
    """
    puuid = fetch_player_data(gameName, tagLine)['puuid']
    matchIds = fetch_matches(puuid)

    kills, deaths, assists, cs, damage = [], [], [], [], []
    previousGames = []

    # Iterate through matches and extract relevant data
    for matchId in matchIds:
        match_data = fetch_match_data(matchId)
        for participant in match_data['info']['participants']:
            if participant['puuid'] == puuid:
                # Append features for this match
                
                kills.append(participant['kills'])
                deaths.append(participant['deaths'])
                assists.append(participant['assists'])
                cs.append(participant['totalMinionsKilled'])
                damage.append(participant['totalDamageDealtToChampions'])

                previousGames.append(participant['championName'] + " " + 
                                     str(participant['kills']) + "-" + 
                                     str(participant['deaths']) + "-" + 
                                     str(participant['assists']) + "    |  CS = " + 
                                     str(participant['totalMinionsKilled']) + " |   Damage = " + 
                                     str(participant['totalDamageDealtToChampions']))
                
    data = {
        'kills': kills,
        'deaths': deaths,
        'assists': assists,
        'cs': cs,
        'damage': damage
    }

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Create lagged features
    for stat in ['kills', 'deaths', 'assists', 'cs', 'damage']:
        df[f'{stat}_lag1'] = df[stat].shift(1)
        df[f'{stat}_lag2'] = df[stat].shift(2)
        df[f'{stat}_lag3'] = df[stat].shift(3)

    # Drop rows with NaN values due to lagging
    df = df.dropna()

    # Define features (X) and target (y)
    features = ['kills_lag1', 'deaths_lag1', 'assists_lag1', 'cs_lag1', 'damage_lag1',
                'kills_lag2', 'deaths_lag2', 'assists_lag2', 'cs_lag2', 'damage_lag2',
                'kills_lag3', 'deaths_lag3', 'assists_lag3', 'cs_lag3', 'damage_lag3']
    X = df[features]
    y = df[['kills', 'deaths', 'assists', 'cs', 'damage']]

    # Normalize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Create and train the Random Forest Regressor model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

    # Predict the stats for the next game
    # Example features from the last game (assuming you have these stats)
    last_game_features = np.array([6, 2, 9, 160, 24000, 7, 3, 8, 165, 23000, 5, 2, 10, 150, 20000]).reshape(1, -1)
    last_game_features_scaled = scaler.transform(last_game_features)
    next_game_prediction = model.predict(last_game_features_scaled)
    context = {'kills': next_game_prediction[0][0],
               'deaths': next_game_prediction[0][1],
               'assists': next_game_prediction[0][2],
               'cs': next_game_prediction[0][3],
               'gold': next_game_prediction[0][4],
               'previousGames' : previousGames,
               'gameName' : gameName,
               'tagLine' : tagLine}
    
    return context

