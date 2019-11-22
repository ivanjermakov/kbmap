#!/usr/bin/env python3

import click

import mapper


@click.group()
def kbmap():
    pass


@kbmap.command(short_help='Perform mapping.')
@click.argument('config_path')
@click.argument('device_name')
@click.option('--uinput-name', default='kbmap', help='Name of the virtual device that will write events.')
def map(config_path, device_name, uinput_name):
    """
    Create virtual device that will remap keyboard events from device with name DEVICE_NAME using CONFIG_PATH
    configuration.
    """
    mapper.apply(config_path, device_name, uinput_name)


@kbmap.command(short_help='Test mapping matching on device.')
@click.argument('config_path')
@click.argument('device_name')
def test(config_path, device_name):
    """
    Preview config mappings in action on specified device.
    """
    mapper.test(
        config_path,
        device_name,
        lambda mappings: click.echo(mappings)
    )


@kbmap.command(short_help='List config mappings.')
@click.argument('config_path')
def list(config_path):
    """
    List config mappings.
    """
    click.echo(mapper.load_mappings(config_path))


kbmap()
