![ASCII art](https://sun9-30.userapi.com/c853628/v853628642/15d5ac/OLBRQhGJb00.jpg)

# KBMAP
Linux keyboard mapping utility

### About
Mapping physical keyboard keys under Linux system is tricky. Since there is multiple places where you can interrupt and handle keystroke, there is a ton of solutions for different levels. But if you need to handle keystroke straight from the physical device, before [converting keycode to the keysym](https://wiki.archlinux.org/index.php/Keyboard_input) (it's a place, where windowing system applies keyboard layouts and locales), then you need a low-level solution. **No more!** 

KBMAP allows you to apply flexible configurations directly to the keyboard input device without writing a mess of C code or breaking system config files. 

Core concepts and features:
 * mapping physical device input, before a [windowing system](https://en.wikipedia.org/wiki/Windowing_system) comes in
 * no differentiation between modifier and character keys (you can use character key as modifier)
 * flexible configuration system
 * alternative software configuration support

### Installing
````shell script
git clone https://github.com/ivanjermakov/kbmap.git
````

### Usage
````shell script
main.py [OPTIONS] CONFIG_PATH DEVICE_NAME

  Create virtual device that will remap keyboard events from device with
  name DEVICE_NAME using CONFIG_PATH configuration.

Options:
  --uinput-name TEXT  Name of the virtual device that will write events
  --help              Show this message and exit.
````

Note: configuration is applied only for current boot. Probably, you may want to run this at system startup.

### Documentation
Documentation and useful resources can be found in [wiki](https://github.com/ivanjermakov/kbmap/wiki).