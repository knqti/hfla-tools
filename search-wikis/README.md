# Overview

[Hack for LA Guides](https://github.com/hackforla/guides) members gather examples from [GitHub Wikis](https://github.com/hackforla/guides/wiki/Gathering-Examples-with-Github) as part of the initial guide-making process. 

`hfla-search-wikis` is a Python script that searches for Wikis within GitHub repositories. It uses [`ripgrep-all`](https://github.com/phiresky/ripgrep-all), a command-line tool, to search for keywords within the Wikis' files.

The script does the following:

1. Asks for keywords to search for
2. Loops through a CSV file of repositories
3. Clones each repository's Wiki
4. Searches for the keywords within the Wiki
5. Deletes the Wiki
6. Outputs a results file

# How to Use

Follow the steps below to use `hfla-search-wikis`.

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [`ripgrep-all`](https://github.com/phiresky/ripgrep-all?tab=readme-ov-file#installation)
- [`git`](https://git-scm.com/downloads)
- bash terminal

## Download

To download a copy:

1. At the top of this repository, click the Code button
2. Click Download ZIP
3. Extract the zipped folder

> Note: If you use the Download ZIP option, the folder will have the branch name added to the end.

To clone this repository, run the bash command in your terminal:

```bash
git clone https://github.com/knqti/hfla-search-wikis.git
```

## Change directory 

Navigate into `hfla-search-wikis`' root directory:

```bash
cd /PATH/TO/hfla-search-wikis
```

## Run

To run `hfla-search-wikis`:

```bash
python3 main.py
```

You are prompted with `Keywords to search for:`. Type your keywords and press enter. 

`hfla-search-wikis` searches through the repository links in *repo_urls.csv*. Update the links as needed.
