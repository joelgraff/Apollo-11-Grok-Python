
# agc_averageg.py
from agc_utils import (
    mask_15bit, store_to_memory, fetch_double_precision,
    double_precision_add, double_precision_accumulate
)

class AGCAverageG:
    def __init__(self):
        self.memory = {
            "GDT": (0, 0),  # Accumulated gravity (double-precision)
            "COUNT": 0      # Number of samples
        }

    def reset(self):
        """Reset accumulator."""
        self.memory["GDT"] = (0, 0)
        store_to_memory("COUNT", 0, self.memory)

    def accumulate(self, g_high, g_low):
        """Add a gravity sample to the accumulator."""
        acc_high, acc_low = self.memory["GDT"]
        acc_high, acc_low = double_precision_accumulate(acc_high, acc_low, g_high, g_low)
        self.memory["GDT"] = (acc_high, acc_low)
        store_to_memory("COUNT", self.memory["COUNT"] + 1, self.memory)
        return acc_high, acc_low

    def average(self):
        """Compute average gravity (simplified division)."""
        if self.memory["COUNT"] == 0:
            return 0, 0
        high, low = self.memory["GDT"]
        # AGC divides by shifting; here we use integer division
        avg_high, avg_low = high // self.memory["COUNT"], low // self.memory["COUNT"]
        return mask_15bit(avg_high), mask_15bit(avg_low)

    def main(self):
        """Sanity check for AGCAverageG."""
        self.reset()
        print(f"Initial GDT: {self.memory['GDT']}, Count: {self.memory['COUNT']}")
        # Accumulate some samples
        self.accumulate(0, 100)
        self.accumulate(0, 200)
        self.accumulate(0, 300)
        print(f"Accumulated GDT: {self.memory['GDT']}, Count: {self.memory['COUNT']}")
        avg_high, avg_low = self.average()
        print(f"Average GDT: {avg_high}, {avg_low}")  # Should be ~0, 200

if __name__ == "__main__":
    avg_g = AGCAverageG()
    avg_g.main()