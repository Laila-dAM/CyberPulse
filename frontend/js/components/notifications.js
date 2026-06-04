class NotificationManager {
    constructor() {
        this.container = null;
        this.notifications = [];
        this.initialize();
    }

    initialize() {
        this.createContainer();
        this.bindEvents();
    }

    createContainer() {
        let container = document.getElementById("notification-container");

        if (!container) {
            container = document.createElement("div");
            container.id = "notification-container";
            container.className = "notification-container";
            document.body.appendChild(container);
        }

        this.container = container;
    }

    bindEvents() {
        document.addEventListener("click", (event) => {
            const closeButton = event.target.closest(".notification-close");

            if (closeButton) {
                const notification = closeButton.closest(".notification");

                if (notification) {
                    this.remove(notification.dataset.id);
                }
            }
        });
    }

    generateId() {
        return `notification-${Date.now()}-${Math.floor(Math.random() * 10000)}`;
    }

    show(message, type = "info", duration = 5000) {
        const id = this.generateId();

        const notification = document.createElement("div");
        notification.className = `notification notification-${type}`;
        notification.dataset.id = id;

        notification.innerHTML = `
            <div class="notification-content">
                <div class="notification-body">
                    <span class="notification-message">${message}</span>
                </div>

                <button
                    type="button"
                    class="notification-close"
                    aria-label="Close Notification"
                >
                    ×
                </button>
            </div>
        `;

        this.container.appendChild(notification);

        this.notifications.push({
            id,
            element: notification
        });

        requestAnimationFrame(() => {
            notification.classList.add("show");
        });

        if (duration > 0) {
            setTimeout(() => {
                this.remove(id);
            }, duration);
        }

        return id;
    }

    success(message, duration = 5000) {
        return this.show(message, "success", duration);
    }

    error(message, duration = 5000) {
        return this.show(message, "error", duration);
    }

    warning(message, duration = 5000) {
        return this.show(message, "warning", duration);
    }

    info(message, duration = 5000) {
        return this.show(message, "info", duration);
    }

    remove(id) {
        const notificationData = this.notifications.find(
            (notification) => notification.id === id
        );

        if (!notificationData) {
            return;
        }

        const element = notificationData.element;

        element.classList.remove("show");
        element.classList.add("hide");

        setTimeout(() => {
            element.remove();

            this.notifications = this.notifications.filter(
                (notification) => notification.id !== id
            );
        }, 300);
    }

    clearAll() {
        [...this.notifications].forEach((notification) => {
            this.remove(notification.id);
        });
    }

    getCount() {
        return this.notifications.length;
    }
}

const notifications = new NotificationManager();

window.notifications = notifications;

window.showNotification = (message, type = "info", duration = 5000) => {
    return notifications.show(message, type, duration);
};

window.showSuccess = (message, duration = 5000) => {
    return notifications.success(message, duration);
};

window.showError = (message, duration = 5000) => {
    return notifications.error(message, duration);
};

window.showWarning = (message, duration = 5000) => {
    return notifications.warning(message, duration);
};

window.showInfo = (message, duration = 5000) => {
    return notifications.info(message, duration);
};