# Overview

`search-projects` is a Python script that searches through GitHub projects. It uses the [GitHub CLI](https://cli.github.com/) tool `gh`.

The script does the following:

1. Gets a list of projects
2. Loops through project items
3. Searches for the keywords within each item
4. Outputs a results CSV file 

# Installation

Download or clone this repository into your local computer.

To download:

1. At the top of this repository, click the Code button
2. Click Download ZIP
3. Extract the zipped folder

To clone this repository, run the following command in your terminal:

```bash
git clone https://github.com/knqti/hfla-tools.git
```

## Change directory 

Navigate into the `search-projects` root directory:

```bash
cd /PATH/TO/search-projects
```

> Note: If you downloaded a ZIP folder, the extracted folder will include the branch name. Use the full name in your `cd` command.

## Dependencies

1. [Install GitHub CLI](https://github.com/cli/cli#installation)
2. [Authenticate to GitHub](https://docs.github.com/en/github-cli/github-cli/quickstart#prerequisites)

# Usage

Run the script:

```bash
python3 main.py
```

Enter your keywords when prompted.