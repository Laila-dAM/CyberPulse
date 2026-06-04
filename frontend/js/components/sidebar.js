class Sidebar {
    constructor() {
        this.currentPath = window.location.pathname;
        this.initialize();
    }

    initialize() {
        this.setActiveLink();
        this.bindEvents();
    }

    setActiveLink() {
        const links = document.querySelectorAll(".sidebar-link");

        links.forEach((link) => {
            const href = link.getAttribute("href");

            if (!href) {
                return;
            }

            const normalizedHref = href.split("/").pop();
            const currentPage = this.currentPath.split("/").pop();

            if (
                normalizedHref === currentPage ||
                (currentPage === "" && normalizedHref === "index.html")
            ) {
                link.classList.add("active");
            } else {
                link.classList.remove("active");
            }
        });
    }

    bindEvents() {
        const menuButton = document.querySelector(".navbar-menu-button");

        if (menuButton) {
            menuButton.addEventListener("click", () => {
                this.toggleSidebar();
            });
        }

        const logoutButton = document.querySelector(".sidebar-logout-button");

        if (logoutButton) {
            logoutButton.addEventListener("click", (event) => {
                this.handleLogout(event);
            });
        }
    }

    toggleSidebar() {
        const sidebar = document.querySelector(".sidebar");

        if (sidebar) {
            sidebar.classList.toggle("sidebar-collapsed");
        }
    }

    handleLogout(event) {
        event.preventDefault();

        localStorage.removeItem("cyberpulseToken");
        localStorage.removeItem("cyberpulseUser");

        window.location.href = "../pages/login.html";
    }

    createMenuItem(config) {
        const item = document.createElement("li");
        item.className = "sidebar-menu-item";

        item.innerHTML = `
            <a href="${config.href}" class="sidebar-link">
                <img
                    src="${config.icon}"
                    alt="${config.label}"
                    class="sidebar-icon"
                >
                <span>${config.label}</span>
            </a>
        `;

        return item;
    }

    renderDynamicMenu(items) {
        const menu = document.querySelector(".sidebar-menu");

        if (!menu) {
            return;
        }

        menu.innerHTML = "";

        items.forEach((item) => {
            menu.appendChild(this.createMenuItem(item));
        });

        this.setActiveLink();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    window.sidebar = new Sidebar();
});