import urllib.request
import json
import sys

# Configuration
GITHUB_USER = "insanethinkingai-creator"
GITHUB_REPO = "cbse_app_content"
TARGET_FILE = "version.json"

def purge_jsdelivr_cache(file_path):
    """
    Triggers a cache purge on jsDelivr for a specific file.
    """
    purge_url = f"https://purge.jsdelivr.net/gh/{GITHUB_USER}/{GITHUB_REPO}@latest/{file_path}"
    
    print(f"--- CDN Purge Utility ---")
    print(f"Target: {GITHUB_USER}/{GITHUB_REPO} -> {file_path}")
    print(f"Requesting: {purge_url}")
    
    try:
        with urllib.request.urlopen(purge_url) as response:
            status = response.getcode()
            data = json.loads(response.read().decode('utf-8'))
            
            if status == 200 and data.get("status") == "finished":
                print(f"SUCCESS: Cache cleared for {file_path}")
                print(f"Provider Results: {data.get('providers')}")
            else:
                print(f"WARNING: Purge request sent but response was unexpected: {data}")
    except Exception as e:
        print(f"ERROR: Failed to purge cache. Ensure the file exists on GitHub. \nDetails: {e}")

if __name__ == "__main__":
    # Defaults to version.json, but you can pass a specific filename as an argument
    file_to_purge = sys.argv[1] if len(sys.argv) > 1 else TARGET_FILE
    purge_jsdelivr_cache(file_to_purge)