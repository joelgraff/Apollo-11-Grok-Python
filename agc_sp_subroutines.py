# agc_sp_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCSPSroutines:
    def __init__(self):
        self.memory = {
            "SP_A": 0,      # First single-precision operand
            "SP_B": 0,      # Second single-precision operand
            "SP_RESULT": 0, # Result of operation
            "OVERFLOW": 0   # Overflow flag
        }

    def sp_add(self, a, b):
        """Single-precision addition with overflow detection."""
        store_to_memory("SP_A", a, self.memory)
        store_to_memory("SP_B", b, self.memory)
        result = a + b
        overflow = 1 if result > 0x7FFF else 0
        store_to_memory("SP_RESULT", mask_15bit(result), self.memory)
        store_to_memory("OVERFLOW", overflow, self.memory)
        return self.memory["SP_RESULT"], overflow

    def sp_subtract(self, a, b):
        """Single-precision subtraction with underflow detection."""
        store_to_memory("SP_A", a, self.memory)
        store_to_memory("SP_B", b, self.memory)
        result = a - b
        overflow = 1 if result < 0 else 0
        store_to_memory("SP_RESULT", mask_15bit(result), self.memory)
        store_to_memory("OVERFLOW", overflow, self.memory)
        return self.memory["SP_RESULT"], overflow

    def main(self):
        """Sanity check for AGCSPSroutines."""
        # Test addition: 300 + 200 = 500
        result, ovf = self.sp_add(300, 200)
        print(f"SP Add (300 + 200): RESULT={result}, OVERFLOW={ovf}")
        # Test subtraction: 700 - 400 = 300
        result, ovf = self.sp_subtract(700, 400)
        print(f"SP Subtract (700 - 400): RESULT={result}, OVERFLOW={ovf}")
        # Test overflow: 32000 + 1000
        result, ovf = self.sp_add(32000, 1000)
        print(f"SP Add Overflow (32000 + 1000): RESULT={result}, OVERFLOW={ovf}")

if __name__ == "__main__":
    sp_subroutines = AGCSPSroutines()
    sp_subroutines.main()