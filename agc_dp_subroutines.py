# agc_dp_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCDPSubroutines:
    def __init__(self):
        self.memory = {
            "A_HIGH": 0,    # First operand high word
            "A_LOW": 0,     # First operand low word
            "B_HIGH": 0,    # Second operand high word
            "B_LOW": 0,     # Second operand low word
            "PROD_HIGH": 0, # Product high word
            "PROD_LOW": 0   # Product low word
        }

    def dp_multiply(self, a_high, a_low, b_high, b_low):
        """Simulate double-precision multiplication."""
        # Store operands
        store_to_memory("A_HIGH", mask_15bit(a_high), self.memory)
        store_to_memory("A_LOW", mask_15bit(a_low), self.memory)
        store_to_memory("B_HIGH", mask_15bit(b_high), self.memory)
        store_to_memory("B_LOW", mask_15bit(b_low), self.memory)

        # Simplified multiplication (ignores high-high term for brevity)
        a = (a_high << 15) + a_low
        b = (b_high << 15) + b_low
        product = a * b
        prod_high = mask_15bit(product >> 30)  # Upper 15 bits of 30-bit result
        prod_low = mask_15bit((product >> 15) & 0x7FFF)  # Middle 15 bits
        store_to_memory("PROD_HIGH", prod_high, self.memory)
        store_to_memory("PROD_LOW", prod_low, self.memory)
        return (prod_high, prod_low)

    def main(self):
        """Sanity check for AGCDPSubroutines."""
        print(f"Initial: A=({self.memory['A_HIGH']}, {self.memory['A_LOW']}), B=({self.memory['B_HIGH']}, {self.memory['B_LOW']})")
        # Multiply (0, 100) * (0, 200)
        result = self.dp_multiply(0, 100, 0, 200)
        print(f"DP Multiply (100 * 200): PRODUCT={result}")

if __name__ == "__main__":
    dp_subroutines = AGCDPSubroutines()
    dp_subroutines.main()