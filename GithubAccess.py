import requests
import json

def get_repos(username):
    res = requests.get('https://api.github.com/users/' + username + '/repos')
    return res.json()

print (get_repos("caseyvtcd"))