# agc_erasable.py
from agc_utils import mask_15bit, store_to_memory

class AGCErasable:
    def __init__(self):
        self.memory = {
            "A": 0,    # Accumulator (address 0)
            "L": 0,    # Lower accumulator (address 1)
            "Q": 0,    # Return address (address 2)
            "TEMP": 0  # Temporary storage
        }

    def assign_and_use(self, acc_value, low_value, ret_value):
        """Assign values to erasable memory and perform a simple operation."""
        # Assign values to A, L, Q
        store_to_memory("A", mask_15bit(acc_value), self.memory)
        store_to_memory("L", mask_15bit(low_value), self.memory)
        store_to_memory("Q", mask_15bit(ret_value), self.memory)

        # Simple operation: TEMP = A + L
        temp = mask_15bit(self.memory["A"] + self.memory["L"])
        store_to_memory("TEMP", temp, self.memory)
        return self.memory["TEMP"]

    def main(self):
        """Sanity check for AGCErasable."""
        print(f"Initial: A={self.memory['A']}, L={self.memory['L']}, Q={self.memory['Q']}, TEMP={self.memory['TEMP']}")
        # Assign values and compute TEMP
        result = self.assign_and_use(100, 200, 300)
        print(f"After Assignment: A={self.memory['A']}, L={self.memory['L']}, Q={self.memory['Q']}, TEMP={result}")

if __name__ == "__main__":
    erasable = AGCErasable()
    erasable.main()