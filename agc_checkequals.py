# agc_checkequals.py
from agc_utils import (
    mask_15bit, store_to_memory, double_precision_add, double_precision_subtract
)

class AGCCheckEquals:
    def __init__(self):
        self.memory = {
            "TESTVAL": 0,    # Value to test
            "RESULT": 0,     # Computed result
            "EXPECTED": 0    # Expected result
        }
        self.passed = True

    def run_add_test(self, a, b, expected):
        """Test double-precision addition."""
        store_to_memory("TESTVAL", a, self.memory)
        store_to_memory("EXPECTED", expected, self.memory)
        high, low = double_precision_add(0, a, b)
        store_to_memory("RESULT", low, self.memory)
        return self.check_result()

    def run_sub_test(self, a, b, expected):
        """Test double-precision subtraction."""
        store_to_memory("TESTVAL", a, self.memory)
        store_to_memory("EXPECTED", expected, self.memory)
        high, low = double_precision_subtract(0, a, b)
        store_to_memory("RESULT", low, self.memory)
        return self.check_result()

    def check_result(self):
        """Compare result to expected value."""
        if self.memory["RESULT"] != self.memory["EXPECTED"]:
            self.passed = False
            return False
        return True

    def main(self):
        """Sanity check for AGCCheckEquals."""
        # Test 1: Addition (300 + 200 = 500)
        add_result = self.run_add_test(300, 200, 500)
        print(f"Add Test (300 + 200 = 500): {'Pass' if add_result else 'Fail'}")
        # Test 2: Subtraction (700 - 400 = 300)
        sub_result = self.run_sub_test(700, 400, 300)
        print(f"Sub Test (700 - 400 = 300): {'Pass' if sub_result else 'Fail'}")
        print(f"All Tests Passed: {self.passed}")

if __name__ == "__main__":
    checkequals = AGCCheckEquals()
    checkequals.main()