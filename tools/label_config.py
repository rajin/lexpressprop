import os
from dotenv import load_dotenv, find_dotenv
import requests
import yaml
from requests.models import Response
from typing import List, Dict, Callable, Optional
from requests.exceptions import HTTPError


def check_response(f: Callable) -> Callable:
    def _inner(*args, **kwargs) -> List[Optional[Dict]]:
        try:
            response = f(*args, **kwargs)
            response.raise_for_status()
            if response.status_code == 200: return response.json()
            else: return []
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
            
    return _inner


def find_repo_name() -> str:
    "Get repo name from .git/config."
    with open('.git/config', 'r') as f:
        gitconfig = f.readlines()

    url_ind = gitconfig.index('[remote "origin"]\n')+1
    url = gitconfig[url_ind]

    return url.split('/')[-1].split('.')[0]


class Hub:
    "Interface to Github."
    def __init__(self, repo: str, token: str):
        self.repo = repo
        self.headers = {
            'Accept': 'application/vnd.github.symmetra-preview+json',
            'Authorization': 'token ' + token   
        }
        self.url = f'https://api.github.com/repos/cortexlogic/{repo}'
        self.labels = self.get_labels()
        
    @check_response
    def get_labels(self) -> Response:
        "List all the labels in a repo."
        response = requests.get(f'{self.url}/labels', headers=self.headers)
        return response
    
    @check_response
    def _delete_label(self, name: str) -> Response:
        "Delete label by name."
        response = requests.delete(f"{self.url}/labels/{name}", headers=self.headers)
        return response
    
    @check_response
    def _add_label(self, label_obj: Dict) -> Response:
        "Add label to repo."
        response = requests.post(f"{self.url}/labels", headers=self.headers,
                                 json=label_obj)
        return response
        
    def delete_all_labels(self):
        "Delete all labels in repo."
        for label_obj in self.labels:
            self._delete_label(label_obj['name'])
        self.labels=[]
        
    def create_from_yaml(self, yaml_path: str='config/github_labels.yaml'):
        "Add labels defined in .yaml file."
        new_labels = yaml.safe_load(open(yaml_path, 'rb'))
        for label_obj in new_labels:
            self._add_label(label_obj)
        self.labels = new_labels
        

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
gh_token = os.environ.get('GITHUB_TOKEN')
repo = find_repo_name()

hub = Hub(repo, gh_token)

if __name__ == "__main__":
    hub.delete_all_labels()
    hub.create_from_yaml()