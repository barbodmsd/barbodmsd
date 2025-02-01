import os
import subprocess


def create_git_commit(commit_message, custom_date, file_path):
    """
    Creates a git commit with a custom date.

    :param commit_message: The message for the commit.
    :param custom_date: The date for the commit in ISO 8601 format (e.g., "2025-01-01T12:00:00").
    :param file_path: The path to the file to modify and commit.
    """
    try:
        # Ensure the file exists
        with open(file_path, "a") as f:
            f.write("\n.\n")

        # Stage the file
        subprocess.run(["git", "add", file_path], check=True)

        # Create the commit with the custom date
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = custom_date
        env["GIT_COMMITTER_DATE"] = custom_date
        subprocess.run(["git", "commit", "-m", commit_message],
                       check=True, env=env)

        print("Commit created successfully with custom date:", custom_date)
    except subprocess.CalledProcessError as e:
        print("Error executing Git command:", e)
    except Exception as ex:
        print("Error:", ex)


# Example usage
if __name__ == "__main__":
    commit_message = "Commit with a custom date"
    custom_date = "2025-01-01T12:00:00"  # ISO 8601 format
    file_path = "example.txt"

    create_git_commit(commit_message, custom_date, file_path)
