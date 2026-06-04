class MetricsManager {
    constructor() {
        this.metrics = [];
        this.initialize();
    }

    async initialize() {
        await this.loadMetrics();
        this.bindEvents();
        this.updateMetricCards();
        this.initializeCharts();
        this.startAutoRefresh();
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

            if (window.showError) {
                window.showError("Failed to load metrics.");
            }
        }
    }

    bindEvents() {
        const refreshButton = document.querySelector(".btn.btn-primary");

        if (refreshButton) {
            refreshButton.addEventListener("click", () => {
                this.refreshMetrics();
            });
        }

        const exportButton = document.querySelector(".btn.btn-secondary");

        if (exportButton) {
            exportButton.addEventListener("click", () => {
                this.exportMetrics();
            });
        }
    }

    updateMetricCards() {
        if (!this.metrics.length) {
            return;
        }

        const cards = document.querySelectorAll(".metric-card");

        cards.forEach((card, index) => {
            const metric = this.metrics[index];

            if (!metric) {
                return;
            }

            const title =
                card.querySelector(".metric-title") ||
                card.querySelector(".metric-card-title");

            const value =
                card.querySelector(".metric-value") ||
                card.querySelector(".metric-card-value");

            const description =
                card.querySelector(".metric-description") ||
                card.querySelector(".metric-card-description");

            const status =
                card.querySelector(".metric-status") ||
                card.querySelector(".metric-card-status");

            if (title) {
                title.textContent = metric.name;
            }

            if (value) {
                value.textContent = metric.value;
            }

            if (description) {
                description.textContent = metric.description;
            }

            if (status) {
                status.textContent = metric.status;
            }

            const progressBar =
                card.querySelector(".metric-card-progress-bar");

            if (progressBar && metric.progress) {
                progressBar.style.width =
                    metric.progress + "%";
            }
        });
    }

    initializeCharts() {
        if (!window.chartManager) {
            return;
        }

        if (document.getElementById("cpu-chart")) {
            window.chartManager.createCpuChart(
                "cpu-chart"
            );
        }

        if (document.getElementById("memory-chart")) {
            window.chartManager.createMemoryChart(
                "memory-chart"
            );
        }

        if (document.getElementById("disk-chart")) {
            window.chartManager.createDiskChart(
                "disk-chart"
            );
        }

        if (document.getElementById("network-chart")) {
            window.chartManager.createNetworkChart(
                "network-chart"
            );
        }
    }

    async refreshMetrics() {
        try {
            await this.loadMetrics();

            this.simulateMetricChanges();

            this.updateMetricCards();

            if (window.showSuccess) {
                window.showSuccess(
                    "Metrics refreshed successfully."
                );
            }
        } catch (error) {
            console.error(error);

            if (window.showError) {
                window.showError(
                    "Unable to refresh metrics."
                );
            }
        }
    }

    simulateMetricChanges() {
        this.metrics.forEach((metric) => {
            if (typeof metric.progress === "number") {
                const variation =
                    Math.floor(
                        Math.random() * 10
                    ) - 5;

                metric.progress =
                    Math.max(
                        0,
                        Math.min(
                            100,
                            metric.progress + variation
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

    exportMetrics() {
        const exportData = {
            generatedAt:
                new Date().toISOString(),
            metrics: this.metrics
        };

        const blob = new Blob(
            [
                JSON.stringify(
                    exportData,
                    null,
                    2
                )
            ],
            {
                type: "application/json"
            }
        );

        const url =
            URL.createObjectURL(blob);

        const link =
            document.createElement("a");

        link.href = url;
        link.download =
            "cyberpulse-metrics-report.json";

        document.body.appendChild(link);

        link.click();

        link.remove();

        URL.revokeObjectURL(url);

        if (window.showSuccess) {
            window.showSuccess(
                "Metrics report exported."
            );
        }
    }

    startAutoRefresh() {
        setInterval(() => {
            this.simulateMetricChanges();
            this.updateMetricCards();
        }, 30000);
    }

    getMetricByName(name) {
        return this.metrics.find(
            (metric) =>
                metric.name
                    .toLowerCase()
                    .includes(
                        name.toLowerCase()
                    )
        );
    }

    getAllMetrics() {
        return this.metrics;
    }

    getCpuMetric() {
        return this.getMetricByName(
            "cpu"
        );
    }

    getMemoryMetric() {
        return this.getMetricByName(
            "memory"
        );
    }

    getDiskMetric() {
        return this.getMetricByName(
            "disk"
        );
    }

    getNetworkMetric() {
        return this.getMetricByName(
            "network"
        );
    }
}

const metricsManager =
    new MetricsManager();

window.metricsManager =
    metricsManager;