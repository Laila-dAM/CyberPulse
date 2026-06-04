class StateManager {
    constructor() {
        this.state = {
            user: null,
            metrics: [],
            alerts: [],
            settings: {},
            notifications: [],
            theme: "dark",
            loading: false,
            sidebarOpen: true,
            lastUpdated: null
        };

        this.listeners = {};
    }

    get(key) {
        return this.state[key];
    }

    getState() {
        return {
            ...this.state
        };
    }

    set(key, value) {
        this.state[key] = value;
        this.state.lastUpdated = new Date().toISOString();

        this.notify(key, value);
        this.save();
    }

    update(data) {
        Object.keys(data).forEach((key) => {
            this.state[key] = data[key];
            this.notify(key, data[key]);
        });

        this.state.lastUpdated = new Date().toISOString();

        this.save();
    }

    subscribe(key, callback) {
        if (!this.listeners[key]) {
            this.listeners[key] = [];
        }

        this.listeners[key].push(callback);

        return () => {
            this.unsubscribe(
                key,
                callback
            );
        };
    }

    unsubscribe(key, callback) {
        if (!this.listeners[key]) {
            return;
        }

        this.listeners[key] =
            this.listeners[key].filter(
                (listener) =>
                    listener !== callback
            );
    }

    notify(key, value) {
        if (!this.listeners[key]) {
            return;
        }

        this.listeners[key].forEach(
            (callback) => {
                callback(value);
            }
        );
    }

    save() {
        localStorage.setItem(
            "cyberpulseState",
            JSON.stringify(this.state)
        );
    }

    load() {
        const savedState =
            localStorage.getItem(
                "cyberpulseState"
            );

        if (!savedState) {
            return;
        }

        try {
            const parsedState =
                JSON.parse(savedState);

            this.state = {
                ...this.state,
                ...parsedState
            };
        } catch (error) {
            console.error(error);
        }
    }

    reset() {
        this.state = {
            user: null,
            metrics: [],
            alerts: [],
            settings: {},
            notifications: [],
            theme: "dark",
            loading: false,
            sidebarOpen: true,
            lastUpdated: null
        };

        localStorage.removeItem(
            "cyberpulseState"
        );
    }

    addNotification(
        message,
        type = "info"
    ) {
        const notification = {
            id: this.generateId(),
            message,
            type,
            createdAt:
                new Date().toISOString()
        };

        this.state.notifications.push(
            notification
        );

        this.notify(
            "notifications",
            this.state.notifications
        );

        this.save();

        return notification;
    }

    removeNotification(id) {
        this.state.notifications =
            this.state.notifications.filter(
                (notification) =>
                    notification.id !== id
            );

        this.notify(
            "notifications",
            this.state.notifications
        );

        this.save();
    }

    clearNotifications() {
        this.state.notifications = [];

        this.notify(
            "notifications",
            this.state.notifications
        );

        this.save();
    }

    generateId() {
        return (
            Date.now().toString(36) +
            Math.random()
                .toString(36)
                .substring(2, 10)
        );
    }
}

const state = new StateManager();

state.load();

window.state = state;