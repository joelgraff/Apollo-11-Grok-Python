# agc_self_check.py
from agc_utils import mask_15bit, store_to_memory

class AGCSelfCheck:
    def __init__(self):
        self.memory = {
            "TESTVAL": 0,    # Test value
            "RESULT": 0,     # Result of test
            "ERROR": 0       # Error flag (0=pass, 1=fail)
        }

    def run_self_check(self, test_value):
        """Simulate a simple self-check: Add test value to itself."""
        # Store test value
        store_to_memory("TESTVAL", mask_15bit(test_value), self.memory)
        # Perform test: RESULT = TESTVAL + TESTVAL
        expected = mask_15bit(test_value * 2)
        result = mask_15bit(self.memory["TESTVAL"] + self.memory["TESTVAL"])
        store_to_memory("RESULT", result, self.memory)
        # Check if result matches expected
        error = 1 if result != expected else 0
        store_to_memory("ERROR", error, self.memory)
        return result, error

    def main(self):
        """Sanity check for AGCSelfCheck."""
        print(f"Initial: TESTVAL={self.memory['TESTVAL']}, RESULT={self.memory['RESULT']}, ERROR={self.memory['ERROR']}")
        # Run self-check with test value 100
        result, error = self.run_self_check(100)
        print(f"Self-Check: TESTVAL={self.memory['TESTVAL']}, RESULT={result}, ERROR={error}")

if __name__ == "__main__":
    self_check = AGCSelfCheck()
    self_check.main()