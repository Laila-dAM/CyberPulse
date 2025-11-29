INSERT INTO metrics (
    timestamp,
    cpu_usage,
    ram_usage,
    disk_usage,
    net_in,
    net_out,
    temperature,
    alert_flag
) VALUES (
    NOW(),
    :cpu_usage,
    :ram_usage,
    :disk_usage,
    :net_in,
    :net_out,
    :temperature,
    :alert_flag
);
