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

### How it works
KBMAP use [python-evdev](https://github.com/gvalkov/python-evdev) to communicate with input devices.

Setup:
 1. Find device with specified name
 2. [Grab](https://python-evdev.readthedocs.io/en/latest/apidoc.html?highlight=grab#evdev.device.InputDevice.grab) it
 3. Create [uinput](https://python-evdev.readthedocs.io/en/latest/apidoc.html#module-evdev.uinput) device that will [write](https://python-evdev.readthedocs.io/en/latest/apidoc.html#evdev.eventio.EventIO.write) mapped keystrokes
 4. Listen for input keyboard events
 5. Handle them

Handling keystroke:
 1. Receive key event (`EV_KEY`)
 2. Get other active keys (aka. modifiers) and create `Combination`
 3. Match combination with configured mappings
 - If match with any: pass mapped combination to `uinput` with currently pressed modifiers
 - If not matched with any: pass it directly to `uinput`

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

### Configuration
As a configuration file you need to provide python `.py` file with global variable named `mappings`. It contain a list of `Mapping` objects and define mapping behavior.

Example configuration to map `ijkl` keys to act as arrow keys while `Caps Lock` is pressed.
 * Using explicit syntax (for simple keystrokes):
   ````python
   # config.py
   from combination import Combination
   from keys import *
   from mapping import Mapping
   
   mappings = [
       Mapping(Combination(J, [CAPSLOCK]), Combination(LEFT)),
       Mapping(Combination(K, [CAPSLOCK]), Combination(DOWN)),
       Mapping(Combination(L, [CAPSLOCK]), Combination(RIGHT)),
       Mapping(Combination(I, [CAPSLOCK]), Combination(UP))
   ]
   ````
 * Using `bind` method:
   ````python
   # config.py
   from keys import *
   
   from mapping import Mapping
     
   mappings = Mapping.bind(
       [CAPSLOCK],
       [
           J, K, L, I
       ],
       [],
       [
           LEFT, DOWN, RIGHT, UP
       ]
   )
   ````
 * Using `bind` method and providing full keyboard layout (preferred for "layer mappings"):
   ````python
   # config.py
   from keys import *
   
   from mapping import Mapping
   
   mappings = Mapping.bind(
       [CAPSLOCK],
       [
           ESC, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, SYSRQ, SCROLLLOCK, PAUSE,
           GRAVE, K1, K2, K3, K4, K5, K6, K7, K8, K9, K0, MINUS, EQUAL, BACKSPACE, INSERT, HOME, PAGEUP,
           TAB, Q, W, E, R, T, Y, U, I, O, P, LEFTBRACE, RIGHTBRACE, BACKSLASH, DELETE, END, PAGEDOWN,
           CAPSLOCK, A, S, D, F, G, H, J, K, L, SEMICOLON, APOSTROPHE, ENTER,
           LEFTSHIFT, Z, X, C, V, B, N, M, COMMA, DOT, SLASH, RIGHTSHIFT, UP,
           LEFTCTRL, LEFTMETA, LEFTALT, SPACE, RIGHTALT, COMPOSE, RIGHTCTRL, LEFT, DOWN, RIGHT,
       ],
       [],
       [
           NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
           NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
           NO, NO, NO, NO, NO, NO, NO, NO, UP, NO, NO, NO, NO, NO, NO, NO, NO,
           NO, NO, NO, NO, NO, NO, NO, LEFT, DOWN, RIGHT, NO, NO, NO,
           NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
           NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
       ]
   )
   ````
 * Using custom configuration script. Python file is a python file. You can write anything you want here (if it has no errors in it, of course).

Preferred location for KBMAP configuration files is `~/.config/kbmap/`.

### Documentation
Documentation and useful resources can be found in [wiki](https://github.com/ivanjermakov/kbmap/wiki).