# agc_imu_performance_tests_3.py
from agc_utils import mask_15bit, store_to_memory

class AGCIMUPerformanceTests3:
    def __init__(self):
        self.memory = {
            "IMU_DRIFT": 0,   # IMU drift (degrees, scaled)
            "DRIFT_OK": 0     # Drift test result (0=fail, 1=pass)
        }

    def test_imu_drift(self, drift):
        """Simulate IMU performance test 3."""
        store_to_memory("IMU_DRIFT", mask_15bit(drift), self.memory)
        ok_flag = 1 if drift < 5 else 0  # Simplified drift threshold
        store_to_memory("DRIFT_OK", ok_flag, self.memory)
        return ok_flag

    def main(self):
        """Sanity check for AGCIMUPerformanceTests3."""
        print(f"Initial: IMU_DRIFT={self.memory['IMU_DRIFT']}, DRIFT_OK={self.memory['DRIFT_OK']}")
        result = self.test_imu_drift(3)
        print(f"IMU Test 3: IMU_DRIFT={self.memory['IMU_DRIFT']}, DRIFT_OK={result}")

if __name__ == "__main__":
    imu_test3 = AGCIMUPerformanceTests3()
    imu_test3.main()