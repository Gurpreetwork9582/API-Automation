import requests
from utils.schema_validator import Validate_schema
import pytest


Schema_path_posts="https://jsonplaceholder.typicode.com/posts"


class Testjsonplaceholder_posts:
    
            
    def test_get_website(self,base_url):
        self.response = requests.get(base_url)
        assert self.response.status_code == 200
        
    @pytest.mark.parametrize("postId",[1,2,3,4,5])                  #parametrized 
    def test_get_posts_1(self,base_url,postId):
        self.posts = "posts"
        self.response=requests.get(f"{base_url}/{self.posts}/{postId}")       #Get check
        print(self.response.json())
        Validate_schema(self.response.json(), "schemas/posts_schema.json")
        
    @pytest.mark.smoke    
    def test_post_posts_new(self,base_url):
        self.posts = "posts"
        self.data = {"userId":10,"title":"Testing the post requests"}
        self.response=requests.post(f"{base_url}/posts", json=self.data)             #Create Check
        assert self.response.status_code == 201                     
        print(self.response.json())
        assert self.response.json()['userId'] == 10

    def test_post_Update(self,base_url):
        self.data = {"title":"New line"}
        self.response = requests.put(f"{base_url}/posts/101",json=self.data)         #Update Check
        print(self.response.text)
        #self.response_json=self.response.json()
        #assert self.response_json["title"] == self.data["title"]

    def test_delete_post(self,base_url):
        self.response=requests.delete(f"{base_url}/posts/1")                         #Delete check
        assert self.response.status_code == 200
        assert self.response.json()== {}
        assert self.response.elapsed.total_seconds() < 2                            #Response time check