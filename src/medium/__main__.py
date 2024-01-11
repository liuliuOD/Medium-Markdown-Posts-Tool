import click
from . import apis, config

@click.command()
@click.option('-t', '--title', default='Draft', help='Title of the post. The default is `Draft`.')
@click.option('-f', '--file', default='README.md', help='The filepath used to create the post. The default is `README.md`.')
@click.option('-H', '--html', is_flag=True, help='The format of file content. The default is `markdown` if this flag is not set.')
def commands(title: str, file: str, html: bool):
    """
    Create Medium posts effortlessly using the CLI.
    """
    author_id = apis.getUserByToken(config.HEADERS)['data']['id']
    with open(file, 'r') as file:
        data = {
            'title': title,
            'contentFormat': config.CONTENT_TYPE_HTML if html else config.CONTENT_TYPE_MARKDOWN,
            'content': file.read(),
            'tags': [],
            'publishStatus': config.PUBLISH_STATUS_DRAFT,
            'license': config.LICENSE_ALL,
            'notifyFollowers': True
        }
        post = apis.createPost(author_id, data, config.HEADERS)

        click.echo('New Post Link: {}'.format(post['data']['url']))

if __name__ == '__main__':
    commands()
