# agc_interp_constants.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add

class AGCInterpConstants:
    def __init__(self):
        self.memory = {
            "DP_HALF": (0, 16384),  # 0.5 in double precision (2^-1 scaled to 15-bit)
            "DP_QUARTER": (0, 8192),  # 0.25 in double precision (2^-2 scaled to 15-bit)
            "RESULT": (0, 0)        # Result of operation
        }

    def use_constant(self, value_high, value_low):
        """Demonstrate constant usage: Add DP_HALF to a value."""
        # Add DP_HALF to input value
        half_high, half_low = self.memory["DP_HALF"]
        result_high, result_low = double_precision_add(value_high, value_low, half_low)
        self.memory["RESULT"] = (result_high, result_low)
        return self.memory["RESULT"]

    def main(self):
        """Sanity check for AGCInterpConstants."""
        print(f"Constants: DP_HALF={self.memory['DP_HALF']}, DP_QUARTER={self.memory['DP_QUARTER']}")
        # Add DP_HALF to (0, 1000)
        result = self.use_constant(0, 1000)
        print(f"Result of 1000 + DP_HALF: RESULT={result}")

if __name__ == "__main__":
    interp_constants = AGCInterpConstants()
    interp_constants.main()