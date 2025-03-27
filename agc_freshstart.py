# agc_freshstart.py
from agc_utils import mask_15bit, store_to_memory

class AGCFreshStart:
    def __init__(self):
        self.memory = {
            "A": 0,       # Accumulator
            "Q": 0,       # Quotient register
            "Z": 0,       # Program counter
            "EBANK": 0,   # Erasable bank register
            "FLAGS": 0    # General flags
        }

    def fresh_start(self):
        """Perform a full system reset."""
        # Reset key registers to zero
        store_to_memory("A", 0, self.memory)
        store_to_memory("Q", 0, self.memory)
        store_to_memory("Z", 1, self.memory)  # Z = 1 to point to initial instruction
        store_to_memory("EBANK", 0, self.memory)
        store_to_memory("FLAGS", 0, self.memory)
        return True  # Indicate completion

    def set_state(self, a, q, z, ebank, flags):
        """Set arbitrary state for testing."""
        store_to_memory("A", a, self.memory)
        store_to_memory("Q", q, self.memory)
        store_to_memory("Z", z, self.memory)
        store_to_memory("EBANK", ebank, self.memory)
        store_to_memory("FLAGS", flags, self.memory)

    def main(self):
        """Sanity check for AGCFreshStart."""
        # Set some non-zero state
        self.set_state(100, 200, 300, 1, 0xFF)
        print(f"Before: A={self.memory['A']}, Q={self.memory['Q']}, Z={self.memory['Z']}, EBANK={self.memory['EBANK']}, FLAGS={self.memory['FLAGS']}")
        # Perform fresh start
        self.fresh_start()
        print(f"After: A={self.memory['A']}, Q={self.memory['Q']}, Z={self.memory['Z']}, EBANK={self.memory['EBANK']}, FLAGS={self.memory['FLAGS']}")

if __name__ == "__main__":
    freshstart = AGCFreshStart()
    freshstart.main()