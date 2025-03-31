# agc_radar_test_programs.py
from agc_utils import mask_15bit, store_to_memory

class AGCRadarTestPrograms:
    def __init__(self):
        self.memory = {
            "RADAR_VAL": 0,   # Radar test value (scaled)
            "TEST_RES": 0     # Test result (0=fail, 1=pass)
        }

    def test_radar(self, value):
        """Simulate radar test program."""
        store_to_memory("RADAR_VAL", mask_15bit(value), self.memory)
        result = 1 if value > 0 else 0  # Simplified pass condition
        store_to_memory("TEST_RES", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCRadarTestPrograms."""
        print(f"Initial: RADAR_VAL={self.memory['RADAR_VAL']}, TEST_RES={self.memory['TEST_RES']}")
        result = self.test_radar(100)
        print(f"Radar Test: RADAR_VAL={self.memory['RADAR_VAL']}, TEST_RES={result}")

if __name__ == "__main__":
    radar_test = AGCRadarTestPrograms()
    radar_test.main()