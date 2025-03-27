# agc_imu_calib_align.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUCalibAlign:
    def __init__(self):
        self.memory = {
            "GYROBIAS": 0,  # Gyro bias (degrees/sec, scaled)
            "ALIGNANG": 0,  # Alignment angle (degrees)
            "CALIB": 0      # Calibration status (0=pending, 1=done)
        }

    def coarse_align(self, bias, target_angle):
        """Simulate IMU coarse alignment."""
        store_to_memory("GYROBIAS", mask_15bit(bias), self.memory)
        adjusted_angle = mask_15bit(target_angle - bias)
        store_to_memory("ALIGNANG", adjusted_angle, self.memory)
        store_to_memory("CALIB", 1, self.memory)
        return adjusted_angle

    def main(self):
        """Sanity check for AGCIMUCalibAlign."""
        print(f"Initial: GYROBIAS={self.memory['GYROBIAS']}, ALIGNANG={self.memory['ALIGNANG']}, CALIB={self.memory['CALIB']}")
        angle = self.coarse_align(2, 45)  # Bias 2 deg/sec, target 45 deg
        print(f"Coarse Align: GYROBIAS={self.memory['GYROBIAS']}, ALIGNANG={angle}, CALIB={self.memory['CALIB']}")

if __name__ == "__main__":
    imu_calib_align = AGCIMUCalibAlign()
    imu_calib_align.main()