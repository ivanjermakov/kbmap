import click
import pkg_resources

from kbmap import log, mapper

VERSION = f'v{pkg_resources.require("kbmap")[0].version}'

WELCOME_MESSAGE = f"""\


    $$\   $$\ $$$$$$$\  $$\      $$\  $$$$$$\  $$$$$$$\  
    $$ | $$  |$$  __$$\ $$$\    $$$ |$$  __$$\ $$  __$$\ 
    $$ |$$  / $$ |  $$ |$$$$\  $$$$ |$$ /  $$ |$$ |  $$ |
    $$$$$  /  $$$$$$$\ |$$\$$\$$ $$ |$$$$$$$$ |$$$$$$$  |
    $$  $$<   $$  __$$\ $$ \$$$  $$ |$$  __$$ |$$  ____/ 
    $$ |\$$\  $$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |      
    $$ | \$$\ $$$$$$$  |$$ | \_/ $$ |$$ |  $$ |$$ |      
    \__|  \__|\_______/ \__|     \__|\__|  \__|\__|      
{VERSION.rjust(57, ' ')}   
"""

@click.command()
@click.argument('device_name')
@click.version_option(version=WELCOME_MESSAGE, message='%(version)s')
@click.option('--config', '-c', required=False, help='Mapping configuration path;')
@click.option('--name', '-n', default='kbmap', help='Name of the virtual device that will write events;')
@click.option('--verbose', '-v', is_flag=True, help='Print detailed logs;')
def main(config, device_name, name, verbose):
    """
    Create virtual device that will remap keyboard events from device with name DEVICE_NAME.
    """
    log.debug_enabled = verbose
    mapper.map_device(device_name, config, name)


main()
