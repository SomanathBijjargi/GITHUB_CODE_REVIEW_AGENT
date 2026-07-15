import requests
from config.settings import settings

class GitHubService:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3.diff",
        }

    def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> str:
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.text  # returns the raw diff

    def post_comment(self, owner: str, repo: str, pr_number: int, body: str):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues/{pr_number}/comments"
        headers = {**self.headers, "Accept": "application/vnd.github+json"}
        response = requests.post(url, json={"body": body}, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def get_pr_details(self,owner,repo,pr_number):
        url = (
            f"{self.BASE_URL}/repos/"
            f"{owner}/{repo}/pulls/{pr_number}"
        )
        headers = {"Authorization":f"Bearer {settings.GITHUB_TOKEN}","Accept":"application/vnd.github+json"}
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        return response.json()
    
    def get_pr_commits(self,owner,repo,pr_number):
        url = (
            f"{self.BASE_URL}/repos/"
            f"{owner}/{repo}/pulls/{pr_number}/commits"
        )
        response = requests.get(url,headers=self.headers)
        response.raise_for_status()
        return response.json()

github_service = GitHubService()