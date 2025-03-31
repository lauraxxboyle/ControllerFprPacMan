import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from sensorlightdisplay import SensorLightDisplay  # your class
from lightdisplay import LightDisplay  # make sure this is also on CIRCUITPY

# Define a color to use for direction feedback (e.g., yellow)
DIRECTION_COLOR = (255, 150, 0)

# Setup keyboard HID and sensor display
keyboard = Keyboard(usb_hid.devices)
sensor = SensorLightDisplay(brightness=0.2)

last_direction = None

while True:
    if sensor.accelerometer is None:
        continue  # Skip if accelerometer failed to initialize

    x, y, _ = sensor.accelerometer.acceleration
    sensor.advanced_control_feedback(y)



    direction = None
    key = None

    # Movement detection based on x and y values
    if x < -3 and x < y:
        direction = "LEFT"
        key = Keycode.LEFT_ARROW
    elif x > 3 and x > y:
        direction = "RIGHT"
        key = Keycode.RIGHT_ARROW
    elif y > 3 and y > x:
        direction = "UP"
        key = Keycode.UP_ARROW
    elif y < -3 and y < x:
        direction = "DOWN"
        key = Keycode.DOWN_ARROW

    # Show direction feedback using your class
    sensor.light(DIRECTION_COLOR)

    # Only send key if direction changed
    if direction and direction != last_direction:
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release_all()
        last_direction = direction
    elif direction is None:
        last_direction = None

        



    time.sleep(0.1)


