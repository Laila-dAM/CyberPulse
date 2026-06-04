class LoginManager {
    constructor() {
        this.form = document.getElementById("login-form");
        this.emailInput = document.getElementById("email");
        this.passwordInput = document.getElementById("password");
        this.rememberMeInput = document.getElementById("remember-me");

        this.initialize();
    }

    initialize() {
        this.loadSavedCredentials();
        this.bindEvents();
        this.checkAuthentication();
    }

    bindEvents() {
        if (!this.form) {
            return;
        }

        this.form.addEventListener(
            "submit",
            this.handleLogin.bind(this)
        );
    }

    async handleLogin(event) {
        event.preventDefault();

        const email = this.emailInput.value.trim();
        const password = this.passwordInput.value.trim();

        if (!email || !password) {
            this.showMessage(
                "Please enter your email and password.",
                "error"
            );
            return;
        }

        this.setLoadingState(true);

        try {
            await this.simulateAuthentication();

            const user = {
                email: email,
                role: "Administrator",
                name: "System Administrator"
            };

            const token = this.generateToken();

            localStorage.setItem(
                "cyberpulseToken",
                token
            );

            localStorage.setItem(
                "cyberpulseUser",
                JSON.stringify(user)
            );

            if (this.rememberMeInput && this.rememberMeInput.checked) {
                localStorage.setItem(
                    "cyberpulseRememberedEmail",
                    email
                );
            } else {
                localStorage.removeItem(
                    "cyberpulseRememberedEmail"
                );
            }

            this.showMessage(
                "Authentication successful.",
                "success"
            );

            setTimeout(() => {
                window.location.href =
                    "../pages/dashboard.html";
            }, 1000);
        } catch {
            this.showMessage(
                "Invalid email or password.",
                "error"
            );
        } finally {
            this.setLoadingState(false);
        }
    }

    async simulateAuthentication() {
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve();
            }, 1200);
        });
    }

    generateToken() {
        return (
            "cp_" +
            Date.now() +
            "_" +
            Math.random()
                .toString(36)
                .substring(2, 15)
        );
    }

    loadSavedCredentials() {
        const savedEmail = localStorage.getItem(
            "cyberpulseRememberedEmail"
        );

        if (
            savedEmail &&
            this.emailInput
        ) {
            this.emailInput.value = savedEmail;

            if (this.rememberMeInput) {
                this.rememberMeInput.checked = true;
            }
        }
    }

    checkAuthentication() {
        const token = localStorage.getItem(
            "cyberpulseToken"
        );

        if (
            token &&
            window.location.pathname.includes(
                "login.html"
            )
        ) {
            window.location.href =
                "../pages/dashboard.html";
        }
    }

    setLoadingState(isLoading) {
        const submitButton =
            this.form?.querySelector(
                'button[type="submit"]'
            );

        if (!submitButton) {
            return;
        }

        if (isLoading) {
            submitButton.disabled = true;
            submitButton.textContent = "Signing In...";
        } else {
            submitButton.disabled = false;
            submitButton.textContent = "Sign In";
        }
    }

    showMessage(message, type) {
        if (
            window.notifications &&
            typeof window.notifications[type] ===
                "function"
        ) {
            window.notifications[type](message);
            return;
        }

        alert(message);
    }

    logout() {
        localStorage.removeItem(
            "cyberpulseToken"
        );

        localStorage.removeItem(
            "cyberpulseUser"
        );

        window.location.href =
            "../pages/login.html";
    }

    isAuthenticated() {
        return Boolean(
            localStorage.getItem(
                "cyberpulseToken"
            )
        );
    }

    getCurrentUser() {
        const user = localStorage.getItem(
            "cyberpulseUser"
        );

        return user
            ? JSON.parse(user)
            : null;
    }
}

const loginManager = new LoginManager();

window.loginManager = loginManager;