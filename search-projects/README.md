# Overview

`search-projects` is a Python script that searches through GitHub projects. It uses the [GitHub CLI](https://cli.github.com/) tool `gh`.

The script does the following:

1. Gets a list of projects
2. Loops through each project's item
3. Searches for the keywords within each item
4. Outputs a CSV file with the results 

# Usage

Run the script with:

```bash
python3 main.py
```

Enter your keywords when prompted.