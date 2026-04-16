# CBSE Grade 7, 10 & 12 Quiz App Content

This directory contains structured JSON data for Grade 7, Grade 10, and Grade 12 MCQ Quiz Apps, strictly aligned with the **NCERT Rationalised Syllabus (2023-24 onwards)** and historical exam frequency patterns.

## File Structure

- `version.json`: The manifest file tracking the latest versions of all available chapters.
- `g7_chapters/`: Grade 7 chapter files (10 MCQs each).
- `g10_chapters/`: Grade 10 chapter files (40 MCQs each).
- `g12_chapters/`: Grade 12 chapter files (40 MCQs each).

## Data Schema

Each chapter JSON file follows a strict schema to ensure compatibility with the quiz engine:

| Key | Type | Description |
| :--- | :--- | :--- |
| `id` | String | Unique identifier (e.g., `g7_math_ch1`) |
| `grade` | String | "7", "10", "11" or "12" |
| `subject` | String | e.g., "Mathematics", "Science", "History", etc. |
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
> "Act as a CBSE Curriculum Expert and Data Engineer. Generate JSON data for Grade {GRADE} {SUBJECT} Chapter {NUMBER}: {TITLE}.
> 
> 1. **Schema Requirements**: Use keys `id`, `grade`, `subject`, `number`, `title`, `version`, and `questions` (array).
> 2. **Question Object**: Include `id` (format: g{GRADE}_{SUBJ_INITIAL}{NUMBER}_q{INDEX}), `text`, `options` (array of exactly 4), `correctIndex` (0-3), `explanation`, and `frequencyRating` (1-5).
> 3. **Quantity**: Generate exactly {COUNT} questions (10 for Grade 7, 40 for Grade 10).
> 4. **Content**: Ensure alignment with NCERT Rationalised Syllabus (2023-24). Provide a mix of easy, conceptual, and high-frequency exam questions with accurate explanations.
> 5. **Output**: Return only the raw valid JSON code block."

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

## Class 10 Syllabus Coverage (NCERT Rationalised)

### Mathematics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Real Numbers | ✅ v1 |
| 2 | Polynomials | ✅ v1 |
| 3 | Pair of Linear Equations in Two Variables | ✅ v1 |
| 4 | Quadratic Equations | ✅ v1 |
| 5 | Arithmetic Progressions | ✅ v1 |
| 6 | Triangles | ✅ v1 |
| 7 | Coordinate Geometry | ✅ v1 |
| 8 | Introduction to Trigonometry | ✅ v1 |
| 9 | Some Applications of Trigonometry | ✅ v1 |
| 10 | Circles | ✅ v1 |
| 11 | Areas Related to Circles | ✅ v1 |
| 12 | Surface Areas and Volumes | ✅ v1 |
| 13 | Statistics | ✅ v1 |
| 14 | Probability | ✅ v1 |

### Science (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Chemical Reactions and Equations | ✅ v1 |
| 2 | Acids, Bases and Salts | ✅ v1 |
| 3 | Metals and Non-metals | ✅ v1 |
| 4 | Carbon and its Compounds | ✅ v1 |
| 5 | Life Processes | ✅ v1 |
| 6 | Control and Coordination | ✅ v1 |
| 7 | How do Organisms Reproduce? | ✅ v1 |
| 8 | Heredity | ✅ v1 |
| 9 | Light – Reflection and Refraction | ✅ v1 |
| 10 | The Human Eye and the Colourful World | ✅ v1 |
| 11 | Electricity | ✅ v1 |
| 12 | Magnetic Effects of Electric Current | ✅ v1 |
| 13 | Our Environment | ✅ v1 |

### Social Science - History (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Rise of Nationalism in Europe | ✅ v1 |
| 2 | Nationalism in India | ✅ v1 |
| 3 | The Making of a Global World | ✅ v1 |
| 4 | The Age of Industrialisation | ✅ v1 |
| 5 | Print Culture and the Modern World | ✅ v1 |

### Mathematics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Real Numbers | ✅ v1 |
| 2 | Polynomials | ✅ v1 |
| 3 | Pair of Linear Equations in Two Variables | ✅ v1 |
| 4 | Quadratic Equations | ✅ v1 |
| 5 | Arithmetic Progressions | ✅ v1 |
| 6 | Triangles | ✅ v1 |
| 7 | Coordinate Geometry | ✅ v1 |
| 8 | Introduction to Trigonometry | ✅ v1 |
| 9 | Some Applications of Trigonometry | ✅ v1 |
| 10 | Circles | ✅ v1 |
| 11 | Areas Related to Circles | ✅ v1 |
| 12 | Surface Areas and Volumes | ✅ v1 |
| 13 | Statistics | ✅ v1 |
| 14 | Probability | ✅ v1 |

### Science (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Chemical Reactions and Equations | ✅ v1 |
| 2 | Acids, Bases and Salts | ✅ v1 |
| 3 | Metals and Non-metals | ✅ v1 |
| 4 | Carbon and its Compounds | ✅ v1 |
| 5 | Life Processes | ✅ v1 |
| 6 | Control and Coordination | ✅ v1 |
| 7 | How do Organisms Reproduce? | ✅ v1 |
| 8 | Heredity | ✅ v1 |
| 9 | Light – Reflection and Refraction | ✅ v1 |
| 10 | The Human Eye and the Colourful World | ✅ v1 |
| 11 | Electricity | ✅ v1 |
| 12 | Magnetic Effects of Electric Current | ✅ v1 |
| 13 | Our Environment | ✅ v1 |

### Social Science - History (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Rise of Nationalism in Europe | ✅ v1 |
| 2 | Nationalism in India | ✅ v1 |
| 3 | The Making of a Global World | ✅ v1 |
| 4 | The Age of Industrialisation | ✅ v1 |
| 5 | Print Culture and the Modern World | ✅ v1 |

### Social Science - Geography (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Resources and Development | ✅ v1 |
| 2 | Forest and Wildlife Resources | ✅ v1 |
| 3 | Water Resources | ✅ v1 |
| 4 | Agriculture | ✅ v1 |
| 5 | Minerals and Energy Resources | ✅ v1 |
| 6 | Manufacturing Industries | ✅ v1 |
| 7 | Lifelines of National Economy | ✅ v1 |

### Social Science - Civics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Power Sharing | ✅ v1 |
| 2 | Federalism | ✅ v1 |
| 3 | Gender, Religion and Caste | ✅ v1 |
| 4 | Political Parties | ✅ v1 |
| 5 | Outcomes of Democracy | ✅ v1 |

### Social Science - Economics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Development | ✅ v1 |
| 2 | Sectors of the Indian Economy | ✅ v1 |
| 3 | Money and Credit | ✅ v1 |
| 4 | Globalisation and the Indian Economy | ✅ v1 |
| 5 | Consumer Rights | ✅ v1 |

### English - First Flight (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | A Letter to God | ✅ v1 |
| 2 | Nelson Mandela: Long Walk to Freedom | ✅ v1 |
| 3 | Two Stories about Flying | ✅ v1 |
| 4 | From the Diary of Anne Frank | ✅ v1 |
| 5 | Glimpses of India | ✅ v1 |
| 6 | Mijbil the Otter | ✅ v1 |
| 7 | Madam Rides the Bus | ✅ v1 |
| 8 | The Sermon at Benares | ✅ v1 |
| 9 | The Proposal | ✅ v1 |

## Class 11 Syllabus Coverage (NCERT Rationalised)

### Mathematics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Sets | ⏳ Pending |
| 2 | Relations and Functions | ⏳ Pending |
| 3 | Trigonometric Functions | ⏳ Pending |
| 4 | Principle of Mathematical Induction | ⏳ Pending |
| 5 | Complex Numbers and Quadratic Equations | ⏳ Pending |
| 6 | Linear Inequalities | ⏳ Pending |
| 7 | Permutations and Combinations | ⏳ Pending |
| 8 | Binomial Theorem | ⏳ Pending |
| 9 | Sequences and Series | ⏳ Pending |
| 10 | Straight Lines | ⏳ Pending |
| 11 | Conic Sections | ⏳ Pending |
| 12 | Introduction to Three Dimensional Geometry | ⏳ Pending |
| 13 | Limits and Derivatives | ⏳ Pending |
| 14 | Statistics | ⏳ Pending |
| 15 | Probability | ⏳ Pending |

### Physics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Physical World | ⏳ Pending |
| 2 | Units and Measurements | ⏳ Pending |
| 3 | Motion in a Straight Line | ⏳ Pending |
| 4 | Motion in a Plane | ⏳ Pending |
| 5 | Laws of Motion | ⏳ Pending |
| 6 | Work, Energy and Power | ⏳ Pending |
| 7 | System of Particles and Rotational Motion | ⏳ Pending |
| 8 | Gravitation | ⏳ Pending |
| 9 | Mechanical Properties of Solids | ⏳ Pending |
| 10 | Mechanical Properties of Fluids | ⏳ Pending |
| 11 | Thermal Properties of Matter | ⏳ Pending |
| 12 | Thermodynamics | ⏳ Pending |
| 13 | Kinetic Theory | ⏳ Pending |
| 14 | Oscillations | ⏳ Pending |
| 15 | Waves | ⏳ Pending |

### English (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Portrait of a Lady | ⏳ Pending |

## Class 12 Syllabus Coverage (NCERT Rationalised)

### Mathematics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Relations and Functions | ✅ v1 |
| 2 | Inverse Trigonometric Functions | ✅ v1 |
| 3 | Matrices | ⏳ Pending |
| 4 | Determinants | ⏳ Pending |
| 5 | Continuity and Differentiability | ⏳ Pending |
| 6 | Application of Derivatives | ⏳ Pending |
| 7 | Integrals | ⏳ Pending |
| 8 | Application of Integrals | ⏳ Pending |
| 9 | Differential Equations | ⏳ Pending |
| 10 | Vector Algebra | ⏳ Pending |
| 11 | Three Dimensional Geometry | ⏳ Pending |
| 12 | Linear Programming | ⏳ Pending |
| 13 | Probability | ⏳ Pending |

### Physics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Electric Charges and Fields | ✅ v1 |
| 2 | Electrostatic Potential and Capacitance | ⏳ Pending |
| 3 | Current Electricity | ⏳ Pending |
| 4 | Moving Charges and Magnetism | ⏳ Pending |
| 5 | Magnetism and Matter | ⏳ Pending |
| 6 | Electromagnetic Induction | ⏳ Pending |
| 7 | Alternating Current | ⏳ Pending |
| 8 | Electromagnetic Waves | ⏳ Pending |
| 9 | Ray Optics and Optical Instruments | ⏳ Pending |
| 10 | Wave Optics | ⏳ Pending |
| 11 | Dual Nature of Radiation and Matter | ⏳ Pending |
| 12 | Atoms | ⏳ Pending |
| 13 | Nuclei | ⏳ Pending |
| 14 | Semiconductor Electronics | ⏳ Pending |

### English - Flamingo (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Last Lesson | ✅ v1 |
| 2 | Lost Spring | ⏳ Pending |
| 3 | Deep Water | ⏳ Pending |
| 4 | The Rattrap | ⏳ Pending |
| 5 | Indigo | ⏳ Pending |

## Deployment & Android Integration Strategy

To minimize requests to the GitHub backend:

1. **Client-Side Caching**: Apps should fetch `version.json` first. To bypass CDN caching for the manifest, append a timestamp:
   `https://cdn.jsdelivr.net/gh/{user}/{repo}@main/version.json?t=${Date.now()}`
2. **Version Comparison**: Compare the `versions` object in the manifest with the local cache.
3. **Conditional Fetching**: Only download `g7_{subject}_ch{number}_v{version}.json` if the version has incremented.
4. **Full Grade Bundle (ZIP)**: Use the filename provided in the `bundles` section of the manifest (e.g., `g7_a1b2c3d4.zip`).
   - **Extraction**: The app should extract the ZIP to `context.getFilesDir() + "/content/g7/"`.
   - **Path Mapping**: The app logic should map the `id` from `version.json` to the local file path (e.g., `id: g7_math_ch1` maps to `.../g7/g7_chapters/g7_math_ch1_v1.json` after extraction).
5. **Minification**: Ensure JSON files are minified (whitespaces removed) before deployment to save bandwidth.
6. **CDN Usage**: Use a CDN that proxies GitHub content (like jsDelivr) to bypass GitHub's raw file rate limits and improve global load times.
   - Format: `https://cdn.jsdelivr.net/gh/{user}/{repo}@{branch}/{path}`

## Compression Performance
Current JSON files are uncompressed. When served via GitHub Pages or jsDelivr, **Brotli** or **Gzip** compression is automatically applied by the server, typically reducing the transfer size by 70-80%.