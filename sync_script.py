
import requests
import os
from datetime import datetime

HANDLE = "EnvyThunder"

def get_solved_problems():
    url = f"https://codeforces.com/api/user.status?handle={HANDLE}"
    response = requests.get(url).json()
    return [s for s in response['result'] if s['verdict'] == 'OK']

def update_problem_files(solved):
    for submission in solved:
        problem = submission['problem']
        filename = f"problems/{problem['contestId']}{problem['index']}.md"
        
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write(f"# {problem['name']}\n")
                f.write(f"- Rating: {problem.get('rating', '?')}\n")
                f.write(f"- Tags: {', '.join(problem.get('tags', []))}\n")
                f.write(f"- Solved: {datetime.fromtimestamp(submission['creationTimeSeconds'])}\n")
                f.write(f"- [Problem Link](https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']})\n")

if __name__ == "__main__":
    solved = get_solved_problems()
    os.makedirs("problems", exist_ok=True)
    update_problem_files(solved)
