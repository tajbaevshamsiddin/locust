from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)
    # headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '}

    # @task
    # def post_request(self):
    #     payload = {"name": "test"}
    #     response = self.client.post("/api/niche/", json=payload, headers=self.headers)
    #     if response.status_code == 201:
    #         print("Post request sent successfully")
    #     else:
    #         print("Error sending post request")

    @task
    def about(self):
        self.client.get("/api/niche/")