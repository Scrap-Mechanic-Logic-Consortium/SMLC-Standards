#!/usr/bin/python3

import requests
import os
import base64
import json

request_url = 'https://api.github.com/repos/Scrap-Mechanic-Logic-Consortium/SMLC-Website/contents/gitRepos.json'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer '+os.environ['WEBSITE_BUILD_TOKEN'],
    'X-GitHub-Api-Version': '2022-11-28'
}
while True:
    response = requests.get(request_url, headers=headers)

    if not response.ok:
        print('Failed to get gitRepos.json from GitHub')
        print(response.status_code, response.text)
        exit(1)

    responseData = response.json()
    content = json.loads(base64.b64decode(responseData['content']).decode('utf-8'))

    # update version of self repo: https://github.com/Scrap-Mechanic-Logic-Consortium/SMLC-Standards.git

    for repo in content:
        if repo['repo'] == 'https://github.com/Scrap-Mechanic-Logic-Consortium/SMLC-Standards.git':
            repo['commit'] = os.environ['GITHUB_SHA']
            break

    content = json.dumps(content, indent=4)
    content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    data = {
        'message': 'Update SMLC-Standards version',
        'content': content,
        'sha': responseData['sha']
    }
    response = requests.put(request_url, headers=headers, json=data)
    if response.ok:
        break
    elif response.status_code == 409:
        continue
    else:
        print('Failed to update gitRepos.json in GitHub')
        print(response.status_code, response.text)
        exit(1)