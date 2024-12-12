import csv
import os
import subprocess as sp
from datetime import datetime

def get_repos(csv_file:str):
    list_of_repos = []
    
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            list_of_repos.append(row)
 
    return list_of_repos

def get_wikis(list_of_repos:list):
    list_of_wikis = []

    for item in list_of_repos:
        url = item[0]
        modified_url = f'{url}.wiki.git'        
        list_of_wikis.append(modified_url)
    
    return list_of_wikis

def clone_wiki(url:str):
    # Make a temporary folder
    tmp = './temp_folder'
    os.mkdir(tmp)
    
    # git clone the wiki
    sp.run(['git', 'clone', f'{url}', f'{tmp}'], text=True)
    
    return tmp

def rga_search(search_for:str, in_folder:str):
    # Use ripgrep-all tool to search the keywords
    rga_results = sp.run(['rga', f'{search_for}', f'{in_folder}'], text=True, capture_output=True)
    return rga_results

def export_to_csv(file_name:str, list_name:str):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list_name)

if __name__ == '__main__':
    now = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
    url_file = './repo_urls.csv'

    keywords = input('Keywords to search for: ').lower().strip()
    keywords_hyphened = keywords.replace(' ', '-')
    
    repo_list = get_repos(url_file)
    wiki_list = get_wikis(repo_list)
    
    results_list = [('Wiki URL', 'Keywords', 'rga Results')]

    for item in wiki_list:        
        wiki_git_url = str(item)
        temp_folder = clone_wiki(wiki_git_url)
        
        print(f'Searching {wiki_git_url}...')
        results = rga_search(keywords, temp_folder)        
        print(results.stdout)

        wiki_url = wiki_git_url.replace('.wiki.git', '/wiki')
        data_list = [(wiki_url, keywords, results)]    
        
        if results.stdout == None or results.stdout == '':
            print(f'No results found in wiki "{wiki_url}" for keywords "{keywords}".')
        else:
            results_list.extend(data_list)

        # Delete the temporary wiki folder
        sp.run(['rm', '-rf', temp_folder], text=True)
    
    output_file = f'{now}_wikis_found_{keywords_hyphened}.csv'
    export_to_csv(output_file, results_list)
    print(f'Done! See output file {output_file}')
