# agc_display_interface_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCDisplayInterfaceRoutines:
    def __init__(self):
        self.memory = {
            "DISP_DATA": 0,   # Data to display (scaled)
            "DISP_FLAG": 0    # Display flag (0=off, 1=on)
        }

    def display_value(self, data):
        """Simulate displaying a value on DSKY."""
        store_to_memory("DISP_DATA", mask_15bit(data), self.memory)
        store_to_memory("DISP_FLAG", 1, self.memory)
        return self.memory["DISP_DATA"]

    def main(self):
        """Sanity check for AGCDisplayInterfaceRoutines."""
        print(f"Initial: DISP_DATA={self.memory['DISP_DATA']}, DISP_FLAG={self.memory['DISP_FLAG']}")
        data = self.display_value(1234)
        print(f"Displayed: DISP_DATA={data}, DISP_FLAG={self.memory['DISP_FLAG']}")

if __name__ == "__main__":
    display = AGCDisplayInterfaceRoutines()
    display.main()