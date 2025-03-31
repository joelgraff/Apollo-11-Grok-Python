# agc_p51_p53.py
from agc_utils import mask_15bit, store_to_memory

class AGCP51P53:
    def __init__(self):
        self.memory = {
            "P51_ANGLE": 0,   # IMU alignment angle (degrees, scaled)
            "P51_STATE": 0    # Program state (0=off, 1=on)
        }

    def run_p51_p53(self, angle):
        """Simulate P51-P53 IMU alignment."""
        store_to_memory("P51_ANGLE", mask_15bit(angle), self.memory)
        store_to_memory("P51_STATE", 1, self.memory)
        return self.memory["P51_ANGLE"]

    def main(self):
        """Sanity check for AGCP51P53."""
        print(f"Initial: P51_ANGLE={self.memory['P51_ANGLE']}, P51_STATE={self.memory['P51_STATE']}")
        angle = self.run_p51_p53(45)
        print(f"P51-P53 Ran: P51_ANGLE={angle}, P51_STATE={self.memory['P51_STATE']}")

if __name__ == "__main__":
    p51p53 = AGCP51P53()
    p51p53.main()