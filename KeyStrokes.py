import keyboard
import datetime

def main():
    print("Keystroke Logger (Safe Version with Timestamp)")
    print("Logs keys only while this window is active.")
    print("Press ESC to stop.\n")

    with open("key_log.txt", "a") as log:
        log.write("\n--- Logging started at "
                  + str(datetime.datetime.now()) + " ---\n")

        while True:
            event = keyboard.read_event()

            if event.event_type == "down":
                # Current timestamp
                ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Log entry
                entry = f"{ts} - {event.name}\n"

                log.write(entry)
                log.flush()

                print(entry, end="")

            if event.name == "esc" and event.event_type == "down":
                print("Stopping logger...")
                break

if __name__ == "__main__":
    main()
