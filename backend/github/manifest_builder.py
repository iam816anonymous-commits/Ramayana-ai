import os
import json

class ManifestBuilder:
    def build(self, data_dir="data"):
        # Simplified for now as repo_scanner does the main job
        from github.repo_scanner import repo_scanner
        return repo_scanner.scan()

manifest_builder = ManifestBuilder()
