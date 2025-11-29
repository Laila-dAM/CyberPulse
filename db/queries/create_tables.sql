DROP TABLE IF EXISTS predictions;
DROP TABLE IF EXISTS alerts;
DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS metrics;
DROP TABLE IF EXISTS users;

CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cpu_usage FLOAT NOT NULL,
    ram_usage FLOAT NOT NULL,
    disk_usage FLOAT NOT NULL,
    net_in FLOAT NOT NULL,
    net_out FLOAT NOT NULL,
    temperature FLOAT,
    alert_flag BOOLEAN DEFAULT FALSE
);

CREATE TABLE alerts (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    metric_id INT NOT NULL REFERENCES metrics(id) ON DELETE CASCADE,
    alert_type VARCHAR(50) NOT NULL,
    description TEXT NOT NULL,
    resolved BOOLEAN DEFAULT FALSE
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) DEFAULT 'viewer',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    metric_id INT NOT NULL REFERENCES metrics(id) ON DELETE CASCADE,
    predicted_cpu FLOAT,
    predicted_ram FLOAT,
    predicted_disk FLOAT,
    prediction_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    log_level VARCHAR(20) NOT NULL,
    source VARCHAR(50),
    message TEXT NOT NULL
);
