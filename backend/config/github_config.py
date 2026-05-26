import os

GITHUB_REPO_URL = os.getenv("GITHUB_REPO_URL", "https://github.com/USER/RamayanaAIData")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")
AUTO_SYNC = os.getenv("AUTO_SYNC", "true").lower() == "true"
LOCAL_CACHE_DIR = "cache/github"
DATA_DIR = "data"
