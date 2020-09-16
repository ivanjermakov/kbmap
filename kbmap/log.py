"""
Kbmap logger.
"""

import click

debug_enabled: bool = False


def log(message: str) -> None:
    """
    Log message to console.
    """
    click.echo(message)


def debug(message: str) -> None:
    """
    Log message to console, only if debug_enable flag is active
    """
    if debug_enabled:
        click.echo(message)


def error(message: str) -> None:
    """
    Log error message to console.
    """
    click.echo(click.style(message, fg='red'), err=True)
