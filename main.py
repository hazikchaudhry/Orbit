from github import Github
import os 

from dotenv import load_dotenv


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

REPO_NAME = "UoaWDCC/VPS"


def get_pr_diff(pr):
    changes = pr.get_files()

    diff = ""

    for file in changes:
        diff += f"\n--- {file.filename} ---\n"
        diff = file.patch or "no diff it seems :("

    return diff 

github = Github(GITHUB_TOKEN)

repo = github.get_repo(REPO_NAME)

prs = repo.get_pulls( state="open")

for pr in prs:
    print(f"PR Title: {pr.title}")

    changes_text = get_pr_diff(pr)

    print(changes_text)
    print("-" * 40)

    