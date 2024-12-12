# Overview

`search-wikis` is a Python script that searches through GitHub wikis. It uses [ripgrep-all](https://github.com/phiresky/ripgrep-all), a command-line tool, to search for keywords within the wiki files.

The script does the following:

1. Loops through a CSV file of repositories
2. Clones each repository's wiki
3. Searches for the keywords within each wiki
4. Deletes the cloned wikis
5. Outputs a results file

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

Navigate into `search-wikis`' root directory:

```bash
cd /PATH/TO/search-wikis
```

## Dependencies

[Install ripgrep-all](https://github.com/phiresky/ripgrep-all?tab=readme-ov-file#installation).

## Usage

Run the script:

```bash
python3 main.py
```

Enter your keywords when prompted.

> Tip: `search-wikis` searches through the repository links in *repo_urls.csv*. Update the links as needed.
