import requests
from utils.schema_validator import Validate_schema




Baseurl = "https://jsonplaceholder.typicode.com/"
Schema_path_posts="https://jsonplaceholder.typicode.com/posts"




class Test_jsonplaceholder():
        
            
    def test_get_website(self):
        self.response = requests.get(Baseurl)
        assert self.response.status_code == 200
        
    def test_get_posts_1(self):
        self.posts = "posts"
        self.posts_id=1
        self.response=requests.get(f"{Baseurl}/{self.posts}/{self.posts_id}")
        print(self.response.json())
        assert Validate_schema(self.response,"https://jsonplaceholder.typicode.com/posts/1")
        
    def test_post_posts_new(self):
        self.posts = "posts"
        self.data = {"userId":10,"title":"Testing the post requests"}
        self.response=requests.post(f"{Baseurl}/posts", json=self.data)
        assert self.response.status_code == 201
        print(self.response.json())
        assert self.response.json()['userId'] == 10

    def test_post_Update(self):
        self.data = {"title":"New line"}
        self.reponse = requests.patch(f"{Baseurl}/posts/101",data=self.data)
        print(self.response.json())
        self.reponse_json=self.response.json()
        assert self.reponse_json["title"] == self.data["title"]

    def test_delete_post(self):
        self.response=requests.delete(f"{Baseurl}/posts/1")
        assert self.response.status_code == 200
        assert self.response.json()== {}
        assert self.reponse.elapsed.total_seconds() < 2
               
        
        
scanner = Test_jsonplaceholder()
#scanner.test_get_website()
scanner.test_get_posts_1()
#scanner.test_post_posts_new()
#scanner.test_post_Update()
#scanner.test_delete_post()

        