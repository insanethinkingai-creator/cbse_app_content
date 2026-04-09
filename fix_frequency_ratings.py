import os
import json

def fix_ratings():
    """
    Iterates through all Grade 7 chapter JSON files and adds a 
    default 'frequencyRating' of 3 to any question missing it.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chapters_subdir = os.path.join(base_dir, "g7_chapters") # New subdirectory for chapter files

    if not os.path.exists(chapters_subdir):
        print(f"Error: Chapter subdirectory '{chapters_subdir}' not found. Skipping rating fix.")
        return
    json_files = [f for f in os.listdir(chapters_subdir) if f.endswith(".json")]

    for filename in json_files:
        file_path = os.path.join(chapters_subdir, filename)
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
            print(f"Updated {filename}")

if __name__ == "__main__":
    fix_ratings()