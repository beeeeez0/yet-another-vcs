import os


def init(repo=None):
    """Initalize a new repository"""
    if repo is None:
        repo_path = os.getcwd()
    elif os.path.exists(os.path.join(os.getcwd(), repo)):
        print(f"Directory {repo} already exists")
        return
    else:
        os.mkdir(repo)
        repo_path = os.path.join(os.getcwd(), repo)

    os.mkdir(os.path.join(repo_path, ".git"))
    os.mkdir(os.path.join(repo_path, ".git", "objects"))
    os.mkdir(os.path.join(repo_path, ".git", "refs"))
    os.mkdir(os.path.join(repo_path, ".git", "refs", "heads"))
    os.mkdir(os.path.join(repo_path, ".git", "refs", "tags"))
    with open(os.path.join(repo_path, ".git", "HEAD"), "w") as f:
        f.write("ref: refs/heads/master")
    print(f"Initalized a repository in {repo_path}")
