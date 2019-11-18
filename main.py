import click


@click.command()
@click.argument('config_path')
@click.argument('device_name')
@click.option('--uinput-name', default='kbmap')
def apply(config_path, device_name, uinput_name):
    print(f'commands: "{config_path}" "{device_name}" "{uinput_name}"')
    import kbmap
    kbmap.apply(config_path, device_name, uinput_name)


apply()
