class CyberPulseApp {
    constructor() {
        this.initialize();
    }

    initialize() {
        this.initializeTheme();
        this.initializeNavigation();
        this.initializeSidebar();
        this.initializeSearch();
        this.initializeNotifications();
        this.initializePageLoader();
        this.initializeDropdowns();
        this.initializeTooltips();
        this.initializeClock();
        this.initializeRefreshButtons();
    }

    initializeTheme() {
        const savedTheme = localStorage.getItem("cyberpulse-theme");

        if (savedTheme) {
            document.documentElement.setAttribute("data-theme", savedTheme);
        }
    }

    initializeNavigation() {
        const links = document.querySelectorAll("a");

        links.forEach((link) => {
            link.addEventListener("click", () => {
                document.body.classList.add("page-loading");
            });
        });
    }

    initializeSidebar() {
        const sidebarButton = document.querySelector(".navbar-menu-button");
        const sidebar = document.querySelector(".sidebar");

        if (!sidebarButton || !sidebar) {
            return;
        }

        sidebarButton.addEventListener("click", () => {
            sidebar.classList.toggle("sidebar-collapsed");
        });
    }

    initializeSearch() {
        const searchForm = document.querySelector(".navbar-search");

        if (!searchForm) {
            return;
        }

        searchForm.addEventListener("submit", (event) => {
            event.preventDefault();

            const input = searchForm.querySelector("input");

            if (!input) {
                return;
            }

            const query = input.value.trim();

            if (!query) {
                return;
            }

            if (window.showInfo) {
                window.showInfo(`Searching for "${query}"`);
            }
        });
    }

    initializeNotifications() {
        const notificationButton = document.querySelector(".notifications-button");

        if (!notificationButton) {
            return;
        }

        notificationButton.addEventListener("click", () => {
            if (window.showInfo) {
                window.showInfo("No new notifications");
            }
        });
    }

    initializePageLoader() {
        window.addEventListener("load", () => {
            document.body.classList.remove("page-loading");
            document.body.classList.add("page-loaded");
        });
    }

    initializeDropdowns() {
        const dropdownTriggers = document.querySelectorAll("[data-dropdown]");

        dropdownTriggers.forEach((trigger) => {
            trigger.addEventListener("click", () => {
                const target = document.querySelector(
                    trigger.dataset.dropdown
                );

                if (target) {
                    target.classList.toggle("open");
                }
            });
        });

        document.addEventListener("click", (event) => {
            if (event.target.closest("[data-dropdown]")) {
                return;
            }

            document
                .querySelectorAll(".dropdown.open")
                .forEach((dropdown) => {
                    dropdown.classList.remove("open");
                });
        });
    }

    initializeTooltips() {
        const elements = document.querySelectorAll("[data-tooltip]");

        elements.forEach((element) => {
            element.addEventListener("mouseenter", () => {
                const tooltip = document.createElement("div");

                tooltip.className = "tooltip";
                tooltip.textContent = element.dataset.tooltip;

                document.body.appendChild(tooltip);

                const rect = element.getBoundingClientRect();

                tooltip.style.left =
                    rect.left +
                    rect.width / 2 -
                    tooltip.offsetWidth / 2 +
                    "px";

                tooltip.style.top =
                    rect.top -
                    tooltip.offsetHeight -
                    10 +
                    "px";

                element.tooltipElement = tooltip;
            });

            element.addEventListener("mouseleave", () => {
                if (element.tooltipElement) {
                    element.tooltipElement.remove();
                    element.tooltipElement = null;
                }
            });
        });
    }

    initializeClock() {
        const clockElement = document.getElementById("system-clock");

        if (!clockElement) {
            return;
        }

        const updateClock = () => {
            const now = new Date();

            clockElement.textContent =
                now.toLocaleDateString() +
                " " +
                now.toLocaleTimeString();
        };

        updateClock();

        setInterval(updateClock, 1000);
    }

    initializeRefreshButtons() {
        const refreshButtons = document.querySelectorAll(
            ".refresh-chart, .refresh-data"
        );

        refreshButtons.forEach((button) => {
            button.addEventListener("click", () => {
                button.disabled = true;

                const originalText = button.textContent;

                button.textContent = "Refreshing...";

                setTimeout(() => {
                    button.disabled = false;
                    button.textContent = originalText;

                    if (window.showSuccess) {
                        window.showSuccess("Data refreshed successfully");
                    }
                }, 1500);
            });
        });
    }

    navigate(url) {
        window.location.href = url;
    }

    reload() {
        window.location.reload();
    }
}

const app = new CyberPulseApp();

window.app = app;

document.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("app-ready");
});