class ApiService {
    constructor() {
        this.baseUrl = "http://localhost:8000";
        this.timeout = 10000;
    }

    async request(
        endpoint,
        options = {}
    ) {
        const controller =
            new AbortController();

        const timeoutId =
            setTimeout(() => {
                controller.abort();
            }, this.timeout);

        const config = {
            method: "GET",
            headers: {
                "Content-Type":
                    "application/json",
                ...this.getAuthHeaders(),
                ...options.headers
            },
            signal: controller.signal,
            ...options
        };

        try {
            const response =
                await fetch(
                    `${this.baseUrl}${endpoint}`,
                    config
                );

            clearTimeout(timeoutId);

            const contentType =
                response.headers.get(
                    "content-type"
                );

            let data = null;

            if (
                contentType &&
                contentType.includes(
                    "application/json"
                )
            ) {
                data =
                    await response.json();
            } else {
                data =
                    await response.text();
            }

            if (!response.ok) {
                throw {
                    status:
                        response.status,
                    message:
                        data?.message ||
                        "Request failed"
                };
            }

            return data;
        } catch (error) {
            clearTimeout(timeoutId);

            if (
                error.name ===
                "AbortError"
            ) {
                throw new Error(
                    "Request timeout"
                );
            }

            throw error;
        }
    }

    getAuthHeaders() {
        const token =
            localStorage.getItem(
                "cyberpulseToken"
            );

        return token
            ? {
                  Authorization: `Bearer ${token}`
              }
            : {};
    }

    async get(endpoint) {
        return this.request(
            endpoint,
            {
                method: "GET"
            }
        );
    }

    async post(
        endpoint,
        data = {}
    ) {
        return this.request(
            endpoint,
            {
                method: "POST",
                body: JSON.stringify(
                    data
                )
            }
        );
    }

    async put(
        endpoint,
        data = {}
    ) {
        return this.request(
            endpoint,
            {
                method: "PUT",
                body: JSON.stringify(
                    data
                )
            }
        );
    }

    async patch(
        endpoint,
        data = {}
    ) {
        return this.request(
            endpoint,
            {
                method: "PATCH",
                body: JSON.stringify(
                    data
                )
            }
        );
    }

    async delete(endpoint) {
        return this.request(
            endpoint,
            {
                method: "DELETE"
            }
        );
    }

    async login(
        email,
        password
    ) {
        return this.post(
            "/auth/login",
            {
                email,
                password
            }
        );
    }

    async logout() {
        return this.post(
            "/auth/logout"
        );
    }

    async getProfile() {
        return this.get(
            "/auth/profile"
        );
    }

    async getMetrics() {
        return this.get(
            "/metrics"
        );
    }

    async getCpuMetrics() {
        return this.get(
            "/metrics/cpu"
        );
    }

    async getMemoryMetrics() {
        return this.get(
            "/metrics/memory"
        );
    }

    async getDiskMetrics() {
        return this.get(
            "/metrics/disk"
        );
    }

    async getNetworkMetrics() {
        return this.get(
            "/metrics/network"
        );
    }

    async getAlerts() {
        return this.get(
            "/alerts"
        );
    }

    async getAlert(id) {
        return this.get(
            `/alerts/${id}`
        );
    }

    async resolveAlert(id) {
        return this.patch(
            `/alerts/${id}/resolve`
        );
    }

    async ignoreAlert(id) {
        return this.patch(
            `/alerts/${id}/ignore`
        );
    }

    async getDashboardData() {
        return this.get(
            "/dashboard"
        );
    }

    async getSettings() {
        return this.get(
            "/settings"
        );
    }

    async updateSettings(
        settings
    ) {
        return this.put(
            "/settings",
            settings
        );
    }

    async getSystemStatus() {
        return this.get(
            "/system/status"
        );
    }

    async getProcesses() {
        return this.get(
            "/system/processes"
        );
    }

    async getServers() {
        return this.get(
            "/servers"
        );
    }

    async getServer(id) {
        return this.get(
            `/servers/${id}`
        );
    }

    async healthCheck() {
        return this.get(
            "/health"
        );
    }

    async loadMockMetrics() {
        const response =
            await fetch(
                "../data/mock-metrics.json"
            );

        return response.json();
    }

    async loadMockAlerts() {
        const response =
            await fetch(
                "../data/mock-alerts.json"
            );

        return response.json();
    }

    async loadMockUsers() {
        const response =
            await fetch(
                "../data/mock-users.json"
            );

        return response.json();
    }
}

const api = new ApiService();

window.api = api;