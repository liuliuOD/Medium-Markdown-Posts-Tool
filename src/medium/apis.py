import requests
from typing import Dict, List

def getUserByToken(headers: Dict, timeout: int = 10) -> Dict:
    response = requests.get('https://api.medium.com/v1/me', headers=headers, timeout=timeout)

    response.raise_for_status()

    return response.json()

def createPost(author_id: str, data: List, headers: Dict, timeout: int = 10) -> Dict:
    response = requests.post(f'https://api.medium.com/v1/users/{author_id}/posts', data=data, headers=headers, timeout=timeout)

    response.raise_for_status()

    return response.json()

def uploadImage(headers: Dict, files: Dict, timeout: int = 10) -> Dict:
    response = requests.post('https://api.medium.com/v1/images', files=files, headers=headers, timeout=timeout)

    response.raise_for_status()

    return response.json()
