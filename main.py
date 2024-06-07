import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_circuitplayground import cp

# Set up the NeoPixels
cp.pixels.brightness = 0.2

# Set up the buttons
button_a = DigitalInOut(board.BUTTON_A)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN

button_b = DigitalInOut(board.BUTTON_B)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN

# Set up double-tap detection
cp.detect_taps = 2

# Blinker states
left_blinker_on = False
right_blinker_on = False
hazard_lights_on = False
red_blink_state = False
left_blinker_state = False
right_blinker_state = False
hazard_light_state = False

def set_blinkers():
    if hazard_lights_on:
        color = (255, 165, 0) if hazard_light_state else (0, 0, 0)
        for i in range(10):
            cp.pixels[i] = color
    elif left_blinker_on and left_blinker_state:
        cp.pixels[1] = (255, 165, 0)  # Orange color for the left blinker
        cp.pixels[2] = (255, 165, 0)
        cp.pixels[8] = (0, 0, 0)  # Ensure right blinker is off
        cp.pixels[9] = (0, 0, 0)
    elif right_blinker_on and right_blinker_state:
        cp.pixels[8] = (255, 165, 0)  # Orange color for the right blinker
        cp.pixels[9] = (255, 165, 0)
        cp.pixels[1] = (0, 0, 0)  # Ensure left blinker is off
        cp.pixels[2] = (0, 0, 0)
    elif cp.switch:
        color = (255, 0, 0) if red_blink_state else (0, 0, 0)
        for i in range(10):
            cp.pixels[i] = color
    else:
        for i in range(10):
            cp.pixels[i] = (0, 0, 0)  # Ensure all other pixels are off
    cp.pixels.show()

blink_time = time.monotonic()
prev_switch_state = cp.switch

while True:
    if cp.tapped:
        hazard_lights_on = not hazard_lights_on
        if hazard_lights_on:
            left_blinker_on = False
            right_blinker_on = False
            left_blinker_state = False
            right_blinker_state = False
        hazard_light_state = False
        set_blinkers()
        time.sleep(0.2)  # Debounce delay

    if button_a.value:
        left_blinker_on = not left_blinker_on
        if left_blinker_on:
            right_blinker_on = False
            right_blinker_state = False
            hazard_lights_on = False
        left_blinker_state = False
        set_blinkers()
        time.sleep(0.2)  # Debounce delay

    if button_b.value:
        right_blinker_on = not right_blinker_on
        if right_blinker_on:
            left_blinker_on = False
            left_blinker_state = False
            hazard_lights_on = False
        right_blinker_state = False
        set_blinkers()
        time.sleep(0.2)  # Debounce delay
    
    current_time = time.monotonic()
    if current_time - blink_time >= 0.5:  # Half-second toggle
        blink_time = current_time
        if hazard_lights_on:
            hazard_light_state = not hazard_light_state
        elif left_blinker_on:
            left_blinker_state = not left_blinker_state
        elif right_blinker_on:
            right_blinker_state = not right_blinker_state
        elif cp.switch:
            red_blink_state = not red_blink_state
        set_blinkers()
    
    # Check if the switch state has changed
    if prev_switch_state != cp.switch:
        if not cp.switch:  # If the switch was turned off
            for i in range(10):
                cp.pixels[i] = (0, 0, 0)  # Turn off all lights
            cp.pixels.show()
        prev_switch_state = cp.switch
    
    time.sleep(0.1)
