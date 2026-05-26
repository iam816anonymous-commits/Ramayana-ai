import os
import json
from github.repo_sync import repo_sync
from github.repo_scanner import repo_scanner

class DataFetcher:
    """Orchestrates the sync and discovery process."""
    def fetch_all(self):
        print("Starting data fetch sequence...")
        synced = repo_sync.sync()
        manifest = repo_scanner.scan()
        return manifest

data_fetcher = DataFetcher()
