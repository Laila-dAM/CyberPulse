class Utils {
    static formatNumber(value) {
        return new Intl.NumberFormat("en-US").format(value);
    }

    static formatCurrency(value, currency = "USD") {
        return new Intl.NumberFormat("en-US", {
            style: "currency",
            currency: currency
        }).format(value);
    }

    static formatPercentage(value, decimals = 0) {
        return `${Number(value).toFixed(decimals)}%`;
    }

    static formatDate(date) {
        return new Date(date).toLocaleDateString("en-US", {
            year: "numeric",
            month: "short",
            day: "numeric"
        });
    }

    static formatDateTime(date) {
        return new Date(date).toLocaleString("en-US", {
            year: "numeric",
            month: "short",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit"
        });
    }

    static formatTime(date) {
        return new Date(date).toLocaleTimeString("en-US", {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit"
        });
    }

    static generateId(prefix = "id") {
        return `${prefix}-${Date.now()}-${Math.random()
            .toString(36)
            .substring(2, 10)}`;
    }

    static randomNumber(min, max) {
        return Math.floor(
            Math.random() * (max - min + 1)
        ) + min;
    }

    static randomFloat(min, max, decimals = 2) {
        return Number(
            (
                Math.random() * (max - min) +
                min
            ).toFixed(decimals)
        );
    }

    static clamp(value, min, max) {
        return Math.min(
            Math.max(value, min),
            max
        );
    }

    static debounce(callback, delay = 300) {
        let timeout;

        return (...args) => {
            clearTimeout(timeout);

            timeout = setTimeout(() => {
                callback(...args);
            }, delay);
        };
    }

    static throttle(callback, limit = 300) {
        let waiting = false;

        return (...args) => {
            if (waiting) {
                return;
            }

            callback(...args);

            waiting = true;

            setTimeout(() => {
                waiting = false;
            }, limit);
        };
    }

    static deepClone(data) {
        return JSON.parse(
            JSON.stringify(data)
        );
    }

    static capitalize(text) {
        if (!text) {
            return "";
        }

        return (
            text.charAt(0).toUpperCase() +
            text.slice(1)
        );
    }

    static slugify(text) {
        return text
            .toLowerCase()
            .trim()
            .replace(/\s+/g, "-")
            .replace(/[^\w-]+/g, "")
            .replace(/--+/g, "-");
    }

    static sleep(milliseconds) {
        return new Promise((resolve) => {
            setTimeout(resolve, milliseconds);
        });
    }

    static isEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(
            email
        );
    }

    static isEmpty(value) {
        return (
            value === null ||
            value === undefined ||
            value === "" ||
            (Array.isArray(value) &&
                value.length === 0)
        );
    }

    static getStorage(key, fallback = null) {
        try {
            const value =
                localStorage.getItem(key);

            return value
                ? JSON.parse(value)
                : fallback;
        } catch {
            return fallback;
        }
    }

    static setStorage(key, value) {
        localStorage.setItem(
            key,
            JSON.stringify(value)
        );
    }

    static removeStorage(key) {
        localStorage.removeItem(key);
    }

    static copyToClipboard(text) {
        return navigator.clipboard.writeText(
            text
        );
    }

    static downloadFile(
        filename,
        content,
        type = "text/plain"
    ) {
        const blob = new Blob([content], {
            type: type
        });

        const url =
            URL.createObjectURL(blob);

        const link =
            document.createElement("a");

        link.href = url;
        link.download = filename;

        document.body.appendChild(link);

        link.click();

        link.remove();

        URL.revokeObjectURL(url);
    }

    static query(selector) {
        return document.querySelector(selector);
    }

    static queryAll(selector) {
        return [
            ...document.querySelectorAll(
                selector
            )
        ];
    }

    static createElement(
        tag,
        className = ""
    ) {
        const element =
            document.createElement(tag);

        if (className) {
            element.className = className;
        }

        return element;
    }

    static getCurrentPage() {
        return window.location.pathname
            .split("/")
            .pop();
    }

    static isDarkMode() {
        return (
            document.documentElement.getAttribute(
                "data-theme"
            ) === "dark"
        );
    }

    static bytesToSize(bytes) {
        const sizes = [
            "Bytes",
            "KB",
            "MB",
            "GB",
            "TB"
        ];

        if (bytes === 0) {
            return "0 Bytes";
        }

        const index = Math.floor(
            Math.log(bytes) /
                Math.log(1024)
        );

        return `${(
            bytes /
            Math.pow(1024, index)
        ).toFixed(2)} ${sizes[index]}`;
    }

    static uptime(seconds) {
        const days = Math.floor(
            seconds / 86400
        );

        const hours = Math.floor(
            (seconds % 86400) / 3600
        );

        const minutes = Math.floor(
            (seconds % 3600) / 60
        );

        return `${days}d ${hours}h ${minutes}m`;
    }
}

window.Utils = Utils;