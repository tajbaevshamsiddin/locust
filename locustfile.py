from locust import HttpUser, task , between


class LoadTesting(HttpUser):
    wait_time = between(5, 15)
    
    # @task
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })
    
    @task
    def about(self):
        self.client.get("/api/niche/")