import axios from "axios"

/** Base URL for the Lolytics API - Correspond to methods in Backend's Prediction Controller. */
const REST_API_BASE_URL = "http://localhost:8080/api/lolytics"

/** GET User Stats - gets a single user by username */
export const getUserStats = (username) => axios.get(REST_API_BASE_URL + "/" + username)