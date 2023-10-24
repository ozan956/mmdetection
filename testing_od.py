import git
import os

def push_to_github(repo_path, commit_message, remote_name='origin', branch_name='master'):
    # Ensure the provided path exists
    if not os.path.exists(repo_path):
        raise ValueError(f"Provided path '{repo_path}' does not exist.")

    # Initialize repo object
    repo = git.Repo(repo_path)

    # Add all changes
    repo.git.add(A=True)

    # Commit the changes
    repo.index.commit(commit_message)

    # Push the changes
    origin = repo.remote(name=remote_name)
    origin.push(branch_name)

# Example Usage:
repo_path = '/path/to/your/repo' # Change this to your repository path
commit_message = 'Added new files' # Change this to your desired commit message
push_to_github(repo_path, commit_message)
