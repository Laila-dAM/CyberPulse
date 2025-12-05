// ===============================================
// CyberPulse – API Client
// Centralized functions for communication with backend
// ===============================================

// Base URL for backend API
const API_BASE_URL = "http://127.0.0.1:8000";

// Helper: request wrapper
async function apiRequest(endpoint, method = "GET", body = null) {
    const options = {
        method,
        headers: {
            "Content-Type": "application/json",
        }
    };

    if (body) {
        options.body = JSON.stringify(body);
    }

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);

        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Fetch Error:", error);
        return { error: true, message: error.message };
    }
}

// ===============================================
// AUTH ENDPOINTS
// ===============================================

// Login
async function loginUser(username, password) {
    return await apiRequest("/auth/login", "POST", { username, password });
}

// ===============================================
// SYSTEM METRICS ENDPOINTS
// ===============================================

// CPU usage
async function getCPUStats() {
    return await apiRequest("/metrics/cpu");
}

// RAM usage
async function getRAMStats() {
    return await apiRequest("/metrics/ram");
}

// Disk usage
async function getDiskStats() {
    return await apiRequest("/metrics/disk");
}

// Network usage
async function getNetworkStats() {
    return await apiRequest("/metrics/network");
}

// Temperature sensors
async function getTemperatureStats() {
    return await apiRequest("/metrics/temp");
}

// System logs
async function getLogData() {
    return await apiRequest("/metrics/logs");
}

// ===============================================
// EXPORT
// ===============================================

// These functions can be imported in other scripts
export {
    loginUser,
    getCPUStats,
    getRAMStats,
    getDiskStats,
    getNetworkStats,
    getTemperatureStats,
    getLogData
};
