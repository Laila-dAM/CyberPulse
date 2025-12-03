const cpuChartCtx = document.getElementById("cpuChart").getContext("2d");
const ramChartCtx = document.getElementById("ramChart").getContext("2d");
const diskChartCtx = document.getElementById("diskChart").getContext("2d");
const netChartCtx = document.getElementById("netChart").getContext("2d");

function createLineChart(ctx, label, color) {
    return new Chart(ctx, {
        type: "line",
        data: {
            labels: [],
            datasets: [
                {
                    label: label,
                    data: [],
                    borderColor: color,
                    backgroundColor: color + "22",
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            animation: false,
            scales: {
                x: { ticks: { color: "#ccc" } },
                y: { ticks: { color: "#ccc" } }
            },
            plugins: {
                legend: { labels: { color: "#fff" } }
            }
        }
    });
}

const cpuChart = createLineChart(cpuChartCtx, "CPU Usage (%)", "#39ff14");
const ramChart = createLineChart(ramChartCtx, "RAM Usage (%)", "#b026ff");
const diskChart = createLineChart(diskChartCtx, "Disk Usage (%)", "#00eaff");
const netChart = createLineChart(netChartCtx, "Network (KB/s)", "#ff00c8");

function updateChart(chart, value) {
    const time = new Date().toLocaleTimeString();
    if (chart.data.labels.length > 20) {
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
    }
    chart.data.labels.push(time);
    chart.data.datasets[0].data.push(value);
    chart.update();
}

async function updateCharts() {
    const cpu = await fetch("/api/cpu").then(r => r.json());
    const ram = await fetch("/api/ram").then(r => r.json());
    const disk = await fetch("/api/disk").then(r => r.json());
    const net = await fetch("/api/network").then(r => r.json());

    updateChart(cpuChart, cpu.value);
    updateChart(ramChart, ram.value);
    updateChart(diskChart, disk.value);
    updateChart(netChart, net.value);
}

setInterval(updateCharts, 3000);
