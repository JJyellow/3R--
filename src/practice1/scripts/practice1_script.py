"""CLI script for the practice1 package. This will be called on the command line"""

import click

from practice1.practice1 import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def practice1_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
