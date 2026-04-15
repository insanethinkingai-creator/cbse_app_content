import os
import re
import json

def audit_grade(grade_num, expected_structure):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chapters_dir = os.path.join(base_dir, f"g{grade_num}_chapters")

    # Mapping subjects to their filename prefixes
    subject_map = {
        "Mathematics": "math",
        "Science": "sci",
        "Physics": "phy",
        "Chemistry": "chem",
        "Biology": "bio",
        "History": "hist",
        "Geography": "geo",
        "Civics": "civ",
        "Economics": "eco",
        "English": "eng"
    }

    if not os.path.exists(chapters_dir):
        print(f"\nSkipping Grade {grade_num}: Directory {chapters_dir} not found.")
        return

    actual_files = os.listdir(chapters_dir)
    print(f"\n--- Grade {grade_num} Content Audit ---")
    
    total_missing = 0
    total_incomplete = 0
    total_found = 0
    
    expected_q_count = 10 if grade_num == 7 else 40

    for subject, count in expected_structure.items():
        prefix = subject_map.get(subject, subject.lower()[:3])
        found_in_subject = 0
        missing_indices = []

        for i in range(1, count + 1):
            # Look for versioned filename pattern: gX_{prefix}_ch{i}_v1.json
            expected_name = f"g{grade_num}_{prefix}_ch{i}_v1.json"
            if expected_name in actual_files:
                found_in_subject += 1
                file_path = os.path.join(chapters_dir, expected_name)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    q_count = len(data.get("questions", []))
                    
                if q_count < expected_q_count:
                    missing_indices.append(f"Ch{i} ({q_count}/{expected_q_count}Q)")
                    total_incomplete += 1
                else:
                    total_found += 1
            else:
                missing_indices.append(str(i))
                total_missing += 1
        
        status = "✅ COMPLETE" if not missing_indices else f"❌ MISSING CH: {', '.join(missing_indices)}"
        print(f"{subject:12} : {found_in_subject}/{count} files found. {status}")

    print("-" * 30)
    print(f"Total Complete: {total_found}")
    print(f"Total Incomplete: {total_incomplete}")
    print(f"Total Missing : {total_missing}")
    print(f"Total Expected: {sum(expected_structure.values())}")

if __name__ == "__main__":
    # Grade 10 Configuration
    g10_structure = {
        "Mathematics": 14,
        "Science": 13,
        "History": 5,
        "Geography": 7,
        "Civics": 5,
        "Economics": 5,
        "English": 9
    }
    audit_grade(10, g10_structure)

    # Grade 11 Configuration
    g11_structure = {
        "Mathematics": 14,
        "Physics": 14,
        "Chemistry": 9,
        "Biology": 19,
        "English": 8
    }
    audit_grade(11, g11_structure)

    # Grade 12 Configuration
    g12_structure = {
        "Mathematics": 13,
        "Physics": 14,
        "Chemistry": 10,
        "Biology": 13,
        "English": 5
    }
    audit_grade(12, g12_structure)