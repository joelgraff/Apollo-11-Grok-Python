# agc_imu_performance_tests_1.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUPerformanceTests1:
    def __init__(self):
        self.memory = {
            "IMU_VAL": 0,    # IMU test value (degrees, scaled)
            "TEST_PASS": 0   # Test pass flag (0=fail, 1=pass)
        }

    def test_imu(self, value):
        """Simulate IMU performance test 1."""
        store_to_memory("IMU_VAL", mask_15bit(value), self.memory)
        pass_flag = 1 if value < 100 else 0  # Simplified threshold
        store_to_memory("TEST_PASS", pass_flag, self.memory)
        return pass_flag

    def main(self):
        """Sanity check for AGCIMUPerformanceTests1."""
        print(f"Initial: IMU_VAL={self.memory['IMU_VAL']}, TEST_PASS={self.memory['TEST_PASS']}")
        result = self.test_imu(75)
        print(f"IMU Test 1: IMU_VAL={self.memory['IMU_VAL']}, TEST_PASS={result}")

if __name__ == "__main__":
    imu_test1 = AGCIMUPerformanceTests1()
    imu_test1.main()