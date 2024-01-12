from src.medium import apis, config, formatter

if __name__ == '__main__':
    author_id = apis.getUserByToken(config.HEADERS)['data']['id']
    with open('README.md', 'r') as file:
        data = formatter.assembleDataForMediumPost(title='draft', html=False, file=file, tags=(), public=False, notify=False)
        post = apis.createPost(author_id, data, config.HEADERS)
        print('New Post Link: {}'.format(post['data']['url']))
