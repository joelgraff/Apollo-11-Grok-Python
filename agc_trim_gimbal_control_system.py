# agc_trim_gimbal_control_system.py
from agc_utils import mask_15bit, store_to_memory

class AGCTrimGimbalControlSystem:
    def __init__(self):
        self.memory = {
            "GIMBAL_ANGLE": 0,   # Gimbal angle (degrees, scaled)
            "TRIM_CMD": 0        # Trim command (scaled)
        }

    def trim_gimbal(self, angle):
        """Simulate trim gimbal control."""
        store_to_memory("GIMBAL_ANGLE", mask_15bit(angle), self.memory)
        cmd = mask_15bit(angle * 2)  # Simplified trim adjustment
        store_to_memory("TRIM_CMD", cmd, self.memory)
        return cmd

    def main(self):
        """Sanity check for AGCTrimGimbalControlSystem."""
        print(f"Initial: GIMBAL_ANGLE={self.memory['GIMBAL_ANGLE']}, TRIM_CMD={self.memory['TRIM_CMD']}")
        cmd = self.trim_gimbal(10)
        print(f"Gimbal Trimmed: GIMBAL_ANGLE={self.memory['GIMBAL_ANGLE']}, TRIM_CMD={cmd}")

if __name__ == "__main__":
    trim_gimbal = AGCTrimGimbalControlSystem()
    trim_gimbal.main()