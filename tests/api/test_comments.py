import requests
from utils.schema_validator import Validate_schema
import pytest



class Testjsonplaceholder_comments:
    
    postId=5
    comments ="comments"
    posts="posts"
        
    
    def test_Base_url(self,api_client):
        self.client=api_client.get("/")
        assert  self.client.status_code == 200
    '''
    
    def test_get_comments(self,base_url):
        response=requests.get(f"{base_url}/{self.comments}")
        assert response.status_code == 200                              #Status code check
        Validate_schema(response.json(),"schemas/comments_schema.json")        #Schema Validator
   '''     
    def test_get_comments_2(self,api_client):
        self.postId=2
        response=api_client.get(f"/comments/{self.postId}")
        assert "application/json" in response.headers["Content-Type"]      #Header (authorization, content-type,cache-control)
        assert response.json()["email"] == "Jayne_Kuhic@sydney.com"         #Reponse email check
        assert "dolore" in response.json()["body"]
        
    def test_Query(self,api_client):
        self.postId=2
        response=api_client.get(f"/comments?postId={self.postId}")
        assert "application/json" in response.headers["Content-Type"]    
        for item in response.json():                                    #Header (authorization, content-type,cache-control)
            Validate_schema(item,"schemas/comments_schema.json")
        
    @pytest.mark.smoke
    def test_Invalid_query(self,api_client):
        response=api_client.get(f"/{self.posts}/{self.comments}")
        assert response.status_code == 404
        
    