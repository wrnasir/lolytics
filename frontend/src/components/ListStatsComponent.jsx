import { useState } from 'react'
import { getUserStats } from '../services/ListStatsService'
import { useNavigate } from 'react-router-dom'

/** Form to edit recipe. */
const ListStatsComponent = () => {

    const [name, setName] = useState("")
    const [tag, setTag] = useState("")
    const [stats, setStats] = useState([])

    function getUserInfo(e) {
        e.preventDefault();

        getUserStats().then((response) => {
            setStats(response)
        }).catch(error => {
            console.log(error)
        })
    }

    return (
            <div class="container">
                <div class="predicted-stats">
                    <h2>Predicted Stats for user: gameName#tagLine</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Kills</th>
                                <th>Deaths</th>
                                <th>Assists</th>
                                <th>CS</th>
                                <th>Damage</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>kills</td>
                                <td>deaths</td>
                                <td>assists</td>
                                <td>cs</td>
                                <td>gold</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div>
                    {
                        stats.map(user => 
                        <tr key={user.kills}>
                            <td>{user.deaths}</td>
                            <td>{user.assists}</td>
                            <td>{user.cs}</td>
                            <td>{user.gold}</td>
                        </tr>)
                    }
                </div>
            </div>
    )
}

export default ListStatsComponent