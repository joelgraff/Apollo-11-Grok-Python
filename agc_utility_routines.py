# agc_utility_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCUtilityRoutines:
    def __init__(self):
        self.memory = {
            "INPUT": 0,   # Input value
            "OUTPUT": 0   # Processed output
        }

    def shift_right(self, value):
        """Simulate a right shift utility routine."""
        store_to_memory("INPUT", mask_15bit(value), self.memory)
        shifted = mask_15bit(value >> 1)
        store_to_memory("OUTPUT", shifted, self.memory)
        return shifted

    def main(self):
        """Sanity check for AGCUtilityRoutines."""
        print(f"Initial: INPUT={self.memory['INPUT']}, OUTPUT={self.memory['OUTPUT']}")
        result = self.shift_right(100)
        print(f"Shifted: INPUT={self.memory['INPUT']}, OUTPUT={result}")

if __name__ == "__main__":
    utils = AGCUtilityRoutines()
    utils.main()