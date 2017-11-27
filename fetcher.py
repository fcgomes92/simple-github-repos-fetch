import webbrowser
import json
import sys
import argparse
from urllib import request

parser = argparse.ArgumentParser(description='Open some users latest repos on github')
parser.add_argument('-u','--username', 
                    dest='username',
                    type=str, 
                    help='GitHub Username', 
                    default='fcgomes92')

args = parser.parse_args()

username = 'fcgomes92' if not args.username else args.username

repos_url = 'https://api.github.com/users/{}/repos?sort=updated&type=all'.format(username)

print("Fetching {} repos".format(username))
with request.urlopen(repos_url) as response:
    if response.status == 200:
        repos = json.loads(response.read().decode())
    
        options = []
        for idx, repo in enumerate(repos):
            print("{:3}) {}".format(idx, repo.get('full_name')))
    
        title = 'Select one of the repos listed below to open it in your default browser: '
        
        try:
            selected = int(input(title))
            if selected > len(repos) - 1:
                raise ValueError
        except ValueError:
            print("Select a valid option!")
        except KeyboardInterrupt:
            print("\nBye bye")
        else:
            webbrowser.open_new_tab(repos[int(selected)].get('html_url'))
            print("Thanks for using this script!")
