import os
import zipfile
import hashlib
import json
from datetime import datetime

def calculate_md5(file_path):
    """Calculate MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def create_bundle():
    # Configuration
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_zip = os.path.join(base_dir, "g7_v1.zip")
    manifest_path = os.path.join(base_dir, "version.json")
    chapters_subdir = os.path.join(base_dir, "g7_chapters") # New subdirectory for chapter files
    
    # 1. Collect all chapter JSON files (excluding manifest itself)
    if not os.path.exists(chapters_subdir):
        print(f"Error: Chapter subdirectory '{chapters_subdir}' not found. Please create it and move chapter JSON files there.")
        return

    json_files = [f for f in os.listdir(chapters_subdir) if f.endswith(".json")]
    
    print(f"Found {len(json_files)} chapter files. Bundling...")

    # 2. Create the ZIP archive
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in json_files:
            file_path = os.path.join(chapters_subdir, file)
            zipf.write(file_path, arcname=os.path.join("g7_chapters", file)) # Preserve subdirectory structure inside ZIP
            
    print(f"Successfully created: {output_zip}")

    # 3. Calculate MD5 Checksum
    zip_md5 = calculate_md5(output_zip)
    print(f"MD5 Checksum: {zip_md5}")

    # 4. Update the manifest (version.json)
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        
        # Update metadata
        manifest["updatedAt"] = datetime.utcnow().isoformat() + "Z"
        
        # Ensure bundles object exists
        if "bundles" not in manifest:
            manifest["bundles"] = {}
            
        # Store the MD5 and version
        manifest["bundles"]["g7_full_zip"] = "v1"
        manifest["bundles"]["g7_full_zip_md5"] = zip_md5
        
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print("Updated version.json with new MD5 checksum and timestamp.")
    else:
        print("Warning: version.json not found. Manifest update skipped.")

if __name__ == "__main__":
    try:
        create_bundle()
    except Exception as e:
        print(f"An error occurred: {e}")