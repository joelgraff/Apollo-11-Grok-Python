# agc_vhf_ranging.py
from agc_utils import mask_15bit, store_to_memory

class AGCVHFRanging:
    def __init__(self):
        self.memory = {
            "RANGE": 0,   # Measured range (meters, scaled)
            "SIGNAL": 0   # VHF signal strength
        }

    def update_range(self, signal):
        """Update range based on VHF signal."""
        store_to_memory("SIGNAL", mask_15bit(signal), self.memory)
        range_val = mask_15bit(signal * 10)  # Simplified scaling
        store_to_memory("RANGE", range_val, self.memory)
        return range_val

    def main(self):
        """Sanity check for AGCVHFRanging."""
        print(f"Initial: RANGE={self.memory['RANGE']}, SIGNAL={self.memory['SIGNAL']}")
        range_val = self.update_range(200)
        print(f"Ranging: RANGE={range_val}, SIGNAL={self.memory['SIGNAL']}")

if __name__ == "__main__":
    vhf = AGCVHFRanging()
    vhf.main()