import os
import json
from config.github_config import DATA_DIR

class RepoScanner:
    def scan(self):
        manifest = {
            "json": [],
            "txt": [],
            "pdf": [],
            "csv": []
        }

        for ext in manifest.keys():
            dir_path = os.path.join(DATA_DIR, ext)
            if os.path.exists(dir_path):
                manifest[ext] = [f for f in os.listdir(dir_path) if f.endswith(f".{ext}")]

        manifest_path = os.path.join(DATA_DIR, "dataset_manifest.json")
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

        print(f"Generated manifest: {manifest_path}")
        return manifest

repo_scanner = RepoScanner()
