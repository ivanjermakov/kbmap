"""
Kbmap logger.
"""

import click

debug_enabled = False


def log(message):
    """
    Log message to console.
    """
    click.echo(message)


def debug(message):
    """
    Log message to console, only if debug_enable flag is active
    """
    if debug_enabled:
        click.echo(message)
