# agc_throttle_control_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCThrottleControlRoutines:
    def __init__(self):
        self.memory = {
            "THROT_VAL": 0,   # Throttle value (percent, scaled)
            "THROT_CMD": 0    # Throttle command (scaled)
        }

    def set_throttle(self, value):
        """Simulate throttle control."""
        store_to_memory("THROT_VAL", mask_15bit(value), self.memory)
        cmd = mask_15bit(value * 10)  # Simplified scaling
        store_to_memory("THROT_CMD", cmd, self.memory)
        return cmd

    def main(self):
        """Sanity check for AGCThrottleControlRoutines."""
        print(f"Initial: THROT_VAL={self.memory['THROT_VAL']}, THROT_CMD={self.memory['THROT_CMD']}")
        cmd = self.set_throttle(75)
        print(f"Throttle Set: THROT_VAL={self.memory['THROT_VAL']}, THROT_CMD={cmd}")

if __name__ == "__main__":
    throttle = AGCThrottleControlRoutines()
    throttle.main()