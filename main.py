from src.medium import apis, config, formatter, services

if __name__ == '__main__':
    # author_id = apis.getUserByToken(config.HEADERS)['data']['id']
    # with open('README.md', 'r') as file:
    #     data = formatter.assembleCommandsData(title='draft', html=False, file=file.read(), tags=(), public=False, notify=False)
    #     post = apis.createPost(author_id, data, config.HEADERS)
    #     print('New Post Link: {}'.format(post['data']['url']))

    with open('README.md', 'r') as file:
        data = file.read()
        data = services.uploadImagesInMarkdown(data)

        print(data)
