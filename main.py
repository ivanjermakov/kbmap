import click


@click.command()
@click.argument('config_path')
@click.argument('device_name')
@click.option('--uinput-name', default='kbmap', help='Name of the virtual device that will write events')
def apply(config_path, device_name, uinput_name):
    """
    Create virtual device that will remap keyboard events from device with name DEVICE_NAME using CONFIG_PATH
    configuration.
    """
    # print(f'commands: "{config_path}" "{device_name}" "{uinput_name}"')
    import kbmap
    kbmap.apply(config_path, device_name, uinput_name)


apply()
