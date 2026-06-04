class ChartManager {
    constructor() {
        this.charts = {};
    }

    createLineChart(canvasId, labels, data, label) {
        const canvas = document.getElementById(canvasId);

        if (!canvas || typeof Chart === "undefined") {
            return null;
        }

        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }

        this.charts[canvasId] = new Chart(canvas, {
            type: "line",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: label,
                        data: data,
                        borderWidth: 2,
                        tension: 0.4,
                        fill: true
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                interaction: {
                    intersect: false,
                    mode: "index"
                },
                plugins: {
                    legend: {
                        display: true
                    }
                },
                scales: {
                    x: {
                        display: true
                    },
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        return this.charts[canvasId];
    }

    createBarChart(canvasId, labels, data, label) {
        const canvas = document.getElementById(canvasId);

        if (!canvas || typeof Chart === "undefined") {
            return null;
        }

        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }

        this.charts[canvasId] = new Chart(canvas, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [
                    {
                        label: label,
                        data: data,
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

        return this.charts[canvasId];
    }

    createDoughnutChart(canvasId, labels, data) {
        const canvas = document.getElementById(canvasId);

        if (!canvas || typeof Chart === "undefined") {
            return null;
        }

        if (this.charts[canvasId]) {
            this.charts[canvasId].destroy();
        }

        this.charts[canvasId] = new Chart(canvas, {
            type: "doughnut",
            data: {
                labels: labels,
                datasets: [
                    {
                        data: data,
                        borderWidth: 0
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: "bottom"
                    }
                }
            }
        });

        return this.charts[canvasId];
    }

    createCpuChart(canvasId) {
        return this.createLineChart(
            canvasId,
            [
                "00:00",
                "04:00",
                "08:00",
                "12:00",
                "16:00",
                "20:00",
                "24:00"
            ],
            [
                25,
                32,
                48,
                42,
                55,
                39,
                42
            ],
            "CPU Usage"
        );
    }

    createMemoryChart(canvasId) {
        return this.createLineChart(
            canvasId,
            [
                "00:00",
                "04:00",
                "08:00",
                "12:00",
                "16:00",
                "20:00",
                "24:00"
            ],
            [
                45,
                52,
                58,
                61,
                68,
                64,
                68
            ],
            "Memory Usage"
        );
    }

    createDiskChart(canvasId) {
        return this.createBarChart(
            canvasId,
            [
                "System",
                "Applications",
                "Database",
                "Logs",
                "Backups"
            ],
            [
                40,
                55,
                72,
                28,
                57
            ],
            "Disk Usage"
        );
    }

    createNetworkChart(canvasId) {
        return this.createLineChart(
            canvasId,
            [
                "00:00",
                "04:00",
                "08:00",
                "12:00",
                "16:00",
                "20:00",
                "24:00"
            ],
            [
                72,
                95,
                110,
                128,
                140,
                118,
                128
            ],
            "Network Traffic"
        );
    }

    updateChart(canvasId, labels, data) {
        const chart = this.charts[canvasId];

        if (!chart) {
            return;
        }

        chart.data.labels = labels;
        chart.data.datasets[0].data = data;
        chart.update();
    }

    destroyChart(canvasId) {
        if (!this.charts[canvasId]) {
            return;
        }

        this.charts[canvasId].destroy();
        delete this.charts[canvasId];
    }

    destroyAll() {
        Object.keys(this.charts).forEach((chartId) => {
            this.destroyChart(chartId);
        });
    }
}

const chartManager = new ChartManager();

window.chartManager = chartManager;

document.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("cpu-chart")) {
        chartManager.createCpuChart("cpu-chart");
    }

    if (document.getElementById("memory-chart")) {
        chartManager.createMemoryChart("memory-chart");
    }

    if (document.getElementById("disk-chart")) {
        chartManager.createDiskChart("disk-chart");
    }

    if (document.getElementById("network-chart")) {
        chartManager.createNetworkChart("network-chart");
    }
});