SELECT *
FROM metrics
WHERE timestamp >= NOW() - INTERVAL '24 HOURS'
ORDER BY timestamp ASC;
