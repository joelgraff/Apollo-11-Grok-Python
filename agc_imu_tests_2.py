# agc_imu_tests_2.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUTests2:
    def __init__(self):
        self.memory = {
            "GYRO": 0,      # Gyro output (degrees/sec, scaled)
            "DRIFT": 0,     # Measured drift (degrees/sec)
            "TESTTIME": 0   # Test duration (centiseconds)
        }

    def drift_test(self, initial_gyro, test_time):
        """Simulate IMU drift test: Measure gyro stability."""
        store_to_memory("GYRO", mask_15bit(initial_gyro), self.memory)
        store_to_memory("TESTTIME", mask_15bit(test_time), self.memory)
        drift = mask_15bit(initial_gyro + 1)
        store_to_memory("DRIFT", drift, self.memory)
        return self.memory["DRIFT"]

    def main(self):
        """Sanity check for AGCIMUTests2."""
        print(f"Initial: GYRO={self.memory['GYRO']}, DRIFT={self.memory['DRIFT']}, TESTTIME={self.memory['TESTTIME']}")
        drift = self.drift_test(10, 100)
        print(f"Drift Test: GYRO={self.memory['GYRO']}, DRIFT={drift}, TESTTIME={self.memory['TESTTIME']}")

if __name__ == "__main__":
    imu_tests_2 = AGCIMUTests2()
    imu_tests_2.main()