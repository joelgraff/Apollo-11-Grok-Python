# agc_radar_test.py
from agc_utils import mask_15bit, store_to_memory

class AGCRadarTest:
    def __init__(self):
        self.memory = {
            "RANGE": 0,     # Radar range (meters, scaled)
            "TESTOK": 0     # Test result (0=fail, 1=pass)
        }

    def radar_test(self, measured_range):
        """Simulate radar test: Check range measurement."""
        store_to_memory("RANGE", mask_15bit(measured_range), self.memory)
        # Pass if range is positive and reasonable (< 32768 for 15-bit)
        test_result = 1 if 0 < measured_range < 32768 else 0
        store_to_memory("TESTOK", test_result, self.memory)
        return self.memory["TESTOK"]

    def main(self):
        """Sanity check for AGCRadarTest."""
        print(f"Initial: RANGE={self.memory['RANGE']}, TESTOK={self.memory['TESTOK']}")
        result = self.radar_test(5000)
        print(f"Radar Test: RANGE={self.memory['RANGE']}, TESTOK={result}")

if __name__ == "__main__":
    radar_test = AGCRadarTest()
    radar_test.main()