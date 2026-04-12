import os
import re

def audit_g10_chapters():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chapters_dir = os.path.join(base_dir, "g10_chapters")
    readme_path = os.path.join(base_dir, "README.md")

    # Mapping subjects to their filename prefixes
    subject_map = {
        "Mathematics": "math",
        "Science": "sci",
        "History": "hist",
        "Geography": "geo",
        "Civics": "civ",
        "Economics": "eco",
        "English": "eng",
        "English_Supplementary": "eng_supp"
    }

    # Expected counts based on NCERT Rationalised Syllabus in README
    # Note: English count increased to reflect full Prose + Footprints without Feet
    expected_structure = {
        "Mathematics": 14,
        "Science": 13,
        "History": 5,
        "Geography": 7,
        "Civics": 5,
        "Economics": 5,
        "English": 9,
        "English_Supplementary": 9
    }

    if not os.path.exists(chapters_dir):
        print(f"Error: Directory {chapters_dir} not found.")
        return

    actual_files = os.listdir(chapters_dir)
    print("--- Grade 10 Content Audit ---")
    
    total_missing = 0
    total_found = 0

    for subject, count in expected_structure.items():
        prefix = subject_map[subject]
        found_in_subject = 0
        missing_indices = []

        for i in range(1, count + 1):
            # Look for versioned filename pattern: g10_{prefix}_ch{i}_v1.json
            expected_name = f"g10_{prefix}_ch{i}_v1.json"
            if expected_name in actual_files:
                found_in_subject += 1
                total_found += 1
            else:
                missing_indices.append(str(i))
                total_missing += 1
        
        status = "✅ COMPLETE" if not missing_indices else f"❌ MISSING CH: {', '.join(missing_indices)}"
        print(f"{subject:12} : {found_in_subject}/{count} files found. {status}")

    print("-" * 30)
    print(f"Total Found   : {total_found}")
    print(f"Total Missing : {total_missing}")
    print(f"Total Expected: {sum(expected_structure.values())}")

if __name__ == "__main__":
    audit_g10_chapters()