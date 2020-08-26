import click

debug = False


def log(message):
    if debug:
        click.echo(message)
