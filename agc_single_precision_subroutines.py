# agc_single_precision_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCSinglePrecisionSubroutines:
    def __init__(self):
        self.memory = {
            "SP_INPUT": 0,    # Single precision input (scaled)
            "SP_RESULT": 0    # Single precision result (scaled)
        }

    def sp_add(self, value):
        """Simulate single precision addition."""
        store_to_memory("SP_INPUT", mask_15bit(value), self.memory)
        result = mask_15bit(self.memory["SP_INPUT"] + 5)  # Simplified addition
        store_to_memory("SP_RESULT", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCSinglePrecisionSubroutines."""
        print(f"Initial: SP_INPUT={self.memory['SP_INPUT']}, SP_RESULT={self.memory['SP_RESULT']}")
        result = self.sp_add(25)
        print(f"SP Add: SP_INPUT={self.memory['SP_INPUT']}, SP_RESULT={result}")

if __name__ == "__main__":
    sp_subs = AGCSinglePrecisionSubroutines()
    sp_subs.main()