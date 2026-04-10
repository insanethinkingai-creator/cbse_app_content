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

def create_bundles():
    # Configuration
    base_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(base_dir, "version.json")
    
    # Identify all grade-specific subdirectories (e.g., g7_chapters, g10_chapters)
    subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.endswith("_chapters")]
    
    if not subdirs:
        print("No chapter subdirectories found (expected folders like 'g7_chapters').")
        return

    # Load existing manifest or create new
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
    else:
        manifest = {"updatedAt": "", "bundles": {}}

    manifest["updatedAt"] = datetime.utcnow().isoformat() + "Z"

    for subdir in subdirs:
        grade_prefix = subdir.split('_')[0] # extracts 'g7' or 'g10'
        bundle_id = f"{grade_prefix}_full_zip"
        bundle_version = "v1"
        output_zip_name = f"{grade_prefix}_{bundle_version}.zip"
        output_zip = os.path.join(base_dir, output_zip_name)
        subdir_path = os.path.join(base_dir, subdir)

        json_files = [f for f in os.listdir(subdir_path) if f.endswith(".json")]
        
        print(f"Processing {grade_prefix}: Found {len(json_files)} files. Bundling...")

        # Create the ZIP archive for this grade
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in json_files:
                file_path = os.path.join(subdir_path, file)
                zipf.write(file_path, arcname=os.path.join(subdir, file))
                
        # Calculate MD5 and update manifest metadata
        zip_md5 = calculate_md5(output_zip)
        manifest["bundles"][bundle_id] = bundle_version
        manifest["bundles"][f"{bundle_id}_md5"] = zip_md5
        manifest["bundles"][f"{bundle_id}_filename"] = output_zip_name
        print(f"Generated {output_zip_name} (MD5: {zip_md5})")

    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print("Updated version.json successfully.")

if __name__ == "__main__":
    try:
        create_bundles()
    except Exception as e:
        print(f"An error occurred: {e}")