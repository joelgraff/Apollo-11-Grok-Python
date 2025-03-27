# agc_imu_tests.py
from agc_utils import (
    mask_15bit, store_to_memory, double_precision_add,
    double_precision_subtract, error_magnitude
)

class AGCIMUTests:
    def __init__(self):
        self.memory = {
            "GYROX": (0, 0),    # Measured gyro value
            "GYROEXP": (0, 0),  # Expected gyro value
            "ERROR": (0, 0)     # Error result
        }

    def set_gyro_data(self, measured_high, measured_low, expected_high, expected_low):
        """Set measured and expected gyro values."""
        self.memory["GYROX"] = (mask_15bit(measured_high), mask_15bit(measured_low))
        self.memory["GYROEXP"] = (mask_15bit(expected_high), mask_15bit(expected_low))

    def check_alignment(self):
        """Check gyro alignment by comparing measured vs expected."""
        gyro_high, gyro_low = self.memory["GYROX"]
        exp_high, exp_low = self.memory["GYROEXP"]
        error_high, error_low = error_magnitude(gyro_high, gyro_low, exp_high, exp_low)
        self.memory["ERROR"] = (error_high, error_low)
        return error_high, error_low

    def main(self):
        """Sanity check for AGCIMUTests."""
        # Simulate gyro data: measured 1000, expected 950
        self.set_gyro_data(0, 1000, 0, 950)
        print(f"Measured GYROX: {self.memory['GYROX']}, Expected: {self.memory['GYROEXP']}")
        error_high, error_low = self.check_alignment()
        print(f"Alignment Error: {error_high}, {error_low}")  # Should be 0, 50

if __name__ == "__main__":
    imu_tests = AGCIMUTests()
    imu_tests.main()