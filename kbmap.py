#!/usr/bin/env python3

import click

import mapper


@click.group()
def kbmap():
    pass


@kbmap.command()
@click.argument('config_path')
@click.argument('device_name')
@click.option('--uinput-name', default='kbmap', help='Name of the virtual device that will write events.')
def map(config_path, device_name, uinput_name):
    """
    Create virtual device that will remap keyboard events from device with name DEVICE_NAME using CONFIG_PATH
    configuration.
    """
    mapper.apply(config_path, device_name, uinput_name)


@kbmap.command()
@click.argument('config_path')
@click.argument('device_name')
def test(config_path, device_name):
    """
    Preview config's mappings in action.
    """
    mapper.test(
        config_path,
        device_name,
        lambda mappings: click.echo(mappings)
    )


kbmap()
