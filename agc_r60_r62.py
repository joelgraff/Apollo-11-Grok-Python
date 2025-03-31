# agc_r60_r62.py
from agc_utils import mask_15bit, store_to_memory

class AGCR60R62:
    def __init__(self):
        self.memory = {
            "ATT_ERROR": 0,   # Attitude error (degrees, scaled)
            "MANEUVER": 0     # Maneuver command (scaled)
        }

    def perform_maneuver(self, error):
        """Simulate R60/R62 attitude maneuver."""
        store_to_memory("ATT_ERROR", mask_15bit(error), self.memory)
        cmd = mask_15bit(error * 4)  # Simplified maneuver command
        store_to_memory("MANEUVER", cmd, self.memory)
        return cmd

    def main(self):
        """Sanity check for AGCR60R62."""
        print(f"Initial: ATT_ERROR={self.memory['ATT_ERROR']}, MANEUVER={self.memory['MANEUVER']}")
        cmd = self.perform_maneuver(15)
        print(f"Maneuver: ATT_ERROR={self.memory['ATT_ERROR']}, MANEUVER={cmd}")

if __name__ == "__main__":
    r60r62 = AGCR60R62()
    r60r62.main()