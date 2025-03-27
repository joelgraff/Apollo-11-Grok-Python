# agc_imu_fine_align.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUFineAlign:
    def __init__(self):
        self.memory = {
            "IMUANGLE": 0,   # Current IMU angle (degrees, scaled)
            "CORRECTION": 0, # Fine correction (degrees)
            "ALIGNDONE": 0   # Alignment status (0=pending, 1=done)
        }

    def fine_align(self, current_angle, correction):
        """Simulate IMU fine alignment."""
        store_to_memory("IMUANGLE", mask_15bit(current_angle), self.memory)
        store_to_memory("CORRECTION", mask_15bit(correction), self.memory)
        new_angle = mask_15bit(current_angle + correction)
        store_to_memory("IMUANGLE", new_angle, self.memory)
        store_to_memory("ALIGNDONE", 1, self.memory)
        return new_angle

    def main(self):
        """Sanity check for AGCIMUFineAlign."""
        print(f"Initial: IMUANGLE={self.memory['IMUANGLE']}, CORRECTION={self.memory['CORRECTION']}, ALIGNDONE={self.memory['ALIGNDONE']}")
        angle = self.fine_align(45, 1)  # 45 deg + 1 deg correction
        print(f"Fine Align: IMUANGLE={angle}, CORRECTION={self.memory['CORRECTION']}, ALIGNDONE={self.memory['ALIGNDONE']}")

if __name__ == "__main__":
    imu_fine_align = AGCIMUFineAlign()
    imu_fine_align.main()