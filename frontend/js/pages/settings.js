class SettingsManager {
    constructor() {
        this.storageKey = "cyberpulseSettings";
        this.settings = this.loadSettings();

        this.initialize();
    }

    initialize() {
        this.populateForms();
        this.bindEvents();
    }

    bindEvents() {
        const forms = document.querySelectorAll(".settings-form");

        forms.forEach((form) => {
            form.addEventListener(
                "submit",
                this.handleFormSubmit.bind(this)
            );
        });

        const checkboxes = document.querySelectorAll(
            '.settings-option input[type="checkbox"]'
        );

        checkboxes.forEach((checkbox) => {
            checkbox.addEventListener("change", () => {
                this.saveNotificationSettings();
            });
        });

        const radioButtons = document.querySelectorAll(
            '.settings-option input[type="radio"]'
        );

        radioButtons.forEach((radio) => {
            radio.addEventListener("change", () => {
                this.saveThemeSettings();
            });
        });
    }

    handleFormSubmit(event) {
        event.preventDefault();

        this.saveFormData(event.target);

        if (window.showSuccess) {
            window.showSuccess(
                "Settings saved successfully."
            );
        }
    }

    loadSettings() {
        const savedSettings = localStorage.getItem(
            this.storageKey
        );

        if (!savedSettings) {
            return {
                account: {
                    fullName: "Administrator",
                    email: "admin@cyberpulse.com"
                },
                monitoring: {
                    cpuThreshold: 80,
                    memoryThreshold: 85,
                    diskThreshold: 90
                },
                notifications: {
                    email: true,
                    critical: true,
                    weekly: false,
                    health: true
                },
                appearance: {
                    theme: "dark"
                }
            };
        }

        return JSON.parse(savedSettings);
    }

    saveSettings() {
        localStorage.setItem(
            this.storageKey,
            JSON.stringify(this.settings)
        );
    }

    populateForms() {
        const fullName =
            document.getElementById("full-name");

        const email =
            document.getElementById("email");

        const cpuThreshold =
            document.getElementById(
                "cpu-threshold"
            );

        const memoryThreshold =
            document.getElementById(
                "memory-threshold"
            );

        const diskThreshold =
            document.getElementById(
                "disk-threshold"
            );

        if (fullName) {
            fullName.value =
                this.settings.account.fullName;
        }

        if (email) {
            email.value =
                this.settings.account.email;
        }

        if (cpuThreshold) {
            cpuThreshold.value =
                this.settings.monitoring.cpuThreshold;
        }

        if (memoryThreshold) {
            memoryThreshold.value =
                this.settings.monitoring.memoryThreshold;
        }

        if (diskThreshold) {
            diskThreshold.value =
                this.settings.monitoring.diskThreshold;
        }

        this.populateNotificationSettings();
        this.populateThemeSettings();
    }

    populateNotificationSettings() {
        const checkboxes = document.querySelectorAll(
            '.settings-option input[type="checkbox"]'
        );

        const values = [
            this.settings.notifications.email,
            this.settings.notifications.critical,
            this.settings.notifications.weekly,
            this.settings.notifications.health
        ];

        checkboxes.forEach((checkbox, index) => {
            if (values[index] !== undefined) {
                checkbox.checked = values[index];
            }
        });
    }

    populateThemeSettings() {
        const radioButtons = document.querySelectorAll(
            '.settings-option input[type="radio"]'
        );

        radioButtons.forEach((radio) => {
            const label =
                radio.parentElement.textContent
                    .trim()
                    .toLowerCase();

            if (
                label.includes(
                    this.settings.appearance.theme
                )
            ) {
                radio.checked = true;
            }
        });
    }

    saveFormData(form) {
        const fullName =
            document.getElementById("full-name");

        const email =
            document.getElementById("email");

        const cpuThreshold =
            document.getElementById(
                "cpu-threshold"
            );

        const memoryThreshold =
            document.getElementById(
                "memory-threshold"
            );

        const diskThreshold =
            document.getElementById(
                "disk-threshold"
            );

        if (fullName) {
            this.settings.account.fullName =
                fullName.value;
        }

        if (email) {
            this.settings.account.email =
                email.value;
        }

        if (cpuThreshold) {
            this.settings.monitoring.cpuThreshold =
                Number(cpuThreshold.value);
        }

        if (memoryThreshold) {
            this.settings.monitoring.memoryThreshold =
                Number(memoryThreshold.value);
        }

        if (diskThreshold) {
            this.settings.monitoring.diskThreshold =
                Number(diskThreshold.value);
        }

        this.saveSettings();
    }

    saveNotificationSettings() {
        const checkboxes = document.querySelectorAll(
            '.settings-option input[type="checkbox"]'
        );

        this.settings.notifications = {
            email:
                checkboxes[0]?.checked || false,
            critical:
                checkboxes[1]?.checked || false,
            weekly:
                checkboxes[2]?.checked || false,
            health:
                checkboxes[3]?.checked || false
        };

        this.saveSettings();

        if (window.showInfo) {
            window.showInfo(
                "Notification preferences updated."
            );
        }
    }

    saveThemeSettings() {
        const selectedTheme =
            document.querySelector(
                '.settings-option input[type="radio"]:checked'
            );

        if (!selectedTheme) {
            return;
        }

        const themeText =
            selectedTheme.parentElement.textContent
                .trim()
                .toLowerCase();

        if (themeText.includes("dark")) {
            this.settings.appearance.theme =
                "dark";
        }

        if (themeText.includes("light")) {
            this.settings.appearance.theme =
                "light";
        }

        if (themeText.includes("system")) {
            this.settings.appearance.theme =
                "system";
        }

        this.saveSettings();

        if (
            window.themeManager &&
            typeof window.themeManager.setTheme ===
                "function"
        ) {
            window.themeManager.setTheme(
                this.settings.appearance.theme
            );
        }

        if (window.showSuccess) {
            window.showSuccess(
                "Theme updated successfully."
            );
        }
    }

    resetSettings() {
        localStorage.removeItem(
            this.storageKey
        );

        window.location.reload();
    }

    exportSettings() {
        const data = JSON.stringify(
            this.settings,
            null,
            2
        );

        const blob = new Blob([data], {
            type: "application/json"
        });

        const url =
            URL.createObjectURL(blob);

        const link =
            document.createElement("a");

        link.href = url;
        link.download =
            "cyberpulse-settings.json";

        document.body.appendChild(link);
        link.click();
        link.remove();

        URL.revokeObjectURL(url);
    }
}

const settingsManager =
    new SettingsManager();

window.settingsManager =
    settingsManager;