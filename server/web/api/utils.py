import os


def make_git_path(name: str) -> str:
    # use all lower case, replace any spaces with hyphens, and append ".git" to the name.
    return name.lower().replace(" ", "-") + ".git"

def create_git_project(filepath: str) -> None:
    # Check if path to model exists
    if os.path.exists(filepath):
        print("exists")
        raise Exception(f"Path {filepath} already exists")
    os.system(f"git init --bare {filepath}")
