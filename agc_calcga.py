# agc_calcga.py
from agc_utils import mask_15bit, store_to_memory

class AGCCalcGA:
    def __init__(self):
        self.memory = {
            "GA_ANGLE": 0,   # Gimbal angle (degrees, scaled)
            "INPUT_ATT": 0   # Input attitude (degrees, scaled)
        }

    def calc_gimbal_angle(self, attitude):
        """Calculate gimbal angle from attitude."""
        store_to_memory("INPUT_ATT", mask_15bit(attitude), self.memory)
        # Simplified: gimbal angle is a direct offset
        ga = mask_15bit(attitude + 10)  # Arbitrary offset
        store_to_memory("GA_ANGLE", ga, self.memory)
        return ga

    def main(self):
        """Sanity check for AGCCalcGA."""
        print(f"Initial: GA_ANGLE={self.memory['GA_ANGLE']}, INPUT_ATT={self.memory['INPUT_ATT']}")
        angle = self.calc_gimbal_angle(30)
        print(f"Calculated: GA_ANGLE={angle}, INPUT_ATT={self.memory['INPUT_ATT']}")

if __name__ == "__main__":
    calcga = AGCCalcGA()
    calcga.main()