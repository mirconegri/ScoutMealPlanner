# 🏕️ Scout Meal Planner

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> 🌐 **<a href="https://scoutmealplanner.mirconegri.com" target="_blank">Visit the project website</a>**

A Python console application that generates a randomized multi-day camp menu and a fully scaled shopping list, designed for scout groups cooking over a campfire with no oven or complex equipment.

Replaces a manual spreadsheet process that previously required roughly two hours of planning per trip. Enter headcount and number of days; get a complete, print-ready menu and shopping list in seconds.

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

- Randomized breakfast combinations (bread with Nutella, bread with jam, or tea with bread and jam), each mapped to its own shopping-list entries
- Randomized lunch and dinner combinations built from carbs, protein, and vegetables — plus two fruit choices per day
- Per-person ingredient quantities (grams/ml) defined once in `meals_data.py` and automatically scaled by participant count
- Generates three output files per run: a human-readable menu, a formatted shopping list, and a CSV for spreadsheet import
- A fresh menu is produced on every run — no two trips get the same plan
- Zero external dependencies — built entirely on the Python standard library

## Tech Stack

- **Language:** Python 3.x
- **Standard library:** `random`, `collections.defaultdict`, `csv`

No third-party packages required. Everything ships with a standard Python installation.

## Project Structure

```
ScoutMealPlanner/
├── main.py              # Entry point — menu generation and file output
├── meals_data.py        # Ingredient options and per-person quantities
├── requirements.txt
├── screenshot/
│   ├── terminal.png
│   ├── shopping_list.png
│   └── menu.png
├── README.md
└── LICENSE
```

> Running `main.py` produces `menu.txt`, `shopping_list.txt`, and `shopping_list.csv` in the project root at runtime. These files are not committed to the repository.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/mirconegri/ScoutMealPlanner.git
cd ScoutMealPlanner
```

No further installation steps are required.

#### Run Online

Run directly in your browser without installing anything:

1. Go to [replit.com](https://replit.com/)
2. Click **Create** → **Import from GitHub**
3. Paste `https://github.com/mirconegri/ScoutMealPlanner`
4. Click **Run**

## Usage

```bash
python3 main.py
```

```
Welcome to Scout Meal Planner
Enter number of camp days: 3
Enter number of participants: 12
```

Output files generated in the current directory:

| File | Description |
|---|---|
| `menu.txt` | Daily menu — breakfast, lunch, dinner, and fruits |
| `shopping_list.txt` | Aggregated ingredient list with total quantities |
| `shopping_list.csv` | Same list formatted for Excel or LibreOffice |

Sample output:

```
Day 1:
  Breakfast: Bread with Nutella
  Lunch:     Pasta with tuna and peppers
  Dinner:    Rice with sausages and zucchini
  Fruits:    Apples, Oranges
```

## Configuration and Environment

No environment variables or configuration files are required. All parameters — number of days and participants — are provided interactively at runtime.

To add new meals or adjust quantities, edit `meals_data.py` directly. Each entry defines ingredients and their per-person amounts; the shopping list aggregates these automatically across all days.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes with a clear message
4. Open a Pull Request

For bugs or ideas (e.g. dietary restriction filters or new meal templates), open an [Issue](https://github.com/mirconegri/ScoutMealPlanner/issues).

### Author

**Mirco Negri** — Computer Science @ UniTrento

[![Portfolio](https://img.shields.io/badge/Portfolio-00599C?style=for-the-badge&logo=globe&logoColor=white)](https://mirconegri.github.io/Portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mirconegri)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mirco-negri-263810225)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mirconegri06@gmail.com)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
