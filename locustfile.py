# Imports classes from Locust
from locust import HttpUser, task 

# Instantiate a new virtual user
class HelloWorldUser(HttpUser): 
    # This tells locust to treat the method below 
    # as something the virtual user would do
    @task 
    # Define a new method
    def hello_world(self): 
        # This method will run an HTTP GET request on the path `/` 
        # of the site you are testing
        self.client.post("/todos/", {
            
        }) 

# class WebsiteUser(HttpUser):
#     wait_time = between(5, 15)
    
#     def on_start(self):
#         self.client.post("/login", {
#             "username": "test_user",
#             "password": ""
#         })
    
#     @task
#     def index(self):
#         self.client.get("/")
#         self.client.get("/static/assets.js")
        
#     @task
#     def about(self):
#         self.client.get("/about/")