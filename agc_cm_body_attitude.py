# agc_cm_body_attitude.py
from agc_utils import mask_15bit, store_to_memory

class AGCCMBodyAttitude:
    def __init__(self):
        self.memory = {
            "ROLL": 0,    # Roll angle (degrees, scaled)
            "PITCH": 0    # Pitch angle (degrees, scaled)
        }

    def set_attitude(self, roll, pitch):
        """Set CM body attitude."""
        store_to_memory("ROLL", mask_15bit(roll), self.memory)
        store_to_memory("PITCH", mask_15bit(pitch), self.memory)
        return self.memory["ROLL"], self.memory["PITCH"]

    def main(self):
        """Sanity check for AGCCMBodyAttitude."""
        print(f"Initial: ROLL={self.memory['ROLL']}, PITCH={self.memory['PITCH']}")
        roll, pitch = self.set_attitude(15, 30)
        print(f"Attitude: ROLL={roll}, PITCH={pitch}")

if __name__ == "__main__":
    body = AGCCMBodyAttitude()
    body.main()