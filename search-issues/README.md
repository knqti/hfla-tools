# Overview

`search-issues` is a Python script that searches for GitHub issues. It uses the Python client, [ghapi](https://ghapi.fast.ai/), to access [GitHub's REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28). 

The script does the following:

1. Asks for keywords to search for
2. Loops through a CSV file of repositories
3. Calls the API for issues within each repository
4. Searches for the keywords within each issue
5. Outputs two results CSV files: 

   i. Repositories with issues found

   ii. Repositories with no issues found

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

Navigate into the `search-issues` root directory:

```bash
cd /PATH/TO/search-issues
```

> Note: If you downloaded a ZIP folder, the extracted folder will include the branch name. Use the full name in your `cd` command.

## Dependencies

Install dependencies from *requirements.txt*:

```bash
pip install -r ./requirements.txt
```

## Personal access token (optional)

A GitHub personal access token is optional, but recommended. Using a token increases API rate limits and provides access to restricted repositories you might otherwise need to login to.

To create a token, see [Managing your personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#about-personal-access-tokens).

To use your token, create a *.env* file:

```bash
echo "GITHUB_TOKEN = 'YOUR_TOKEN_GOES_HERE'" > .env
```

# Usage

Run the script:

```bash
python3 main.py
```

Enter your keywords to search when prompted.

> Tip: `search-issues` searches through the repository links in *repo_urls.csv*. Update the links as needed.

# API References

- `ghapi` method [search.issues_and_pull_requests](https://ghapi.fast.ai/fullapi.html)
- GitHub API endpoint [Search issues and pull requests](https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-issues-and-pull-requests)
