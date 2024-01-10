import apis
import config

if __name__ == '__main__':
    author_id = apis.getUserByToken(config.HEADERS)['data']['id']
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
        post = apis.createPost(author_id, data, config.HEADERS)
        print('New Post Link: {}'.format(post['data']['url']))
