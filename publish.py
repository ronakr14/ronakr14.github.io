import os
import shutil
import subprocess
from datetime import datetime


def remove_folder_if_exists(folder_path):
    """Remove a folder if it exists."""
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        shutil.rmtree(folder_path)
        print(f"Removed folder: {folder_path}")
    else:
        print(f"Folder does not exist: {folder_path}")


def run_command(command):
    """Run a shell command and print its output."""
    try:
        result = subprocess.run(command, check=True, shell=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e.stderr}")
        exit(1)


def main(directory, hugo_folder, git_folder):
    # Step 1: Remove the 'docs' folder if it exists
    public_path = os.path.join(directory, hugo_folder)
    docs_path = os.path.join(directory, git_folder)
    remove_folder_if_exists(public_path)
    remove_folder_if_exists(docs_path)

    # Step 2: Run 'hugo build' command
    print("Running 'hugo build' command...")
    run_command("hugo build")

    # Step 3: Rename 'public' folder to 'docs'
    if os.path.exists(public_path) and os.path.isdir(public_path):
        os.rename(public_path, docs_path)
        print(f"Renamed {public_path} folder to {docs_path}.")
    else:
        print("Error: 'public' folder does not exist.")

    # Step 4: Run 'git add .' command
    print("Running 'git add .' command...")
    run_command("git add .")

    # Step 5: Run 'git commit' command with current timestamp
    commit_message = f"publish via python {datetime.now()}"
    print(f"Running 'git commit' with message: '{commit_message}'...")
    run_command(f'git commit -m "{commit_message}"')

    # Step 6: Run 'git push' command
    print("Running 'git push' command...")
    run_command("git push")


if __name__ == "__main__":
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    hugo_folder = 'public'
    git_folder = 'docs'
    main(directory, hugo_folder, git_folder)
