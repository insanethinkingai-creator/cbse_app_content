import os
import zipfile
import hashlib
import json
from datetime import datetime
import urllib.request

# CDN Purge Configuration
GITHUB_USER = "insanethinkingai-creator"
GITHUB_REPO = "cbse_app_content"

def calculate_md5(file_path):
    """Calculate MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def validate_json(file_path, is_manifest=False):
    """Validate JSON syntax and basic schema requirements."""
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Syntax Error in {file_path}: {e}")

    if is_manifest:
        required_manifest = ["updatedAt", "bundles", "enabledGrades"]
        for key in required_manifest:
            if key not in data:
                raise ValueError(f"Schema Error: Manifest missing required key '{key}'")
    else:
        # Chapter File Schema Validation
        required_chapter = ["id", "grade", "subject", "number", "title", "version", "questions"]
        for key in required_chapter:
            if key not in data:
                raise ValueError(f"Schema Error in {file_path}: Missing key '{key}'")

        # Validate question count based on grade
        grade = str(data.get("grade"))
        expected_count = 40
        actual_count = len(data.get("questions", []))
        if actual_count < expected_count:
            raise ValueError(f"Data Error in {file_path}: Expected at least {expected_count} questions for Grade {grade}, but found only {actual_count}")

        for i, q in enumerate(data.get("questions", [])):
            q_id = q.get("id", f"index_{i}")
            # Check required question keys
            for field in ["id", "text", "options", "correctIndex"]:
                if field not in q:
                    raise ValueError(f"Schema Error in {file_path}: Question '{q_id}' missing '{field}'")
            
            # Validate options array
            options = q.get("options")
            if not isinstance(options, list) or len(options) != 4:
                raise ValueError(f"Data Error in {file_path}: Question '{q_id}' must have exactly 4 options")
            
            # Validate correctIndex bounds
            idx = q.get("correctIndex")
            if not isinstance(idx, int) or not (0 <= idx <= 3):
                raise ValueError(f"Data Error in {file_path}: Question '{q_id}' has invalid correctIndex: {idx}")
    return data

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
        manifest = validate_json(manifest_path, is_manifest=True)
        if "enabledGrades" not in manifest:
            manifest["enabledGrades"] = []
    else:
        manifest = {"updatedAt": "", "enabledGrades": [], "bundles": {}}

    manifest["updatedAt"] = datetime.utcnow().isoformat() + "Z"

    processed_grades = set()

    for subdir in subdirs:
        grade_prefix = subdir.split('_')[0] # extracts 'g7' or 'g10'
        bundle_id = f"{grade_prefix}_full_zip"
        subdir_path = os.path.join(base_dir, subdir)

        json_files = [f for f in os.listdir(subdir_path) if f.endswith(".json")]

        if not json_files:
            print(f"Skipping {grade_prefix}: No JSON files found in {subdir}. skipping bundle creation.")
            continue
        
        print(f"Processing {grade_prefix}: Found {len(json_files)} files ({', '.join(json_files)}). Bundling...")

        # Create the ZIP archive for this grade
        temp_zip = os.path.join(base_dir, f"{grade_prefix}_temp.zip")
        with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in json_files:
                file_path = os.path.join(subdir_path, file)
                # Validate each file before adding it to the bundle
                validate_json(file_path, is_manifest=False)
                zipf.write(file_path, arcname=os.path.join(subdir, file))
                
        # Calculate MD5 and update manifest metadata
        zip_md5 = calculate_md5(temp_zip)
        short_hash = zip_md5[:8]
        output_zip_name = f"{grade_prefix}_{short_hash}.zip"
        output_zip = os.path.join(base_dir, output_zip_name)
        
        # Rename temp to hashed name
        if os.path.exists(output_zip):
            os.remove(output_zip)
        os.rename(temp_zip, output_zip)

        manifest["bundles"][bundle_id] = short_hash
        manifest["bundles"][f"{bundle_id}_md5"] = zip_md5
        manifest["bundles"][f"{bundle_id}_filename"] = output_zip_name
        print(f"Generated {output_zip_name} (MD5: {zip_md5})")
        processed_grades.add(grade_prefix)

    # Sync enabledGrades and sort descending (g12 to g7)
    manifest["enabledGrades"] = sorted(list(processed_grades), key=lambda x: int(x[1:]) if x[1:].isdigit() else 0, reverse=True)

    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print("Updated version.json successfully.")

    # Trigger CDN Purge for the manifest to ensure mirrors update immediately
    purge_url = f"https://purge.jsdelivr.net/gh/{GITHUB_USER}/{GITHUB_REPO}@latest/version.json"
    print(f"Purging CDN cache for manifest: {purge_url}")
    try:
        with urllib.request.urlopen(purge_url) as response:
            print(f"CDN response: {response.read().decode('utf-8')}")
    except Exception as e:
        print(f"CDN purge request failed: {e}")

if __name__ == "__main__":
    try:
        create_bundles()
    except Exception as e:
        print(f"An error occurred: {e}")