# agc_optics_test.py
from agc_utils import mask_15bit, store_to_memory

class AGCOpticsTest:
    def __init__(self):
        self.memory = {
            "SEXANGLE": 0,  # Sextant angle (degrees, scaled)
            "TESTFLAG": 0   # Test result (0=fail, 1=pass)
        }

    def optics_test(self, measured_angle):
        """Simulate optics test: Check sextant angle."""
        store_to_memory("SEXANGLE", mask_15bit(measured_angle), self.memory)
        # Simple pass condition: angle > 0
        test_result = 1 if measured_angle > 0 else 0
        store_to_memory("TESTFLAG", test_result, self.memory)
        return self.memory["TESTFLAG"]

    def main(self):
        """Sanity check for AGCOpticsTest."""
        print(f"Initial: SEXANGLE={self.memory['SEXANGLE']}, TESTFLAG={self.memory['TESTFLAG']}")
        result = self.optics_test(45)  # Test with 45 degrees
        print(f"Optics Test: SEXANGLE={self.memory['SEXANGLE']}, TESTFLAG={result}")

if __name__ == "__main__":
    optics_test = AGCOpticsTest()
    optics_test.main()