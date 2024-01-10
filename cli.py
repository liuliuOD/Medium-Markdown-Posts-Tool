import click
import apis
import config

@click.command()
@click.option('--title', default='Draft', help='Title of the post. The default is `Draft`.')
@click.option('--file', default='README.md', help='The filepath used to create the post. The default is `README.md`.')
@click.option('--fm', default='md', help='The format of file content. Can choose either `md` or `html`. The default is `md`.')
def commands(title: str, file: str, fm: str):
    """
    Create Medium posts effortlessly using the CLI.
    """
    author_id = apis.getUserByToken(config.HEADERS)['data']['id']
    with open(file, 'r') as file:
        data = {
            'title': title,
            'contentFormat': config.CONTENT_TYPE_MARKDOWN if fm == 'md' else config.CONTENT_TYPE_HTML,
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
