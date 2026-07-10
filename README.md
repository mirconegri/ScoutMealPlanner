# 🏕️ Scout Meal Planner

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A Python console application that generates a randomized multi-day camp menu — breakfast, lunch, dinner, and fruit — along with a scaled shopping list, designed for active teenagers (16–18) cooking over a campfire with no ovens or complex recipes required.

## Table of Contents

- [Preview](#preview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration and Environment](#configuration-and-environment)
- [Contributing](#contributing)
- [License](#license)

## Preview

**Terminal Interface**

<p align="center"><img src="screenshot/terminal.png" width="650px"></p>

| Shopping List | Menu Overview |
|:---:|:---:|
| <img src="screenshot/shopping_list.png" height="500px"> | <img src="screenshot/menu.png" height="500px"> |

## Features

- Randomized breakfast selection (bread with Nutella, bread with jam, or tea with bread and jam), each with its own matching shopping-list entries
- Randomized lunch and dinner combinations built from carbs, protein, and vegetables, plus two fruit choices per day
- Per-person quantities (grams/ml) defined per ingredient, automatically scaled by the number of participants
- Generates three output files per run: a readable menu, a formatted shopping list, and a CSV version for spreadsheets
- A fresh, different menu is produced on every run
- No external dependencies — built entirely on the Python standard library

## Tech Stack

- **Language:** Python 3.x
- **Standard library modules used:** `random`, `collections.defaultdict`, `csv`

> This project has no third-party runtime dependencies. Everything needed to run it ships with a standard Python installation.

## Project Structure

```
ScoutMealPlanner/
├── main.py              # Entry point — menu/shopping-list generation and file output
├── meals_data.py        # Ingredient options and per-person quantities
├── requirements.txt
├── screenshot/
│   ├── terminal.png
│   ├── shopping_list.png
│   └── menu.png
├── README.md
└── LICENSE
```

> **Note:** running `main.py` also produces `menu.txt`, `shopping_list.txt`, and `shopping_list.csv` in the project root — these are generated at runtime and are not part of the committed repository structure.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/mirconegri/ScoutMealPlanner.git
cd ScoutMealPlanner
```

No further installation steps are required — there are no packages to install.

#### Run Online (No Installation)

You can also run the project directly in your browser via Replit:

1. Go to [replit.com](https://replit.com/)
2. Click **Create** → **Import from GitHub**
3. Paste the repository URL: `https://github.com/mirconegri/ScoutMealPlanner`
4. Click **Run** and interact with the program directly in the browser console

## Usage

```bash
python3 main.py
```

You'll be prompted for two values:

```
🔥 Welcome to Scout Meal Planner 🔥
Enter number of camp days: 3
Enter number of participants: 12
```

The script then generates three files in the current directory:

| File | Description |
|---|---|
| `menu.txt` | Human-readable daily menu (breakfast, lunch, dinner, fruits) |
| `shopping_list.txt` | Aggregated ingredient list with total quantities |
| `shopping_list.csv` | Same shopping list, formatted for Excel/LibreOffice |

Example excerpt from `menu.txt`:

```
Day 1:
  🍞 Breakfast: bread with Nutella
  🍽️ Lunch: Pasta with tuna and peppers
  🍽️ Dinner: Rice with sausages and zucchini
  🍎 Fruits: Apples, Oranges
```

## Configuration and Environment

This project requires no environment variables or configuration files. All parameters (camp days, participants) are provided interactively via terminal input at runtime.

## Contributing

Contributions are welcome! To propose a change:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes with a clear message
4. Open a Pull Request

Found a bug or have an idea (e.g. new meal templates)? Open an [Issue](https://github.com/mirconegri/ScoutMealPlanner/issues).

### 👤 Author & Connect

**Mirco Negri** — *Computer Science Student @ UniTrento*

[![Portfolio](https://img.shields.io/badge/Portfolio-00599C?style=for-the-badge&logo=globe&logoColor=white)](https://mirconegri.github.io/Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mirconegri)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mirco-negri-263810225)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mirconegri06@gmail.com)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mirco_negri_?igsh=MWtlbXY0a3R4NTJmNA==)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/share/172rhaPCUK/)

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
<br>
© 2026 Mirco Negri
