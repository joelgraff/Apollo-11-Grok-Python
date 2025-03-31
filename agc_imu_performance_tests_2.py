# agc_imu_performance_tests_2.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUPerformanceTests2:
    def __init__(self):
        self.memory = {
            "IMU_RATE": 0,    # IMU rate (degrees/sec, scaled)
            "TEST_STAT": 0    # Test status (0=pending, 1=complete)
        }

    def test_imu_rate(self, rate):
        """Simulate IMU performance test 2."""
        store_to_memory("IMU_RATE", mask_15bit(rate), self.memory)
        store_to_memory("TEST_STAT", 1, self.memory)
        return self.memory["IMU_RATE"]

    def main(self):
        """Sanity check for AGCIMUPerformanceTests2."""
        print(f"Initial: IMU_RATE={self.memory['IMU_RATE']}, TEST_STAT={self.memory['TEST_STAT']}")
        rate = self.test_imu_rate(10)
        print(f"IMU Test 2: IMU_RATE={rate}, TEST_STAT={self.memory['TEST_STAT']}")

if __name__ == "__main__":
    imu_test2 = AGCIMUPerformanceTests2()
    imu_test2.main()