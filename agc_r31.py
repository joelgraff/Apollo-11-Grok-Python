# agc_r31.py
from agc_utils import mask_15bit, store_to_memory

class AGCR31:
    def __init__(self):
        self.memory = {
            "R31_VEL": 0,     # Velocity for R31 (m/s, scaled)
            "R31_RANGE": 0    # Range for R31 (meters, scaled)
        }

    def compute_r31(self, velocity):
        """Simulate R31 VHF ranging."""
        store_to_memory("R31_VEL", mask_15bit(velocity), self.memory)
        range_val = mask_15bit(velocity * 20)  # Simplified range calc
        store_to_memory("R31_RANGE", range_val, self.memory)
        return range_val

    def main(self):
        """Sanity check for AGCR31."""
        print(f"Initial: R31_VEL={self.memory['R31_VEL']}, R31_RANGE={self.memory['R31_RANGE']}")
        range_val = self.compute_r31(150)
        print(f"R31 Computed: R31_VEL={self.memory['R31_VEL']}, R31_RANGE={range_val}")

if __name__ == "__main__":
    r31 = AGCR31()
    r31.main()