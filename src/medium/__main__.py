import click
from . import commands

@click.group()
def cli():
    pass

cli.add_command(commands.createPost, name='post:create')

if __name__ == '__main__':
    cli()
