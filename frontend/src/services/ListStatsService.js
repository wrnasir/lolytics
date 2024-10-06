import axios from "axios"

/** Base URL for the Lolytics API - Correspond to methods in Backend's Prediction Controller. */
const REST_API_BASE_URL = "http://127.0.0.1:8000/api"

/** POST User Stats - gets a single user by username */
export const getUserStats = (user) => {
    return axios.post(`${REST_API_BASE_URL}/stats`, {
        gameName: user.gameName,
        tagLine: user.tagLine
    });
};
