# Keylogger Project
This is a simple keylogger implemented in Python using the `pynput` library. The keylogger captures key presses and writes them to a file named `keylogs.txt`.

## Features
- Logs key presses, including space, enter, backspace, tab, shift, ctrl, and alt.
- Writes key logs to a file named `keylogs.txt`.
- Stops logging when the escape key (`esc`) is pressed.

## Requirements
- Python 3.x
- `pynput` library

## Installation
1. Clone the repository:
    git clone https://github.com/Jokika11/Prasunet_CS_04.git

2. Install the required library:
    ```bash
    pip install pynput
    ```

## Usage
1. Run the keylogger script:
    ```bash
    python Simple_Keylogger.py
    ```
2. The keylogger will start capturing key presses and writing them to `keylogs.txt` in the same directory.
3. To stop the keylogger, press the escape key (`esc`).

## Key Mapping
The keylogger maps special keys to specific strings in the `keylogs.txt` file:
- Space: ` `
- Enter: `\n`
- Backspace: `<BACKSPACE>`
- Tab: `<TAB>`
- Shift: `<SHIFT>`
- Ctrl: `<CTRL>`
- Alt: `<ALT>`

## ⚠️Disclaimer⚠️
This keylogger is intended for educational purposes only. Unauthorized use of keylogging software can be illegal and unethical. Always obtain proper authorization before using a keylogger on any system.
