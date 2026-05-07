import requests



Baseurl = "https://jsonplaceholder.typicode.com/"


class jsonplaceholder():
    def get_website(self):
        self.response = requests.get(Baseurl)
        assert self.response.status_code ==200
        print(self.response.text)
        
    def get_posts(self):
        self.posts = "posts"
        self.posts_id=1
        self.response=requests.get(f"{Baseurl}/{self.posts}/{self.posts_id}")
        print(self.response.json())
        
        
        
        
        
        
scanner = jsonplaceholder()
scanner.get_website()
scanner.get_posts()