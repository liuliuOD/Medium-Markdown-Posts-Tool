import click
from . import apis, config
from typing import Tuple

@click.command()
@click.option('--title', default='Draft', help='Title of the post. The default is `Draft`.')
@click.option('-f', '--file', default='README.md', help='The filepath used to create the post. The default is `README.md`.')
@click.option('-H', '--html', is_flag=True, help='The format of file content. The default is `markdown` if this flag is not set.')
@click.option('-P', '--public', is_flag=True, help='The status of the created post. The default is `draft` if this flag is not set.')
@click.option('-N', '--notify', is_flag=True, help='Notify your follower.')
@click.option('-t', '--tags', multiple=True, default=[], help='The tags you want to set to the post.')
def commands(title: str, file: str, html: bool, public: bool, notify: bool, tags: Tuple):
    """
    Create Medium posts effortlessly using the CLI.
    """
    author_id = apis.getUserByToken(config.HEADERS)['data']['id']
    with open(file, 'r') as file:
        data = {
            'title': title,
            'contentFormat': config.CONTENT_TYPE_HTML if html else config.CONTENT_TYPE_MARKDOWN,
            'content': file.read(),
            'tags': tags,
            'publishStatus': config.PUBLISH_STATUS_PUBLIC if public else config.PUBLISH_STATUS_DRAFT,
            'license': config.LICENSE_ALL,
            'notifyFollowers': notify
        }
        post = apis.createPost(author_id, data, config.HEADERS)

        click.echo('New Post Link: {}'.format(post['data']['url']))

if __name__ == '__main__':
    commands()
