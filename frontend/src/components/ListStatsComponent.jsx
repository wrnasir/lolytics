import { useState, useEffect } from 'react';
import { getUserStats } from '../services/ListStatsService';
import { useNavigate } from 'react-router-dom';

/** Form to edit recipe. */
const ListStatsComponent = () => {
    const [name, setName] = useState("Rozu");
    const [tag, setTag] = useState("8112");
    const [stats, setStats] = useState([]);

    useEffect(() => {
        getUserInfo();
    }, []);

    function getUserInfo() {
        getUserStats({ gameName: name, tagLine: tag })
            .then((response) => {
                setStats(response.data);
                console.log(response.data)
            })
            .catch(error => {
                console.log(error);
            });
    }

    return (
        <div className="container">
            <div className="predicted-stats">
                <h2>Predicted Stats for user: {name}#{tag}</h2>
                {stats ? (
                    <>
                        <table>
                            <thead>
                                <tr>
                                    <th>Kills</th>
                                    <th>Deaths</th>
                                    <th>Assists</th>
                                    <th>CS</th>
                                    <th>Gold</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>{stats.kills}</td>
                                    <td>{stats.deaths}</td>
                                    <td>{stats.assists}</td>
                                    <td>{stats.cs}</td>
                                    <td>{stats.gold}</td>
                                </tr>
                            </tbody>
                        </table>
                        <h3>Previous Games</h3>
                        <table>
                            <thead>
                                <tr>
                                    <th>Champion Name</th>
                                    <th>KDA</th>
                                    <th>CS</th>
                                    <th>Damage</th>
                                </tr>
                            </thead>
                            <tbody>
                                {stats.previousGames.map((game, index) => (
                                    <tr key={index}>
                                        <td>{game.championName}</td>
                                        <td>{game.kda}</td>
                                        <td>{game.CS}</td>
                                        <td>{game.damage}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </>
                ) : (
                    <p>Loading...</p>
                )}
            </div>
        </div>
    );
}

export default ListStatsComponent;
