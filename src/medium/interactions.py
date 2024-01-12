import click
from . import apis, config, formatter

@click.command()
def createPost():
    title = click.prompt('The `title` of your post', type=click.STRING, default='Draft')

    filepath = click.prompt('The `filepath` you want to used to create the post', type=click.STRING)

    content_format = click.prompt('The format of the file content', type=click.Choice([config.CONTENT_TYPE_HTML, config.CONTENT_TYPE_MARKDOWN]), default=config.CONTENT_TYPE_MARKDOWN)

    publish_status = click.prompt('The status of the create post', type=click.Choice([config.PUBLISH_STATUS_UNLISTED, config.PUBLISH_STATUS_DRAFT, config.PUBLISH_STATUS_PUBLIC]), default=config.PUBLISH_STATUS_DRAFT)

    can_notify = click.prompt('Do you want to notify your follower when this post be published', type=click.BOOL, default=False)

    should_open_in_browser = click.prompt('Do you want to open the link of the created post in your default browser', type=click.BOOL, default=True)

    tags = click.prompt('The tags you want to set to the post (split by comma (,) symbols)', type=click.STRING, default='')
    tags = [tag.strip() for tag in tags.split(',')] if tags else []

    with open(filepath, 'r') as file:
        if click.confirm('Please check again; the above information is correct', abort=True):
            data = formatter.assembleDataForMediumPost(title, content_format, file, tags, publish_status, can_notify)
            author_id = apis.getUserByToken(config.HEADERS)['data']['id']
            post = apis.createPost(author_id, data, config.HEADERS)
            url_post = post['data']['url']

    click.echo('New Post Link: {}'.format(url_post))
    if should_open_in_browser and url_post:
        import webbrowser
        webbrowser.open(url_post)

if __name__ == '__main__':
    createPost()
