import click
from . import commands, interactions

@click.group()
def cli():
    pass

cli.add_command(commands.createPost, name='post:create')
cli.add_command(interactions.createPost, name='post:interact')

if __name__ == '__main__':
    cli()
