# CBSE Grade 7-12 Quiz App Content

This directory contains structured JSON data for Grade 7 to Grade 12 MCQ Quiz Apps, strictly aligned with the **NCERT Rationalised Syllabus (2023-24 onwards)** and historical exam frequency patterns.

## File Structure

- `version.json`: The manifest file tracking the latest versions of all available chapters.
- `g7_chapters/`: Grade 7 chapter files (40 MCQs each).
- `g8_chapters/`: Grade 8 chapter files (40 MCQs each).
- `g9_chapters/`: Grade 9 chapter files (40 MCQs each).
- `g10_chapters/`: Grade 10 chapter files (40 MCQs each).
- `g11_chapters/`: Grade 11 chapter files (40 MCQs each).
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
| `questions` | Array | List of 40 question objects |

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
> 5. **Output**: Return only the raw valid JSON code block. Set {COUNT} to 40 for all grades."

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

### Mathematics (40 Questions per Chapter)
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

### Science (40 Questions per Chapter)
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

### Social Science (40 Questions per Chapter)
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

### English (Honeycomb) (40 Questions per Chapter)
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

## Class 8 Syllabus Coverage (NCERT Rationalised)

### Mathematics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Rational Numbers | ✅ v1 |
| 2 | Linear Equations in One Variable | ✅ v1 |
| 3 | Understanding Quadrilaterals | ✅ v1 |
| 4 | Data Handling | ✅ v1 |
| 5 | Squares and Square Roots | ✅ v1 |
| 6 | Cubes and Cube Roots | ✅ v1 |
| 7 | Comparing Quantities | ✅ v1 |
| 8 | Algebraic Expressions and Identities | ✅ v1 |
| 9 | Mensuration | ✅ v1 |
| 10 | Exponents and Powers | ✅ v1 |
| 11 | Direct and Inverse Proportions | ✅ v1 |
| 12 | Factorisation | ✅ v1 |
| 13 | Introduction to Graphs | ✅ v1 |

### Science (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Crop Production and Management | ✅ v1 |
| 2 | Microorganisms: Friend and Foe | ✅ v1 |
| 3 | Coal and Petroleum | ✅ v1 |
| 4 | Combustion and Flame | ✅ v1 |
| 5 | Conservation of Plants and Animals | ✅ v1 |
| 6 | Reproduction in Animals | ✅ v1 |
| 7 | Reaching the Age of Adolescence | ✅ v1 |
| 8 | Force and Pressure | ✅ v1 |
| 9 | Friction | ✅ v1 |
| 10 | Sound | ✅ v1 |
| 11 | Chemical Effects of Electric Current | ✅ v1 |
| 12 | Some Natural Phenomena | ✅ v1 |
| 13 | Light | ✅ v1 |

### Social Science (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| Hist 1 | How, When and Where | ✅ v1 |
| Hist 2 | From Trade to Territory | ✅ v1 |
| Hist 3 | Ruling the Countryside | ✅ v1 |
| Hist 4 | Tribals, Dikus and the Vision of a Golden Age | ✅ v1 |
| Hist 5 | When People Rebel | ✅ v1 |
| Hist 6 | Civilising the "Native", Educating the Nation | ✅ v1 |
| Hist 7 | Women, Caste and Reform | ✅ v1 |
| Hist 8 | The Making of the National Movement | ✅ v1 |
| Geo 1 | Resources | ✅ v1 |
| Geo 2 | Land, Soil, Water, Natural Vegetation | ✅ v1 |
| Geo 3 | Mineral and Power Resources | ✅ v1 |
| Geo 4 | Agriculture | ✅ v1 |
| Geo 5 | Industries | ✅ v1 |
| Geo 6 | Human Resources | ✅ v1 |
| Civ 1 | The Indian Constitution | ✅ v1 |
| Civ 2 | Understanding Secularism | ✅ v1 |
| Civ 3 | Parliament and the Making of Laws | ✅ v1 |
| Civ 4 | The Judiciary | ✅ v1 |
| Civ 5 | Understanding Marginalisation | ✅ v1 |
| Civ 6 | Confronting Marginalisation | ✅ v1 |
| Civ 7 | Public Facilities | ✅ v1 |
| Civ 8 | Law and Social Justice | ✅ v1 |

### English (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Best Christmas Present in the World | ✅ v1 |
| 2 | The Tsunami | ✅ v1 |
| 3 | Glimpses of the Past | ✅ v1 |
| 4 | Bepin Choudhury’s Lapse of Memory | ✅ v1 |
| 5 | The Summit Within | ✅ v1 |
| 6 | This is Jody’s Fawn | ✅ v1 |
| 7 | A Visit to Cambridge | ✅ v1 |
| 8 | A Short Monsoon Diary | ✅ v1 |

## Class 9 Syllabus Coverage (NCERT Rationalised)

### Mathematics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Number Systems | ✅ v1 |
| 2 | Polynomials | ✅ v1 |
| 3 | Coordinate Geometry | ✅ v1 |
| 4 | Linear Equations in Two Variables | ✅ v1 |
| 5 | Introduction to Euclid’s Geometry | ✅ v1 |
| 6 | Lines and Angles | ✅ v1 |
| 7 | Triangles | ✅ v1 |
| 8 | Quadrilaterals | ✅ v1 |
| 9 | Areas of Parallelograms and Triangles | ✅ v1 |
| 10 | Circles | ✅ v1 |
| 11 | Constructions | ✅ v1 |
| 12 | Heron’s Formula | ✅ v1 |
| 13 | Surface Areas and Volumes | ✅ v1 |
| 14 | Statistics | ✅ v1 |
| 15 | Probability | ✅ v1 |

### Science (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Matter in Our Surroundings | ✅ v1 |
| 2 | Is Matter Around Us Pure | ✅ v1 |
| 3 | Atoms and Molecules | ✅ v1 |
| 4 | Structure of the Atom | ✅ v1 |
| 5 | The Fundamental Unit of Life | ✅ v1 |
| 6 | Tissues | ✅ v1 |
| 7 | Motion | ✅ v1 |
| 8 | Force and Laws of Motion | ✅ v1 |
| 9 | Gravitation | ✅ v1 |
| 10 | Work and Energy | ✅ v1 |
| 11 | Sound | ✅ v1 |
| 12 | Improvement in Food Resources | ✅ v1 |

### English (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Fun They Had | ✅ v1 |
| 2 | The Sound of Music | ✅ v1 |
| 3 | The Little Girl | ✅ v1 |
| 4 | A Truly Beautiful Mind | ✅ v1 |
| 5 | The Snake and the Mirror | ✅ v1 |
| 6 | My Childhood | ✅ v1 |
| 7 | Reach for the Top | ✅ v1 |
| 8 | Kathmandu | ✅ v1 |
| 9 | If I Were You | ✅ v1 |
| 10 | In the Kingdom of Fools | ✅ v1 |
| 11 | The Happy Prince | ✅ v1 |

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
| 1 | Sets | ✅ v1 |
| 2 | Relations and Functions | ✅ v1 |
| 3 | Trigonometric Functions | ✅ v1 |
| 4 | Complex Numbers and Quadratic Equations | ✅ v1 |
| 5 | Linear Inequalities | ✅ v1 |
| 6 | Permutations and Combinations | ✅ v1 |
| 7 | Binomial Theorem | ✅ v1 |
| 8 | Sequences and Series | ✅ v1 |
| 9 | Straight Lines | ✅ v1 |
| 10 | Conic Sections | ✅ v1 |
| 11 | Introduction to Three Dimensional Geometry | ✅ v1 |
| 12 | Limits and Derivatives | ✅ v1 |
| 13 | Statistics | ✅ v1 |
| 14 | Probability | ✅ v1 |

### Physics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Physical World | ✅ v1 |
| 2 | Units and Measurements | ✅ v1 |
| 3 | Motion in a Straight Line | ✅ v1 |
| 4 | Motion in a Plane | ✅ v1 |
| 5 | Laws of Motion | ✅ v1 |
| 6 | Work, Energy and Power | ✅ v1 |
| 7 | System of Particles and Rotational Motion | ✅ v1 |
| 8 | Gravitation | ✅ v1 |
| 9 | Mechanical Properties of Solids | ✅ v1 |
| 10 | Mechanical Properties of Fluids | ✅ v1 |
| 11 | Thermal Properties of Matter | ✅ v1 |
| 12 | Thermodynamics | ✅ v1 |
| 13 | Kinetic Theory | ✅ v1 |
| 14 | Oscillations | ✅ v1 |
| 15 | Waves | ✅ v1 |

### Chemistry (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Some Basic Concepts of Chemistry | ✅ v1 |
| 2 | Structure of Atom | ✅ v1 |
| 3 | Classification of Elements and Periodicity | ✅ v1 |
| 4 | Chemical Bonding and Molecular Structure | ✅ v1 |
| 5 | Thermodynamics | ✅ v1 |
| 6 | Equilibrium | ✅ v1 |
| 7 | Redox Reactions | ✅ v1 |
| 8 | Organic Chemistry – Basic Principles | ✅ v1 |
| 9 | Hydrocarbons | ✅ v1 |

### Biology (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Living World | ✅ v1 |
| 2 | Biological Classification | ✅ v1 |
| 3 | Plant Kingdom | ✅ v1 |
| 4 | Animal Kingdom | ✅ v1 |
| 5 | Morphology of Flowering Plants | ✅ v1 |
| 6 | Anatomy of Flowering Plants | ✅ v1 |
| 7 | Structural Organisation in Animals | ✅ v1 |
| 8 | Cell: The Unit of Life | ✅ v1 |
| 9 | Biomolecules | ✅ v1 |
| 10 | Cell Cycle and Cell Division | ✅ v1 |
| 11 | Photosynthesis in Higher Plants | ✅ v1 |
| 12 | Respiration in Plants | ✅ v1 |
| 13 | Plant Growth and Development | ✅ v1 |
| 14 | Breathing and Exchange of Gases | ✅ v1 |
| 15 | Body Fluids and Circulation | ✅ v1 |
| 16 | Excretory Products and their Elimination | ✅ v1 |
| 17 | Locomotion and Movement | ✅ v1 |
| 18 | Neural Control and Coordination | ✅ v1 |
| 19 | Chemical Coordination and Integration | ✅ v1 |

### English (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Portrait of a Lady | ✅ v1 |
| 2 | "We’re Not Afraid to Die..." | ✅ v1 |
| 3 | Discovering Tut: the Saga Continues | ✅ v1 |
| 4 | Landscape of the Soul | ✅ v1 |
| 5 | The Ailing Planet | ✅ v1 |
| 6 | The Browning Version | ✅ v1 |
| 7 | The Adventure | ✅ v1 |
| 8 | Silk Road | ✅ v1 |

## Class 12 Syllabus Coverage (NCERT Rationalised)

### Mathematics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Relations and Functions | ✅ v1 |
| 2 | Inverse Trigonometric Functions | ✅ v1 |
| 3 | Matrices | ✅ v1 |
| 4 | Determinants | ✅ v1 |
| 5 | Continuity and Differentiability | ✅ v1 |
| 6 | Application of Derivatives | ✅ v1 |
| 7 | Integrals | ✅ v1 |
| 8 | Application of Integrals | ✅ v1 |
| 9 | Differential Equations | ✅ v1 |
| 10 | Vector Algebra | ✅ v1 |
| 11 | Three Dimensional Geometry | ✅ v1 |
| 12 | Linear Programming | ✅ v1 |
| 13 | Probability | ✅ v1 |

### Physics (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Electric Charges and Fields | ✅ v1 |
| 2 | Electrostatic Potential and Capacitance | ✅ v1 |
| 3 | Current Electricity | ✅ v1 |
| 4 | Moving Charges and Magnetism | ✅ v1 |
| 5 | Magnetism and Matter | ✅ v1 |
| 6 | Electromagnetic Induction | ✅ v1 |
| 7 | Alternating Current | ✅ v1 |
| 8 | Electromagnetic Waves | ✅ v1 |
| 9 | Ray Optics and Optical Instruments | ✅ v1 |
| 10 | Wave Optics | ✅ v1 |
| 11 | Dual Nature of Radiation and Matter | ✅ v1 |
| 12 | Atoms | ✅ v1 |
| 13 | Nuclei | ✅ v1 |
| 14 | Semiconductor Electronics | ✅ v1 |

### Chemistry (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Solutions | ✅ v1 |
| 2 | Electrochemistry | ✅ v1 |
| 3 | Chemical Kinetics | ✅ v1 |
| 4 | d and f Block Elements | ✅ v1 |
| 5 | Coordination Compounds | ✅ v1 |
| 6 | Haloalkanes and Haloarenes | ✅ v1 |
| 7 | Alcohols, Phenols and Ethers | ✅ v1 |
| 8 | Aldehydes, Ketones and Carboxylic Acids | ✅ v1 |
| 9 | Amines | ✅ v1 |
| 10 | Biomolecules | ✅ v1 |

### Biology (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | Sexual Reproduction in Flowering Plants | ✅ v1 |
| 2 | Human Reproduction | ✅ v1 |
| 3 | Reproductive Health | ✅ v1 |
| 4 | Principles of Inheritance and Variation | ✅ v1 |
| 5 | Molecular Basis of Inheritance | ✅ v1 |
| 6 | Evolution | ✅ v1 |
| 7 | Human Health and Disease | ✅ v1 |
| 8 | Microbes in Human Welfare | ✅ v1 |
| 9 | Biotechnology: Principles and Processes | ✅ v1 |
| 10 | Biotechnology and its Applications | ✅ v1 |
| 11 | Organisms and Populations | ✅ v1 |
| 12 | Ecosystem | ✅ v1 |
| 13 | Biodiversity and Conservation | ✅ v1 |

### English - Flamingo (40 Questions per Chapter)
| Ch # | Chapter Title | Status |
| :--- | :--- | :--- |
| 1 | The Last Lesson | ✅ v1 |
| 2 | Lost Spring | ✅ v1 |
| 3 | Deep Water | ✅ v1 |
| 4 | The Rattrap | ✅ v1 |
| 5 | Indigo | ✅ v1 |

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