from src.medium import formatter, services

if __name__ == '__main__':
    with open('README.md', 'r') as file:
        file_content = file.read()
        file_content = services.uploadImagesInMarkdown(file_content)
        data = formatter.assembleCommandsData(title='draft', html=False, file_content=file_content, tags=(), public=False, notify=False)
        print(data)

        post = services.createPost(data)
        print('New Post Link: {}'.format(formatter.getUrlFromResponse(post)))
