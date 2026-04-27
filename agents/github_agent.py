from git import Repo

def push_to_github(project_name):
    repo = Repo.init(project_name)
    repo.git.add(all=True)
    repo.index.commit("Initial commit")

    repo.create_remote("origin", "https://github.com/YOUR_USERNAME/YOUR_REPO.git")
    repo.git.push("--set-upstream", "origin", "main")
