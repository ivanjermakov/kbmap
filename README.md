<img src="https://sun9-30.userapi.com/c853628/v853628642/15d5ac/OLBRQhGJb00.jpg">

<h3 align="center">KBMAP</h3>

<p align="center">
    Linux keyboard mapping utility
    <br>
    <a href="https://github.com/ivanjermakov/kbmap/actions">
        <img src="https://img.shields.io/github/workflow/status/ivanjermakov/kbmap/kbmap">
    </a>
    <a href="https://codecov.io/gh/ivanjermakov/kbmap">
        <img src="https://codecov.io/gh/ivanjermakov/kbmap/branch/master/graph/badge.svg">
    </a>
</p>

# NOTICE
**This project is discontinued, I recommend using [KMonad](https://github.com/kmonad/kmonad) as it's capable of everything *kbmap* planned to support**

### About
Mapping physical keyboard keys under Linux system is tricky. Since there is multiple places where you can interrupt and handle keystroke, there is a ton of solutions for different levels. KBMAP focuses on handling keystroke straight from the physical device, before [converting keycode to the keysym](https://wiki.archlinux.org/index.php/Keyboard_input) (it's a place, where windowing system applies keyboard layouts and locales).

KBMAP allows you to apply flexible configurations directly to the keyboard input device without writing a mess of C code or breaking system config files. 

KBMAP is heavily inspired by [QMK](https://github.com/qmk/qmk_firmware/) - highly customizable mechanical keyboard firmware. Basically, ideally KBMAP will be the QMK of any non-programmable keyboard (and maybe not only keyboard).

### Installing
````shell script
pip install kbmap
````

### Usage
````shell script
Usage: kbmap [OPTIONS] DEVICE_NAME

  Create virtual device that will remap keyboard events from device with
  name DEVICE_NAME.

Options:
  --version          Show the version and exit.
  -c, --config TEXT  Mapping configuration path.
  -n, --name TEXT    Name of the virtual device that will write events.
  -v, --verbose      Print detailed logs.
  --help             Show this message and exit.
````

### FAQ
**Q: How it works?**\
A: KBMAP uses [evdev](https://en.wikipedia.org/wiki/Evdev) - a Linux input event interface.
There is python binding for evdev library: [python-evdev](https://python-evdev.readthedocs.io/en/latest/).
Mapping algorithm:
1. Find a target device by name (specified with DEVICE_NAME argument)
2. Create new [uinput device](https://python-evdev.readthedocs.io/en/latest/apidoc.html#module-evdev.uinput) (kind of a virtual input device) with specified name (--name option)
3. [Grab](https://python-evdev.readthedocs.io/en/latest/apidoc.html?highlight=grab#evdev.device.InputDevice.grab) target device (so only KBMAP process receive input events)
4. Listen for key events from target device
5. Perform remapping based on config file (specified with CONFIG_PATH argument)
6. Dispatch events through created uinput device

**Q: Linux only?**\
A: Yes, since [evdev](https://en.wikipedia.org/wiki/Evdev) is a specific Linux interface, KBMAP cannot be used on non-unix operating systems.

**Q: Alternatives for Windows?**\
A: [AutoHotkey](https://en.wikipedia.org/wiki/AutoHotkey).

**Q: How is KBMAP related to QMK?**\
A: QMK has a lot of mapping features.
But QMK is a firmware and you cannot use it unless your keyboard is programmable.
The mind behind KBMAP is to allow non-programmable keyboard users to achieve QMK-like customizability with their input device.
Current goal is to reach [TMK](https://github.com/tmk/tmk_core) (a program, QMK being forked from) functionality.

**Q: I am getting UInputError: "/dev/uinput" cannot be opened for writing.**\
A: [Solution](https://github.com/ivanjermakov/kbmap/issues/8).

**Q: How to run KBMAP at system boot?**\
A: It can be done in several ways, check out [stackoverflow question](https://stackoverflow.com/questions/12973777/how-to-run-a-shell-script-at-startup) and [Arch Linux wiki page](https://wiki.archlinux.org/index.php/Autostarting).

**Q: What features are already implemented?**\
**Q: How to configure KBMAP?**\
**Q: KBMAP keycodes?**\
A: See [wiki](https://github.com/ivanjermakov/kbmap/wiki).


### Documentation
Documentation and useful resources can be found in [wiki](https://github.com/ivanjermakov/kbmap/wiki).
