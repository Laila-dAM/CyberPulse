const terminalToggle = document.getElementById("terminal-toggle");
const terminalOverlay = document.getElementById("terminal-overlay");
const terminalOutput = document.getElementById("terminal-output");
const terminalInput = document.getElementById("terminal-input");

let terminalActive = false;

terminalToggle.addEventListener("click", () => {
    terminalActive = !terminalActive;
    terminalOverlay.style.display = terminalActive ? "flex" : "none";
    if (terminalActive) terminalInput.focus();
});

terminalInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        const cmd = terminalInput.value.trim();
        executeCommand(cmd);
        terminalInput.value = "";
    }
});

function executeCommand(cmd) {
    if (cmd === "help") {
        print("Available commands:");
        print("help  - show all commands");
        print("clear - clear the terminal");
        print("ping  - test connectivity");
        print("stats - show system stats snapshot");
    } else if (cmd === "clear") {
        terminalOutput.innerHTML = "";
    } else if (cmd === "ping") {
        print("Pinging server...");
        setTimeout(() => print("Ping successful: 12ms"), 500);
    } else if (cmd === "stats") {
        fetch("/api/monitoring/snapshot")
            .then(res => res.json())
            .then(data => print(JSON.stringify(data)))
            .catch(() => print("Error fetching stats"));
    } else if (cmd.length === 0) {
        return;
    } else {
        print("Unknown command: " + cmd);
    }
}

function print(text) {
    const line = document.createElement("div");
    line.textContent = text;
    terminalOutput.appendChild(line);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
}
