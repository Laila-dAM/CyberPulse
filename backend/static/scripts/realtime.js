const ws = new WebSocket("ws://localhost:8080/ws");

ws.onopen = () => {
    console.log("Connected to CyberPulse Realtime WebSocket");
};

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === "cpu") {
        updateCPUChart(data.value);
        document.getElementById("cpu-value").textContent = data.value + "%";
    }

    if (data.type === "ram") {
        updateRAMChart(data.value);
        document.getElementById("ram-value").textContent = data.value + "%";
    }

    if (data.type === "disk") {
        updateDiskChart(data.value);
        document.getElementById("disk-value").textContent = data.value + "%";
    }

    if (data.type === "network") {
        updateNetworkChart(data.in, data.out);
        document.getElementById("net-in-value").textContent = data.in + " KB/s";
        document.getElementById("net-out-value").textContent = data.out + " KB/s";
    }

    if (data.type === "temp") {
        updateTempChart(data.value);
        document.getElementById("temp-value").textContent = data.value + "°C";
    }
};

ws.onclose = () => {
    console.log("Realtime connection closed");
};
