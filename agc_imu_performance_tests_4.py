# agc_imu_performance_tests_4.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUPerformanceTests4:
    def __init__(self):
        self.memory = {
            "IMU_ERROR": 0,   # IMU error value (degrees, scaled)
            "TEST_OK": 0      # Test result (0=fail, 1=pass)
        }

    def test_imu_error(self, error):
        """Simulate IMU performance test 4."""
        store_to_memory("IMU_ERROR", mask_15bit(error), self.memory)
        ok_flag = 1 if error < 10 else 0  # Simplified error threshold
        store_to_memory("TEST_OK", ok_flag, self.memory)
        return ok_flag

    def main(self):
        """Sanity check for AGCIMUPerformanceTests4."""
        print(f"Initial: IMU_ERROR={self.memory['IMU_ERROR']}, TEST_OK={self.memory['TEST_OK']}")
        result = self.test_imu_error(7)
        print(f"IMU Test 4: IMU_ERROR={self.memory['IMU_ERROR']}, TEST_OK={result}")

if __name__ == "__main__":
    imu_test4 = AGCIMUPerformanceTests4()
    imu_test4.main()