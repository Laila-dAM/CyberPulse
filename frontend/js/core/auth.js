class AuthManager {
    constructor() {
        this.tokenKey = "cyberpulseToken";
        this.userKey = "cyberpulseUser";
    }

    login(user, token) {
        localStorage.setItem(
            this.tokenKey,
            token
        );

        localStorage.setItem(
            this.userKey,
            JSON.stringify(user)
        );

        return true;
    }

    logout() {
        localStorage.removeItem(
            this.tokenKey
        );

        localStorage.removeItem(
            this.userKey
        );

        window.location.href =
            "../pages/login.html";
    }

    isAuthenticated() {
        return Boolean(
            localStorage.getItem(
                this.tokenKey
            )
        );
    }

    getToken() {
        return localStorage.getItem(
            this.tokenKey
        );
    }

    getUser() {
        const user =
            localStorage.getItem(
                this.userKey
            );

        if (!user) {
            return null;
        }

        try {
            return JSON.parse(user);
        } catch {
            return null;
        }
    }

    updateUser(userData) {
        const currentUser =
            this.getUser();

        if (!currentUser) {
            return;
        }

        const updatedUser = {
            ...currentUser,
            ...userData
        };

        localStorage.setItem(
            this.userKey,
            JSON.stringify(updatedUser)
        );
    }

    requireAuthentication() {
        const protectedPages = [
            "dashboard.html",
            "metrics.html",
            "alerts.html",
            "settings.html",
            "about.html"
        ];

        const currentPage =
            window.location.pathname
                .split("/")
                .pop();

        if (
            protectedPages.includes(
                currentPage
            ) &&
            !this.isAuthenticated()
        ) {
            window.location.href =
                "../pages/login.html";
        }
    }

    redirectAuthenticatedUser() {
        const currentPage =
            window.location.pathname
                .split("/")
                .pop();

        if (
            currentPage ===
                "login.html" &&
            this.isAuthenticated()
        ) {
            window.location.href =
                "../pages/dashboard.html";
        }
    }

    getAuthorizationHeaders() {
        const token =
            this.getToken();

        return {
            "Content-Type":
                "application/json",
            Authorization: token
                ? `Bearer ${token}`
                : ""
        };
    }

    hasRole(role) {
        const user =
            this.getUser();

        if (!user) {
            return false;
        }

        return (
            user.role === role
        );
    }

    getUserName() {
        const user =
            this.getUser();

        return user
            ? user.name
            : "Guest";
    }

    getUserEmail() {
        const user =
            this.getUser();

        return user
            ? user.email
            : "";
    }

    validateSession() {
        const token =
            this.getToken();

        if (!token) {
            return false;
        }

        return token.length > 10;
    }

    clearSession() {
        localStorage.removeItem(
            this.tokenKey
        );

        localStorage.removeItem(
            this.userKey
        );
    }
}

const authManager =
    new AuthManager();

document.addEventListener(
    "DOMContentLoaded",
    () => {
        authManager.requireAuthentication();
        authManager.redirectAuthenticatedUser();
    }
);

window.authManager =
    authManager;