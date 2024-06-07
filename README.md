# Circuit Playground Blinker and Hazard Light Controller

My son Aart wanted car lights for his bike and I'm obliging with a CPX.

This script controls the NeoPixels on an Adafruit Circuit Playground Express to simulate car lights including left and right blinkers, hazard lights, and a red blinking light mode activated by the slide switch. The script uses button inputs and tap detection to toggle the various light modes.

## Features

- **Left Blinker**: Activated by pressing button A. The left blinker lights up NeoPixels 1 and 2 in orange, blinking at half-second intervals.
- **Right Blinker**: Activated by pressing button B. The right blinker lights up NeoPixels 8 and 9 in orange, blinking at half-second intervals.
- **Hazard Lights**: Activated by double-tapping the Circuit Playground. All NeoPixels blink in orange at half-second intervals.
- **Red Blinking Light Mode**: Activated by the slide switch. All NeoPixels blink in red at half-second intervals. This mode has the lowest priority and will only activate if no other modes are active.
- **State Management**: Ensures that activating one mode will turn off all other modes, preventing conflicting light patterns.

## Usage

1. **Left Blinker**: Press button A to toggle the left blinker on and off.
2. **Right Blinker**: Press button B to toggle the right blinker on and off.
3. **Hazard Lights**: Double-tap the Circuit Playground to toggle the hazard lights on and off.
4. **Red Blinking Light Mode**: Slide the switch to the on position to activate the red blinking light mode. This will only activate if no other mode is active.

## Setup

1. Ensure you have the required libraries installed:
   - `adafruit_circuitplayground`
   - `board`
   - `digitalio`
   - `neopixel`

2. Upload the script to your Circuit Playground Express using your preferred method (e.g., copying the script to the CIRCUITPY drive).

3. Connect to your Circuit Playground and run the script.

## Code Explanation

The script initializes the NeoPixels and button inputs. It sets up double-tap detection using the `cp.detect_taps` attribute. The main loop handles button presses and double-tap detection to toggle the different light modes.

### Functions

- **set_blinkers()**: This function updates the NeoPixels based on the current state of the blinkers, hazard lights, and red blinking light mode. It ensures the correct priority of the light modes.
- **Main Loop**: The main loop checks for button presses and double-tap events, toggling the respective modes and calling `set_blinkers()` to update the NeoPixels. It also handles the timing for blinking the lights at half-second intervals.

### State Variables

- **left_blinker_on**: Indicates if the left blinker is active.
- **right_blinker_on**: Indicates if the right blinker is active.
- **hazard_lights_on**: Indicates if the hazard lights are active.
- **red_blink_state**: Indicates the current state of the red blinking light (on or off).
- **left_blinker_state**: Indicates the current state of the left blinker light (on or off).
- **right_blinker_state**: Indicates the current state of the right blinker light (on or off).
- **hazard_light_state**: Indicates the current state of the hazard light (on or off).

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for this project.

## License

This project is licensed under the MIT License.
