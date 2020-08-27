#!/usr/bin/env python3

import click

import log
import mapper


@click.command(short_help='Perform mapping.')
@click.argument('config_path')
@click.argument('device_name')
@click.option('--name', '-n', default='kbmap', help='Name of the virtual device that will write events.')
@click.option('--verbose', '-v', is_flag=True, help='Print detailed logs')
def kbmap(config_path, device_name, uinput_name, verbose):
    """
    Create virtual device that will remap keyboard events from device with name DEVICE_NAME using CONFIG_PATH
    configuration.
    """
    log.debug = verbose
    mapper.map(config_path, device_name, uinput_name)


kbmap()
