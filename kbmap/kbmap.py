import click

from kbmap import log, mapper


@click.command(short_help='Perform mapping.')
@click.argument('config_path')
@click.argument('device_name')
@click.option('--name', '-n', default='kbmap', help='Name of the virtual device that will write events.')
@click.option('--verbose', '-v', is_flag=True, help='Print detailed logs')
def main(config_path, device_name, name, verbose):
    """
    Create virtual device that will remap keyboard events from device with name DEVICE_NAME using CONFIG_PATH
    configuration.
    """
    log.debug_enabled = verbose
    mapper.map_device(config_path, device_name, name)


main()