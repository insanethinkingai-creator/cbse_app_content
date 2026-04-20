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
    
    total_missing_files = 0
    total_incomplete = 0
    total_complete_chapters = 0
    
    expected_q_count = 40

    for subject, count in expected_structure.items():
        prefix = subject_map.get(subject, subject.lower()[:3])
        found_in_subject = 0
        missing_files = []
        incomplete_chapters = []

        for i in range(1, count + 1):
            # Look for versioned filename pattern: gX_{prefix}_ch{i}_v1.json
            expected_name = f"g{grade_num}_{prefix}_ch{i}_v1.json"
            if expected_name in actual_files:
                found_in_subject += 1
                file_path = os.path.join(chapters_dir, expected_name)
                #print(f"  Checking: {expected_name}", flush=True)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    current_q_count = len(data.get("questions", []))
                    
                    if current_q_count < expected_q_count:
                        incomplete_chapters.append(f"Ch{i} ({current_q_count}/{expected_q_count}Q)")
                        total_incomplete += 1
                    else:
                        total_complete_chapters += 1
                except json.JSONDecodeError as e:
                    print(f"  ❌ ERROR: Malformed JSON in {expected_name}: {e}")
                    total_incomplete += 1
                    continue
            else:
                missing_files.append(str(i))
                total_missing_files += 1
        
        if not missing_files and not incomplete_chapters:
            status = "✅ COMPLETE"
        elif missing_files:
            status = f"❌ MISSING FILES: {', '.join(missing_files)}"
            if incomplete_chapters:
                status += f" | ⚠️ INCOMPLETE: {', '.join(incomplete_chapters)}"
        else:
            status = f"⚠️ INCOMPLETE: {', '.join(incomplete_chapters)}"
        
        print(f"{subject:12} : {found_in_subject}/{count} files found. {status}")

    print("-" * 30)
    print(f"Total Complete Chapters: {total_complete_chapters}")
    print(f"Total Incomplete (<40Q): {total_incomplete}")
    print(f"Total Missing Files: {total_missing_files}")
    total_chapters_checked = total_complete_chapters + total_incomplete + total_missing_files
    print(f"Total Chapters Checked: {total_chapters_checked}")
    print(f"Total Expected: {sum(expected_structure.values())}")

if __name__ == "__main__":
    # Grade 7 Configuration
    g7_structure = {
        "Mathematics": 13,
        "Science": 13,
        "History": 8,
        "Geography": 7,
        "Civics": 8,
        "English": 8
    }
    audit_grade(7, g7_structure)

    # Grade 8 Configuration
    g8_structure = {
        "Mathematics": 13,
        "Science": 13,
        "History": 8,
        "Geography": 6,
        "Civics": 8,
        "English": 8
    }
    audit_grade(8, g8_structure)

    # Grade 9 Configuration
    g9_structure = {
        "Mathematics": 15,
        "Science": 12,
        "English": 11
    }
    audit_grade(9, g9_structure)

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