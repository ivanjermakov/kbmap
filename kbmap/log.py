import click

debug_enabled = False


def log(message):
    click.echo(message)


def debug(message):
    if debug_enabled:
        click.echo(message)
