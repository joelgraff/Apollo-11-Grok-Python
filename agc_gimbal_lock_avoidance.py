# agc_gimbal_lock_avoidance.py
from agc_utils import mask_15bit, store_to_memory

class AGCGimbalLockAvoidance:
    def __init__(self):
        self.memory = {
            "GIMBAL_ANGLE": 0,   # Current gimbal angle (degrees, scaled)
            "SAFE_ANGLE": 0      # Adjusted safe angle (degrees, scaled)
        }

    def avoid_lock(self, angle):
        """Simulate gimbal lock avoidance."""
        store_to_memory("GIMBAL_ANGLE", mask_15bit(angle), self.memory)
        # Simplified: limit angle to avoid lock (e.g., < 85°)
        safe = mask_15bit(min(angle, 85))
        store_to_memory("SAFE_ANGLE", safe, self.memory)
        return safe

    def main(self):
        """Sanity check for AGCGimbalLockAvoidance."""
        print(f"Initial: GIMBAL_ANGLE={self.memory['GIMBAL_ANGLE']}, SAFE_ANGLE={self.memory['SAFE_ANGLE']}")
        safe = self.avoid_lock(90)
        print(f"Avoided Lock: GIMBAL_ANGLE={self.memory['GIMBAL_ANGLE']}, SAFE_ANGLE={safe}")

if __name__ == "__main__":
    gimbal = AGCGimbalLockAvoidance()
    gimbal.main()