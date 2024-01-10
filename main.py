import apis
import config
import os
from dotenv import load_dotenv
load_dotenv()

HEADERS = {
    'Authorization': 'Bearer {}'.format(os.getenv('TOKEN')),
    'User-Agent': os.getenv('USER_AGENT')
}

if __name__ == '__main__':
    author_id = apis.getUserByToken(HEADERS)['data']['id']
    with open('README.md', 'r') as file:
        data = {
            'title': 'draft',
            'contentFormat': config.CONTENT_TYPE_MARKDOWN,
            'content': file.read(),
            'tags': [],
            'publishStatus': config.PUBLISH_STATUS_DRAFT,
            'license': config.LICENSE_ALL,
            'notifyFollowers': True
        }
        post = apis.createPost(author_id, data, HEADERS)
        print(f'New Post Link: {post['data']['url']}')
