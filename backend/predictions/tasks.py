import os
import requests
from celery import shared_task
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
load_dotenv()

@shared_task
def fetch_player_data(gameName, tagLine):
    """
    Fetch player data from Riot API based on the provided username.

    Args:
        username (str): The summoner name of the player.

    Returns:
        dict: The JSON response from the Riot API containing player data.
    """
    check_api_key()
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={api_key}"
    return request_riot_api(url)

@shared_task
def fetch_summoner_data(puuid):
    """
    Fetch summoner data from Riot API based on the provided summoner ID.

    Args:
        summoner_id (str): The ID of the summoner.

    Returns:
        dict: The JSON response from the Riot API containing summoner data.
    """
    check_api_key()
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={api_key}"
    return request_riot_api(url)

@shared_task
def fetch_matches(puuid):
    """
    Fetch match IDs from Riot API based on the provided player's PUUID.

    Args:
        puuid (str): The PUUID of the player.

    Returns:
        dict: The JSON response from the Riot API containing match IDs.
    """
    check_api_key()
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&type=ranked&start=0&count=10&api_key={api_key}"
    return request_riot_api(url)

@shared_task
def fetch_match_data(match_id):
    """
    Fetch match data from Riot API based on the provided match ID.

    Args:
        match_id (str): The ID of the match.

    Returns:
        dict: The JSON response from the Riot API containing match data.
    """
    check_api_key()
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}"
    return request_riot_api(url)

def check_api_key():
    """
    Check if the RIOT_API_KEY is set in the environment variables.

    Raises:
        ValueError: If the RIOT_API_KEY is not found in environment variables.
    """
    global api_key
    api_key = os.environ.get("API_KEY")
    if not api_key:
        logger.error("API_KEY not found in environment variables")
        raise ValueError("API_KEY not found in environment variables")

def request_riot_api(url):
    """
    Send a GET request to the Riot API and return the JSON response.

    Args:
        url (str): The URL for the Riot API request.

    Returns:
        dict: The JSON response from the Riot API.

    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")
        return None