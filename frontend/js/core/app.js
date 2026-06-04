class App {
    constructor() {
        this.name = "CyberPulse";
        this.version = "1.0.0";
        this.initialized = false;
    }

    async initialize() {
        if (this.initialized) {
            return;
        }

        this.setupTheme();
        this.setupAuthentication();
        this.setupSidebar();
        this.setupNotifications();
        this.setupGlobalEvents();
        this.loadUserData();
        this.updateApplicationInfo();

        this.initialized = true;

        console.log(
            `${this.name} ${this.version} initialized`
        );
    }

    setupTheme() {
        if (
            window.themeManager &&
            typeof window.themeManager.initialize ===
                "function"
        ) {
            window.themeManager.initialize();
        }
    }

    setupAuthentication() {
        if (
            window.authManager &&
            typeof window.authManager.validateSession ===
                "function"
        ) {
            const isValid =
                window.authManager.validateSession();

            if (!isValid) {
                const currentPage =
                    window.location.pathname;

                const isLoginPage =
                    currentPage.includes(
                        "login.html"
                    );

                if (!isLoginPage) {
                    window.authManager.logout();
                }
            }
        }
    }

    setupSidebar() {
        if (
            window.sidebarManager &&
            typeof window.sidebarManager.initialize ===
                "function"
        ) {
            window.sidebarManager.initialize();
        }
    }

    setupNotifications() {
        if (
            window.notifications &&
            typeof window.notifications.info ===
                "function"
        ) {
            window.notifications.info(
                "CyberPulse is ready."
            );
        }
    }

    setupGlobalEvents() {
        window.addEventListener(
            "online",
            () => {
                this.handleOnline();
            }
        );

        window.addEventListener(
            "offline",
            () => {
                this.handleOffline();
            }
        );

        document.addEventListener(
            "visibilitychange",
            () => {
                this.handleVisibilityChange();
            }
        );
    }

    handleOnline() {
        if (
            window.notifications &&
            typeof window.notifications.success ===
                "function"
        ) {
            window.notifications.success(
                "Connection restored."
            );
        }
    }

    handleOffline() {
        if (
            window.notifications &&
            typeof window.notifications.warning ===
                "function"
        ) {
            window.notifications.warning(
                "Connection lost."
            );
        }
    }

    handleVisibilityChange() {
        if (
            document.visibilityState ===
            "visible"
        ) {
            this.refreshCurrentPage();
        }
    }

    refreshCurrentPage() {
        if (
            window.dashboardManager &&
            typeof window.dashboardManager.refreshDashboard ===
                "function"
        ) {
            window.dashboardManager.refreshDashboard();
        }

        if (
            window.metricsManager &&
            typeof window.metricsManager.refreshMetrics ===
                "function"
        ) {
            window.metricsManager.refreshMetrics();
        }

        if (
            window.alertsManager &&
            typeof window.alertsManager.refreshAlerts ===
                "function"
        ) {
            window.alertsManager.refreshAlerts();
        }
    }

    loadUserData() {
        if (
            !window.authManager ||
            typeof window.authManager.getUser !==
                "function"
        ) {
            return;
        }

        const user =
            window.authManager.getUser();

        if (!user) {
            return;
        }

        const userElements =
            document.querySelectorAll(
                "[data-user-name]"
            );

        userElements.forEach((element) => {
            element.textContent =
                user.name || "Administrator";
        });
    }

    updateApplicationInfo() {
        const versionElement =
            document.querySelector(
                "[data-app-version]"
            );

        if (versionElement) {
            versionElement.textContent =
                this.version;
        }
    }

    getInfo() {
        return {
            name: this.name,
            version: this.version,
            initialized: this.initialized
        };
    }

    destroy() {
        this.initialized = false;
    }
}

const app = new App();

document.addEventListener(
    "DOMContentLoaded",
    () => {
        app.initialize();
    }
);

window.app = app;