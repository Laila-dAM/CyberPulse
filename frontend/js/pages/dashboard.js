class DashboardManager {
    constructor() {
        this.metrics = [];
        this.alerts = [];
        this.initialize();
    }

    async initialize() {
        await Promise.all([
            this.loadMetrics(),
            this.loadAlerts()
        ]);

        this.updateOverviewCards();
        this.updateAlertsTable();
        this.initializeCharts();
        this.startRealtimeUpdates();
    }

    async loadMetrics() {
        try {
            const response = await fetch("../data/mock-metrics.json");

            if (!response.ok) {
                throw new Error("Unable to load metrics");
            }

            this.metrics = await response.json();
        } catch (error) {
            console.error(error);
        }
    }

    async loadAlerts() {
        try {
            const response = await fetch("../data/mock-alerts.json");

            if (!response.ok) {
                throw new Error("Unable to load alerts");
            }

            this.alerts = await response.json();
        } catch (error) {
            console.error(error);
        }
    }

    updateOverviewCards() {
        const metricCards =
            document.querySelectorAll(".metric-card");

        metricCards.forEach((card, index) => {
            const metric = this.metrics[index];

            if (!metric) {
                return;
            }

            const title =
                card.querySelector(
                    ".metric-card-title"
                ) ||
                card.querySelector(
                    ".metric-title"
                );

            const value =
                card.querySelector(
                    ".metric-card-value"
                ) ||
                card.querySelector(
                    ".metric-value"
                );

            const description =
                card.querySelector(
                    ".metric-card-description"
                ) ||
                card.querySelector(
                    ".metric-description"
                );

            const status =
                card.querySelector(
                    ".metric-card-status"
                ) ||
                card.querySelector(
                    ".metric-status"
                );

            const progressBar =
                card.querySelector(
                    ".metric-card-progress-bar"
                );

            if (title) {
                title.textContent =
                    metric.name;
            }

            if (value) {
                value.textContent =
                    metric.value;
            }

            if (description) {
                description.textContent =
                    metric.description;
            }

            if (status) {
                status.textContent =
                    metric.status;
            }

            if (
                progressBar &&
                metric.progress
            ) {
                progressBar.style.width =
                    metric.progress + "%";
            }
        });
    }

    updateAlertsTable() {
        const alertsContainer =
            document.querySelector(
                ".recent-alerts-list"
            );

        if (!alertsContainer) {
            return;
        }

        alertsContainer.innerHTML = "";

        const recentAlerts =
            this.alerts.slice(0, 5);

        recentAlerts.forEach((alert) => {
            const item =
                document.createElement(
                    "div"
                );

            item.className =
                "recent-alert-item";

            item.innerHTML = `
                <div class="recent-alert-content">
                    <h4 class="recent-alert-title">
                        ${alert.title}
                    </h4>

                    <p class="recent-alert-description">
                        ${alert.description}
                    </p>
                </div>

                <div class="recent-alert-meta">
                    <span class="alert-badge ${alert.severity.toLowerCase()}">
                        ${alert.severity}
                    </span>

                    <span class="recent-alert-time">
                        ${alert.time}
                    </span>
                </div>
            `;

            alertsContainer.appendChild(
                item
            );
        });
    }

    initializeCharts() {
        if (!window.chartManager) {
            return;
        }

        if (
            document.getElementById(
                "dashboard-cpu-chart"
            )
        ) {
            window.chartManager.createCpuChart(
                "dashboard-cpu-chart"
            );
        }

        if (
            document.getElementById(
                "dashboard-memory-chart"
            )
        ) {
            window.chartManager.createMemoryChart(
                "dashboard-memory-chart"
            );
        }
    }

    startRealtimeUpdates() {
        setInterval(() => {
            this.simulateRealtimeMetrics();
            this.updateOverviewCards();
        }, 10000);
    }

    simulateRealtimeMetrics() {
        this.metrics.forEach((metric) => {
            if (
                typeof metric.progress ===
                "number"
            ) {
                const variation =
                    Math.floor(
                        Math.random() * 8
                    ) - 4;

                metric.progress =
                    Math.max(
                        0,
                        Math.min(
                            100,
                            metric.progress +
                                variation
                        )
                    );

                if (
                    metric.unit === "%"
                ) {
                    metric.value =
                        metric.progress + "%";
                }
            }
        });
    }

    getMetricCount() {
        return this.metrics.length;
    }

    getAlertCount() {
        return this.alerts.length;
    }

    getCriticalAlertCount() {
        return this.alerts.filter(
            (alert) =>
                alert.severity.toLowerCase() ===
                "critical"
        ).length;
    }

    refreshDashboard() {
        this.loadMetrics();
        this.loadAlerts();
        this.updateOverviewCards();
        this.updateAlertsTable();

        if (window.showSuccess) {
            window.showSuccess(
                "Dashboard updated successfully."
            );
        }
    }
}

const dashboardManager =
    new DashboardManager();

window.dashboardManager =
    dashboardManager;