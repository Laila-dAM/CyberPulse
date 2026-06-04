class Router {
    constructor() {
        this.routes = {};
        this.currentRoute = null;

        this.initialize();
    }

    initialize() {
        window.addEventListener(
            "popstate",
            () => {
                this.resolveRoute();
            }
        );

        document.addEventListener(
            "DOMContentLoaded",
            () => {
                this.resolveRoute();
                this.bindLinks();
            }
        );
    }

    add(path, callback) {
        this.routes[path] = callback;
    }

    remove(path) {
        delete this.routes[path];
    }

    navigate(path) {
        if (
            window.location.pathname === path
        ) {
            return;
        }

        history.pushState(
            {},
            "",
            path
        );

        this.resolveRoute();
    }

    redirect(path) {
        history.replaceState(
            {},
            "",
            path
        );

        this.resolveRoute();
    }

    resolveRoute() {
        const path =
            window.location.pathname;

        this.currentRoute = path;

        const route =
            this.routes[path];

        if (route) {
            route();
            return;
        }

        this.handleNotFound();
    }

    handleNotFound() {
        const notFoundHandler =
            this.routes["/404"];

        if (notFoundHandler) {
            notFoundHandler();
        }
    }

    bindLinks() {
        document.addEventListener(
            "click",
            (event) => {
                const link =
                    event.target.closest(
                        "[data-route]"
                    );

                if (!link) {
                    return;
                }

                event.preventDefault();

                const path =
                    link.getAttribute(
                        "data-route"
                    );

                if (path) {
                    this.navigate(path);
                }
            }
        );
    }

    getCurrentRoute() {
        return this.currentRoute;
    }

    isCurrentRoute(path) {
        return (
            this.currentRoute === path
        );
    }

    registerDefaultRoutes() {
        this.add("/", () => {
            console.log(
                "Home route loaded"
            );
        });

        this.add(
            "/pages/dashboard.html",
            () => {
                console.log(
                    "Dashboard route loaded"
                );
            }
        );

        this.add(
            "/pages/metrics.html",
            () => {
                console.log(
                    "Metrics route loaded"
                );
            }
        );

        this.add(
            "/pages/alerts.html",
            () => {
                console.log(
                    "Alerts route loaded"
                );
            }
        );

        this.add(
            "/pages/settings.html",
            () => {
                console.log(
                    "Settings route loaded"
                );
            }
        );

        this.add(
            "/pages/about.html",
            () => {
                console.log(
                    "About route loaded"
                );
            }
        );

        this.add(
            "/pages/login.html",
            () => {
                console.log(
                    "Login route loaded"
                );
            }
        );

        this.add("/404", () => {
            console.error(
                "Route not found"
            );
        });
    }
}

const router = new Router();

router.registerDefaultRoutes();

window.router = router;