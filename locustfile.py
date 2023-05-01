from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTUxNzkwLCJpYXQiOjE2ODI5NTExOTAsImp0aSI6IjExMWNiZWY0MTQ0ZjQ4NDVhNzI3ODM2MGVjZmUyMWU3IiwidXNlcl9pZCI6ImY3OTNkNDg3LTMyMWYtNDU5Yy1iZjJhLTg4YjhlNmVjOGVhZCJ9.QDzjlbndYJvYf1d-hXYNitXiZb7aPR_fpDtS7yQ2lDA'}

    @task
    def post_request(self):
        payload = {"name": "test"}
        response = self.client.post("/api/niche/", json=payload, headers=self.headers)
        if response.status_code == 200:
            print("Post request sent successfully")
        else:
            print("Error sending post request")