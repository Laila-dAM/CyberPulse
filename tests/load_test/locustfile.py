from locust import HttpUser, task, between
import random

class CyberPulseUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_dashboard(self):
        self.client.get("/api/metrics")

    @task
    def get_cpu(self):
        self.client.get("/api/metrics/cpu")

    @task
    def get_ram(self):
        self.client.get("/api/metrics/ram")

    @task
    def get_disk(self):
        self.client.get("/api/metrics/disk")

    @task
    def get_network(self):
        self.client.get("/api/metrics/network")

    @task
    def get_temp(self):
        self.client.get("/api/metrics/temp")

    @task
    def random_metric(self):
        endpoints = [
            "/api/metrics/cpu",
            "/api/metrics/ram",
            "/api/metrics/disk",
            "/api/metrics/network",
            "/api/metrics/temp"
        ]
        self.client.get(random.choice(endpoints))
