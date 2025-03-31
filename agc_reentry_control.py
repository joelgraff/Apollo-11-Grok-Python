# agc_reentry_control.py
from agc_utils import mask_15bit, store_to_memory

class AGCReentryControl:
    def __init__(self):
        self.memory = {
            "ROLL": 0,       # Roll angle (degrees, scaled)
            "ROLLCMD": 0,    # Commanded roll angle
            "ACTIVE": 0      # Control active (0=off, 1=on)
        }

    def adjust_roll(self, current_roll, target_roll):
        """Simulate reentry roll adjustment."""
        store_to_memory("ROLL", mask_15bit(current_roll), self.memory)
        store_to_memory("ROLLCMD", mask_15bit(target_roll), self.memory)
        new_roll = mask_15bit(target_roll)
        store_to_memory("ROLL", new_roll, self.memory)
        store_to_memory("ACTIVE", 1, self.memory)
        return new_roll

    def main(self):
        """Sanity check for AGCReentryControl."""
        print(f"Initial: ROLL={self.memory['ROLL']}, ROLLCMD={self.memory['ROLLCMD']}, ACTIVE={self.memory['ACTIVE']}")
        roll = self.adjust_roll(10, 15)  # 10 deg to 15 deg
        print(f"Roll Adjust: ROLL={roll}, ROLLCMD={self.memory['ROLLCMD']}, ACTIVE={self.memory['ACTIVE']}")

if __name__ == "__main__":
    reentry_control = AGCReentryControl()
    reentry_control.main()