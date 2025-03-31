# agc_find_cdu_desired.py
from agc_utils import mask_15bit, store_to_memory

class AGCFindCDUDesired:
    def __init__(self):
        self.memory = {
            "CURRENT_CDU": 0,   # Current CDU angle (degrees, scaled)
            "DESIRED_CDU": 0    # Desired CDU angle (degrees, scaled)
        }

    def find_desired(self, current, target):
        """Simulate finding desired CDU angle."""
        store_to_memory("CURRENT_CDU", mask_15bit(current), self.memory)
        desired = mask_15bit(target)  # Simplified: direct assignment
        store_to_memory("DESIRED_CDU", desired, self.memory)
        return desired

    def main(self):
        """Sanity check for AGCFindCDUDesired."""
        print(f"Initial: CURRENT_CDU={self.memory['CURRENT_CDU']}, DESIRED_CDU={self.memory['DESIRED_CDU']}")
        desired = self.find_desired(30, 45)
        print(f"Desired CDU: CURRENT_CDU={self.memory['CURRENT_CDU']}, DESIRED_CDU={desired}")

if __name__ == "__main__":
    cdu = AGCFindCDUDesired()
    cdu.main()