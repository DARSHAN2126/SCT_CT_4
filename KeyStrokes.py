# Safe example: captures keys only inside the program window (not a keylogger)

import keyboard

print("Type something (Ctrl+C to stop):")

with open("input_log.txt", "a") as f:
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":   # key press only
            f.write(event.name + "\n")
            f.flush()
            print("You pressed:", event.name)
