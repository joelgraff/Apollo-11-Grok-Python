# agc_landing_analog_displays.py
from agc_utils import mask_15bit, store_to_memory

class AGCLandingAnalogDisplays:
    def __init__(self):
        self.memory = {
            "ALTRATE": 0,   # Altitude rate (m/s, scaled)
            "DISPLAY": 0    # Analog display value
        }

    def update_display(self, alt_rate):
        """Simulate updating analog display with altitude rate."""
        store_to_memory("ALTRATE", mask_15bit(alt_rate), self.memory)
        # Simplified scaling for display (e.g., 1:1 mapping)
        display_val = mask_15bit(alt_rate)
        store_to_memory("DISPLAY", display_val, self.memory)
        return display_val

    def main(self):
        """Sanity check for AGCLandingAnalogDisplays."""
        print(f"Initial: ALTRATE={self.memory['ALTRATE']}, DISPLAY={self.memory['DISPLAY']}")
        disp = self.update_display(50)  # 50 m/s altitude rate
        print(f"Display Update: ALTRATE={self.memory['ALTRATE']}, DISPLAY={disp}")

if __name__ == "__main__":
    landing_analog_displays = AGCLandingAnalogDisplays()
    landing_analog_displays.main()