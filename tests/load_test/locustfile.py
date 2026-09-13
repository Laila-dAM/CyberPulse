import random

from locust import HttpUser, between, task


class CyberPulseUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_dashboard(self):
        """Request the metrics dashboard."""
        self.client.get("/api/metrics")

    @task
    def get_cpu(self):
        """Request CPU metrics."""
        self.client.get("/api/metrics/cpu")

    @task
    def get_ram(self):
        """Request RAM metrics."""
        self.client.get("/api/metrics/ram")

    @task
    def get_disk(self):
        """Request disk metrics."""
        self.client.get("/api/metrics/disk")

    @task
    def get_network(self):
        """Request network metrics."""
        self.client.get("/api/metrics/network")

    @task
    def get_temp(self):
        """Request temperature metrics."""
        self.client.get("/api/metrics/temp")

    @task
    def random_metric(self):
        """Request a random metric endpoint."""
        endpoints = [
            "/api/metrics/cpu",
            "/api/metrics/ram",
            "/api/metrics/disk",
            "/api/metrics/network",
            "/api/metrics/temp",
        ]
        self.client.get(random.choice(endpoints))
