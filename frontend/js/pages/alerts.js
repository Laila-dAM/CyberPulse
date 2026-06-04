class AlertsManager {
    constructor() {
        this.alerts = [];
        this.filteredAlerts = [];
        this.initialize();
    }

    async initialize() {
        await this.loadAlerts();
        this.bindEvents();
        this.updateSummary();
    }

    async loadAlerts() {
        try {
            const response = await fetch("../data/mock-alerts.json");

            if (!response.ok) {
                throw new Error("Unable to load alerts");
            }

            this.alerts = await response.json();
            this.filteredAlerts = [...this.alerts];

            this.renderAlerts();
        } catch (error) {
            console.error(error);

            if (window.showError) {
                window.showError("Failed to load alerts.");
            }
        }
    }

    bindEvents() {
        const severityFilter = document.getElementById("severity-filter");
        const statusFilter = document.getElementById("status-filter");

        if (severityFilter) {
            severityFilter.addEventListener("change", () => {
                this.applyFilters();
            });
        }

        if (statusFilter) {
            statusFilter.addEventListener("change", () => {
                this.applyFilters();
            });
        }

        const refreshButton = document.querySelector(".btn.btn-primary");

        if (refreshButton) {
            refreshButton.addEventListener("click", () => {
                this.refreshAlerts();
            });
        }

        const clearButton = document.querySelector(".btn.btn-secondary");

        if (clearButton) {
            clearButton.addEventListener("click", () => {
                this.clearResolvedAlerts();
            });
        }
    }

    applyFilters() {
        const severityFilter =
            document.getElementById("severity-filter");

        const statusFilter =
            document.getElementById("status-filter");

        const severityValue =
            severityFilter?.value.toLowerCase() || "";

        const statusValue =
            statusFilter?.value.toLowerCase() || "";

        this.filteredAlerts = this.alerts.filter((alert) => {
            const severityMatch =
                severityValue === "" ||
                severityValue === "all levels" ||
                alert.severity.toLowerCase() === severityValue;

            const statusMatch =
                statusValue === "" ||
                statusValue === "all statuses" ||
                alert.status.toLowerCase() === statusValue;

            return severityMatch && statusMatch;
        });

        this.renderAlerts();
    }

    renderAlerts() {
        const container =
            document.querySelector(".alerts-list");

        if (!container) {
            return;
        }

        container.innerHTML = "";

        this.filteredAlerts.forEach((alert) => {
            container.appendChild(
                this.createAlertElement(alert)
            );
        });
    }

    createAlertElement(alert) {
        const article =
            document.createElement("article");

        article.className =
            `alert-item ${alert.severity.toLowerCase()}`;

        article.innerHTML = `
            <div class="alert-item-header">
                <div>
                    <h3 class="alert-title">
                        ${alert.title}
                    </h3>

                    <p class="alert-category">
                        ${alert.category}
                    </p>
                </div>

                <span class="alert-severity">
                    ${alert.severity}
                </span>
            </div>

            <p class="alert-description">
                ${alert.description}
            </p>

            <div class="alert-details">
                <span>
                    Server: ${alert.server}
                </span>

                <span>
                    Time: ${alert.time}
                </span>

                <span>
                    Status: ${alert.status}
                </span>
            </div>

            <div class="alert-actions">
                ${
                    alert.status.toLowerCase() === "active"
                        ? `
                    <button
                        type="button"
                        class="btn btn-secondary ignore-alert"
                        data-id="${alert.id}"
                    >
                        Ignore
                    </button>

                    <button
                        type="button"
                        class="btn btn-primary resolve-alert"
                        data-id="${alert.id}"
                    >
                        Resolve
                    </button>
                `
                        : `
                    <button
                        type="button"
                        class="btn btn-secondary"
                    >
                        View Details
                    </button>
                `
                }
            </div>
        `;

        const resolveButton =
            article.querySelector(".resolve-alert");

        if (resolveButton) {
            resolveButton.addEventListener("click", () => {
                this.resolveAlert(alert.id);
            });
        }

        const ignoreButton =
            article.querySelector(".ignore-alert");

        if (ignoreButton) {
            ignoreButton.addEventListener("click", () => {
                this.ignoreAlert(alert.id);
            });
        }

        return article;
    }

    resolveAlert(id) {
        const alert = this.alerts.find(
            (item) => item.id === id
        );

        if (!alert) {
            return;
        }

        alert.status = "Resolved";

        this.applyFilters();
        this.updateSummary();

        if (window.showSuccess) {
            window.showSuccess(
                "Alert resolved successfully."
            );
        }
    }

    ignoreAlert(id) {
        this.alerts = this.alerts.filter(
            (alert) => alert.id !== id
        );

        this.applyFilters();
        this.updateSummary();

        if (window.showInfo) {
            window.showInfo(
                "Alert removed from the list."
            );
        }
    }

    clearResolvedAlerts() {
        this.alerts = this.alerts.filter(
            (alert) =>
                alert.status.toLowerCase() !==
                "resolved"
        );

        this.applyFilters();
        this.updateSummary();

        if (window.showSuccess) {
            window.showSuccess(
                "Resolved alerts cleared."
            );
        }
    }

    refreshAlerts() {
        this.applyFilters();

        if (window.showSuccess) {
            window.showSuccess(
                "Alerts refreshed successfully."
            );
        }
    }

    updateSummary() {
        const criticalCount =
            this.alerts.filter(
                (alert) =>
                    alert.severity.toLowerCase() ===
                    "critical"
            ).length;

        const warningCount =
            this.alerts.filter(
                (alert) =>
                    alert.severity.toLowerCase() ===
                    "warning"
            ).length;

        const infoCount =
            this.alerts.filter(
                (alert) =>
                    alert.severity.toLowerCase() ===
                    "information"
            ).length;

        const resolvedCount =
            this.alerts.filter(
                (alert) =>
                    alert.status.toLowerCase() ===
                    "resolved"
            ).length;

        const summaryCards =
            document.querySelectorAll(
                ".summary-card span"
            );

        if (summaryCards.length >= 4) {
            summaryCards[0].textContent =
                criticalCount;

            summaryCards[1].textContent =
                warningCount;

            summaryCards[2].textContent =
                infoCount;

            summaryCards[3].textContent =
                resolvedCount;
        }
    }

    getAlertById(id) {
        return this.alerts.find(
            (alert) => alert.id === id
        );
    }

    getActiveAlerts() {
        return this.alerts.filter(
            (alert) =>
                alert.status.toLowerCase() ===
                "active"
        );
    }

    getResolvedAlerts() {
        return this.alerts.filter(
            (alert) =>
                alert.status.toLowerCase() ===
                "resolved"
        );
    }
}

const alertsManager = new AlertsManager();

window.alertsManager = alertsManager;