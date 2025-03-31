# agc_interpretive_constants.py
from agc_utils import mask_15bit, store_to_memory

class AGCInterpretiveConstants:
    def __init__(self):
        self.memory = {
            "CONST1": 0,    # Constant 1 (scaled)
            "CONST2": 0     # Constant 2 (scaled)
        }

    def set_constants(self, c1, c2):
        """Simulate setting interpretive constants."""
        store_to_memory("CONST1", mask_15bit(c1), self.memory)
        store_to_memory("CONST2", mask_15bit(c2), self.memory)
        return self.memory["CONST1"], self.memory["CONST2"]

    def main(self):
        """Sanity check for AGCInterpretiveConstants."""
        print(f"Initial: CONST1={self.memory['CONST1']}, CONST2={self.memory['CONST2']}")
        c1, c2 = self.set_constants(100, 200)
        print(f"Constants Set: CONST1={c1}, CONST2={c2}")

if __name__ == "__main__":
    constants = AGCInterpretiveConstants()
    constants.main()