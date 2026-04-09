# CBSE Grade 7 Quiz App Content

This directory contains structured JSON data for a Grade 7 MCQ Quiz App, strictly aligned with the **NCERT Rationalised Syllabus (2023-24 onwards)** and historical exam frequency patterns.

## File Structure

- `version.json`: The manifest file tracking the latest versions of all available chapters.
- `g7_chapters/g7_{subject}_ch{number}_v{version}.json`: Individual chapter files containing 10 MCQs each, located in a grade-specific subdirectory.

## Data Schema

Each chapter JSON file follows a strict schema to ensure compatibility with the quiz engine:

| Key | Type | Description |
| :--- | :--- | :--- |
| `id` | String | Unique identifier (e.g., `g7_math_ch1`) |
| `grade` | String | Always "7" |
| `subject` | String | "Mathematics" or "Science" |
| `number` | String | Chapter number as per NCERT |
| `title` | String | Official chapter name |
| `version` | String | Version string (e.g., "v1") |
| `questions` | Array | List of 10 question objects |

### Question Object
Each question includes:
- `id`: Unique string (e.g., `g7_m1_q1`).
- `text`: The MCQ question text.
- `options`: Array of exactly 4 strings.
- `correctIndex`: Integer (0-3) indicating the correct answer.
- `explanation`: 1-2 sentence explanation.
- `frequencyRating`: Integer (1-5) indicating how often this concept appears in exams.

## How to Use the Generation Prompt

To generate additional chapters or update existing ones, use the following prompt structure with a coding assistant:

### Instruction Template
> "Act as a CBSE Curriculum Expert and Data Engineer. Generate JSON data for Grade 7 [Subject] Chapter [Number]: [Chapter Title]. 
> 
> 1. Follow the schema used in existing files (e.g., g7_math_ch1).
> 2. Ensure exactly 10 questions ranging from Easy to Conceptual.
> 3. Provide accurate explanations for each answer.
> 4. Use the ID format: g7_[m/s][chapter_number]_q[question_number]."

## Content Maintenance & Bundling

To maintain data integrity and optimize delivery to the Android app, use the provided utility scripts.

### 1. Schema Validation & Rating Fix
If new chapters are generated without frequency ratings, run:
```bash
python fix_frequency_ratings.py
```

### 2. Creating the Production Bundle
After adding or modifying files in `g7_chapters/`, generate the ZIP bundle:
```bash
python create_bundle.py
```
This script automatically packages all chapters into `g7_v1.zip`, calculates its MD5 checksum, and updates the `updatedAt` and `bundles` metadata in `version.json`.

## Syllabus Coverage (NCERT Rationalised)

### Mathematics
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Integers | ✅ v1 |
| 2 | Fractions and Decimals | ✅ v1 |
| 3 | Data Handling | ✅ v1 |
| 4 | Simple Equations | ✅ v1 |
| 5 | Lines and Angles | ✅ v1 |
| 6 | The Triangle and its Properties | ✅ v1 |
| 7 | Comparing Quantities | ✅ v1 |
| 8 | Rational Numbers | ✅ v1 |
| 9 | Perimeter and Area | ✅ v1 |
| 10 | Algebraic Expressions | ✅ v1 |
| 11 | Exponents and Powers | ✅ v1 |
| 12 | Symmetry | ✅ v1 |
| 13 | Visualising Solid Shapes | ✅ v1 |

### Science
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Nutrition in Plants | ✅ v1 |
| 2 | Nutrition in Animals | ✅ v1 |
| 3 | Heat | ✅ v1 |
| 4 | Acids, Bases and Salts | ✅ v1 |
| 5 | Physical and Chemical Changes | ✅ v1 |
| 6 | Respiration in Organisms | ✅ v1 |
| 7 | Transportation in Animals and Plants | ✅ v1 |
| 8 | Reproduction in Plants | ✅ v1 |
| 9 | Motion and Time | ✅ v1 |
| 10 | Electric Current and its Effects | ✅ v1 |
| 11 | Light | ✅ v1 |
| 12 | Forests: Our Lifeline | ✅ v1 |
| 13 | Wastewater Story | ✅ v1 |

### Social Science
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| Hist 1 | Tracing Changes Through a Thousand Years | ✅ v1 |
| Hist 2 | New Kings and Kingdoms | ✅ v1 |
| Hist 3 | Delhi: 12th to 15th Century | ✅ v1 |
| Hist 4 | The Mughals (16th to 17th Century) | ✅ v1 |
| Hist 5 | Tribes, Nomads and Settled Communities | ✅ v1 |
| Hist 6 | Devotional Paths to the Divine | ✅ v1 |
| Hist 7 | The Making of Regional Cultures | ✅ v1 |
| Hist 8 | Eighteenth-Century Political Formations | ✅ v1 |
| Geo 1 | Environment | ✅ v1 |
| Geo 2 | Inside Our Earth | ✅ v1 |
| Geo 3 | Our Changing Earth | ✅ v1 |
| Geo 4 | Air | ✅ v1 |
| Geo 5 | Water | ✅ v1 |
| Geo 6 | Human Environment Interactions | ✅ v1 |
| Geo 7 | Life in the Deserts | ✅ v1 |
| Civ 1 | On Equality | ✅ v1 |
| Civ 2 | Role of the Government in Health | ✅ v1 |
| Civ 3 | How the State Government Works | ✅ v1 |
| Civ 4 | Growing up as Boys and Girls | ✅ v1 |
| Civ 5 | Women Change the World | ✅ v1 |
| Civ 6 | Understanding Media | ✅ v1 |
| Civ 7 | Markets Around Us | ✅ v1 |
| Civ 8 | A Shirt in the Market | ✅ v1 |

### English (Honeycomb)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Three Questions | ✅ v1 |
| 2 | A Gift of Chappals | ✅ v1 |
| 3 | Gopal and the Hilsa Fish | ✅ v1 |
| 4 | The Ashes That Made Trees Bloom | ✅ v1 |
| 5 | Quality | ✅ v1 |
| 6 | Expert Detectives | ✅ v1 |
| 7 | The Invention of Vita-Wonk | ✅ v1 |
| 8 | A Homage to our Brave Soldiers | ✅ v1 |

## Deployment & Android Integration Strategy

To minimize requests to the GitHub backend:

1. **Client-Side Caching**: Apps should fetch `version.json` first.
2. **Version Comparison**: Compare the `versions` object in the manifest with the local cache.
3. **Conditional Fetching**: Only download `g7_{subject}_ch{number}_v{version}.json` if the version has incremented.
4. **Full Grade Bundle (ZIP)**: For the best onboarding experience, use `g7_v1.zip`. 
   - **Extraction**: The app should extract the ZIP to `context.getFilesDir() + "/content/g7/"`.
   - **Path Mapping**: The app logic should map the `id` from `version.json` to the local file path (e.g., `id: g7_math_ch1` maps to `.../g7/g7_chapters/g7_math_ch1_v1.json` after extraction).
5. **Minification**: Ensure JSON files are minified (whitespaces removed) before deployment to save bandwidth.
6. **CDN Usage**: Use a CDN that proxies GitHub content (like jsDelivr) to bypass GitHub's raw file rate limits and improve global load times.
   - Format: `https://cdn.jsdelivr.net/gh/{user}/{repo}@{branch}/{path}`

## Compression Performance
Current JSON files are uncompressed. When served via GitHub Pages or jsDelivr, **Brotli** or **Gzip** compression is automatically applied by the server, typically reducing the transfer size by 70-80%.