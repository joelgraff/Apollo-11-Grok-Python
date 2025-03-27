# agc_p20_p25_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCP20P25Subroutines:
    def __init__(self):
        self.memory = {
            "RANGE1": 0,     # First range measurement (meters, scaled)
            "RANGE2": 0,     # Second range measurement
            "RANGEDIFF": 0   # Range difference
        }

    def range_diff(self, range1, range2):
        """Simulate range difference calculation for P20-P25."""
        store_to_memory("RANGE1", mask_15bit(range1), self.memory)
        store_to_memory("RANGE2", mask_15bit(range2), self.memory)
        diff = mask_15bit(range1 - range2)
        store_to_memory("RANGEDIFF", diff, self.memory)
        return diff

    def main(self):
        """Sanity check for AGCP20P25Subroutines."""
        print(f"Initial: RANGE1={self.memory['RANGE1']}, RANGE2={self.memory['RANGE2']}, RANGEDIFF={self.memory['RANGEDIFF']}")
        diff = self.range_diff(2000, 1800)  # 2000m - 1800m
        print(f"Range Diff: RANGE1={self.memory['RANGE1']}, RANGE2={self.memory['RANGE2']}, RANGEDIFF={diff}")

if __name__ == "__main__":
    p20_p25_subroutines = AGCP20P25Subroutines()
    p20_p25_subroutines.main()