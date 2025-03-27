# agc_trim_gimbal.py
from agc_utils import mask_15bit, store_to_memory

class AGCTrimGimbal:
    def __init__(self):
        self.memory = {
            "GIMBAL": 0,     # Current gimbal angle (degrees, scaled)
            "TRIM": 0,       # Trim correction (degrees)
            "ADJUSTED": 0    # Adjusted gimbal angle
        }

    def trim_gimbal(self, current_angle, trim_correction):
        """Simulate trim gimbal adjustment."""
        store_to_memory("GIMBAL", mask_15bit(current_angle), self.memory)
        store_to_memory("TRIM", mask_15bit(trim_correction), self.memory)
        adjusted = mask_15bit(current_angle + trim_correction)
        store_to_memory("ADJUSTED", adjusted, self.memory)
        return adjusted

    def main(self):
        """Sanity check for AGCTrimGimbal."""
        print(f"Initial: GIMBAL={self.memory['GIMBAL']}, TRIM={self.memory['TRIM']}, ADJUSTED={self.memory['ADJUSTED']}")
        angle = self.trim_gimbal(30, 5)  # 30 deg + 5 deg trim
        print(f"Trim Adjust: GIMBAL={self.memory['GIMBAL']}, TRIM={self.memory['TRIM']}, ADJUSTED={angle}")

if __name__ == "__main__":
    trim_gimbal = AGCTrimGimbal()
    trim_gimbal.main()