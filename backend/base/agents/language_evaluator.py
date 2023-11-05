import requests
import re


def get_github_repo_languages(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return data.items()
        else:
            print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")



def convert_github_url_to_api(url):
    match = re.match(r'https://github\.com/([^/]+)/([^/]+)', url)
    
    if match:
        username, repository = match.groups()
        
        api_url = f'https://api.github.com/repos/{username}/{repository}/languages'
        
        return api_url
    else:
        return None



def language_evaluator(project_url, claimed_languages):
  language_api_url = convert_github_url_to_api(project_url)
  print(language_api_url)

  actual_languages_data = dict(get_github_repo_languages(language_api_url))
  print(actual_languages_data)

  actual_languages = list(actual_languages_data.keys())
  print(actual_languages)

  total_claimed_languages = len(claimed_languages)

  actual_found_languages = 0

  for clanguage in claimed_languages:
    for alanguage in actual_languages:
      if clanguage.lower() == alanguage.lower():
        actual_found_languages += 1

# reducing the score for giving false information
  score = actual_found_languages - ((total_claimed_languages - actual_found_languages) / 2)

  if score < 0:
    score = 0

  return score




language_evaluator('https://github.com/psn0w/JApi', ['shell', 'python', 'R', 'C++', 'React', 'css', 'html', 'flask'])