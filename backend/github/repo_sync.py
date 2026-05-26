import os
import subprocess
import shutil
from config.github_config import GITHUB_REPO_URL, GITHUB_BRANCH, LOCAL_CACHE_DIR, DATA_DIR

class RepoSync:
    def __init__(self):
        self.repo_dir = os.path.join(LOCAL_CACHE_DIR, "repo")
        os.makedirs(LOCAL_CACHE_DIR, exist_ok=True)

    def sync(self):
        if not os.path.exists(self.repo_dir):
            print(f"Cloning {GITHUB_REPO_URL}...")
            # We use a mock or skip if URL is placeholder for now,
            # but the architecture must support the real git call.
            if "USER" in GITHUB_REPO_URL:
                print("Using placeholder URL, skipping actual clone. Ensure GITHUB_REPO_URL is set.")
                return False

            subprocess.run(["git", "clone", "-b", GITHUB_BRANCH, GITHUB_REPO_URL, self.repo_dir], check=True)
        else:
            print(f"Pulling latest changes from {GITHUB_REPO_URL}...")
            subprocess.run(["git", "-C", self.repo_dir, "pull", "origin", GITHUB_BRANCH], check=True)

        self._update_local_data()
        return True

    def _update_local_data(self):
        """Copies discovered data files to the project's data directory."""
        for sub in ["json", "txt", "pdf", "csv"]:
            src = os.path.join(self.repo_dir, "data", sub)
            dst = os.path.join(DATA_DIR, sub)
            if os.path.exists(src):
                os.makedirs(dst, exist_ok=True)
                for f in os.listdir(src):
                    shutil.copy2(os.path.join(src, f), os.path.join(dst, f))
                print(f"Synced {sub} files.")

repo_sync = RepoSync()
