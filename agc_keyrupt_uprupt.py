# agc_keyrupt_uprupt.py
from agc_utils import mask_15bit, store_to_memory

class AGCKeyruptUprupt:
    def __init__(self):
        self.memory = {
            "KEYCODE": 0,    # Key code from DSKY
            "INTTIME": 0,    # Interrupt time (centiseconds)
            "STATE": 0       # Interrupt state (0=idle, 1=active)
        }

    def keyrupt(self, time, key_code):
        """Simulate KEYRUPT: Process a DSKY keypress."""
        # Update interrupt time
        store_to_memory("INTTIME", mask_15bit(time), self.memory)
        # Store key code (e.g., 1-9, V, N)
        store_to_memory("KEYCODE", mask_15bit(key_code), self.memory)
        # Mark interrupt active
        store_to_memory("STATE", 1, self.memory)
        return self.memory["KEYCODE"]

    def main(self):
        """Sanity check for AGCKeyruptUprupt."""
        print(f"Initial: KEYCODE={self.memory['KEYCODE']}, INTTIME={self.memory['INTTIME']}, STATE={self.memory['STATE']}")
        # Simulate KEYRUPT with key code 5 (e.g., digit 5) at 50cs
        key = self.keyrupt(50, 5)
        print(f"KEYRUPT: KEYCODE={key}, INTTIME={self.memory['INTTIME']}, STATE={self.memory['STATE']}")

if __name__ == "__main__":
    keyrupt_uprupt = AGCKeyruptUprupt()
    keyrupt_uprupt.main()