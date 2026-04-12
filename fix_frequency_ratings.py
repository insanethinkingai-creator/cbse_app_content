import os
import json

def fix_ratings():
    """
    Iterates through all chapter subdirectories and adds a 
    default 'frequencyRating' of 3 to any question missing it.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Dynamically find all chapter directories (g7_chapters, g10_chapters, etc.)
    subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.endswith("_chapters")]

    for subdir in subdirs:
        subdir_path = os.path.join(base_dir, subdir)
        json_files = [f for f in os.listdir(subdir_path) if f.endswith(".json")]

        for filename in json_files:
            file_path = os.path.join(subdir_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            updated = False
            if "questions" in data:
                for q in data["questions"]:
                    if "frequencyRating" not in q:
                        q["frequencyRating"] = 3  # Default rating for conceptual integrity
                        updated = True
            
            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                print(f"Updated {subdir}/{filename}")

if __name__ == "__main__":
    fix_ratings()