# agc_pinball_game_buttons_and_lights.py
from agc_utils import mask_15bit, store_to_memory

class AGCPinballGameButtonsAndLights:
    def __init__(self):
        self.memory = {
            "BUTTON": 0,    # Button input (e.g., verb key, scaled)
            "LIGHT": 0      # Light status (0=off, 1=on)
        }

    def press_button(self, button_code):
        """Simulate button press and light toggle."""
        store_to_memory("BUTTON", mask_15bit(button_code), self.memory)
        store_to_memory("LIGHT", 1, self.memory)
        return self.memory["BUTTON"]

    def main(self):
        """Sanity check for AGCPinballGameButtonsAndLights."""
        print(f"Initial: BUTTON={self.memory['BUTTON']}, LIGHT={self.memory['LIGHT']}")
        button = self.press_button(5)  # Simulate verb key press
        print(f"Button Pressed: BUTTON={button}, LIGHT={self.memory['LIGHT']}")

if __name__ == "__main__":
    pinball = AGCPinballGameButtonsAndLights()
    pinball.main()