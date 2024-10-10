import os
import sys
import requests

def move_snake(commits):
    snake = "🐍"
    empty = "➡️"
    path = [empty] * len(commits)
    output = ""

    for i in range(len(commits)):
        path[i] = snake
        output = " ".join(path)
        path[i] = empty  # Limpa a posição anterior
    
    return output

def post_comment(repo, pr_number, comment):
    token = os.getenv('GITHUB_TOKEN')
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }
    payload = {'body': comment}
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code

if __name__ == "__main__":
    repo = os.getenv('GITHUB_REPOSITORY')
    pr_number = os.getenv('PR_NUMBER')
    commits = sys.argv[1:]
    
    snake_output = move_snake(commits)
    post_comment(repo, pr_number, snake_output)
