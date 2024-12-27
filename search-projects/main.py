import csv
import json
import subprocess as sp
from datetime import datetime

def get_project_numbers(owner:str):
    data = sp.run(['gh', 'project', 'list', '--owner', owner, '--format', 'json', '-L', '100'], text=True, capture_output=True)
    parsed_data = json.loads(data.stdout)

    numbers_titles = []

    for project in parsed_data['projects']:
        numbers_titles.append(project['number'])
        numbers_titles.append(project['title'])

    print(f'Total projects found: {len(numbers_titles) / 2}')

    return numbers_titles

def get_project_items(owner:str, numbers_titles:list, keywords:str):
    contents = []

    for item in range(0, len(numbers_titles), 2):
        number = numbers_titles[item]
        title = numbers_titles[item + 1]
        print(f'Project # {number}: {title}')

        try: 
            data = sp.run(['gh', 'project', 'item-list', str(number), '--owner', owner, '--format', 'json'], text=True, capture_output=True, encoding='utf-8')
            parsed_data = json.loads(data.stdout)
            
            if parsed_data['items']:
                print(f'Searching through {len(parsed_data["items"])} project items...')

                content_matches = search_keywords(parsed_data, keywords)
                contents.extend(content_matches)
        
        except Exception as e:
            print('== Exception Error ==')
            print(f'{e}\n')
            print(f'Project number: {number}')
            print(f'Project title: {title}')

    return contents

def search_keywords(data, keywords:str):
    matches = []

    for entry in data['items']:
        content = entry.get('content', {})
        title = content.get('title', '').lower()
        body = content.get('body', '').lower()
        keyword_lower = keywords.lower()

        if keyword_lower in title or keyword_lower in body:
            matches.append(content)

    return matches

def list_to_csv(data, output_file, col_names):
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    now = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
    keywords = input('Keywords to search for: ')
    owner = 'hackforla'

    project_numbers = get_project_numbers(owner)
    project_items = get_project_items(owner, project_numbers, keywords)
    
    if project_items:
        keys = project_items[0].keys()
        output_file = f'{now}_projects_{keywords}.csv'
        list_to_csv(project_items, output_file, keys)
        print(f'Done! Found {len(project_items)} results. \nOutput file ready: {output_file}')
    else:
        print('Done! No results found.')
