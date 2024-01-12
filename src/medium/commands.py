import click
from . import formatter
from . import apis, config

@click.command()
@click.option('--title', default='Draft', show_default='Draft', help='Title of the post.')
@click.option('-f', '--file', default='README.md', show_default='README.md', help='The filepath used to create the post.')
@click.option('-H', '--html', is_flag=True, show_default='markdown', help='The format of file content.')
@click.option('-P', '--public', is_flag=True, show_default='draft', help='The status of the created post.')
@click.option('-N', '--notify', is_flag=True, help='Notify your follower.')
@click.option('-O', '--open-in-browser', is_flag=True, help='Open the created post in your default browser.')
@click.option('-t', '--tags', multiple=True, default=[], help='The tags you want to set to the post.')
def createPost(title: click.STRING, file: click.STRING, html: click.BOOL, public: click.BOOL, notify: click.BOOL, open_in_browser: click.BOOL, tags: click.Tuple):
    """
    Create Medium posts effortlessly using the CLI.
    """
    author_id = apis.getUserByToken(config.HEADERS)['data']['id']
    with open(file, 'r') as file:
        data = formatter.assembleCommandsData(title, html, file, tags, public, notify)
        post = apis.createPost(author_id, data, config.HEADERS)
        url_post = post['data']['url']

    click.echo('New Post Link: {}'.format(url_post))
    if open_in_browser and url_post:
        import webbrowser
        webbrowser.open(url_post)

if __name__ == '__main__':
    createPost()
