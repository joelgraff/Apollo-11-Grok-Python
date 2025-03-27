# agc_block_two_self_check.py
from agc_utils import mask_15bit, store_to_memory

class AGCBlockTwoSelfCheck:
    def __init__(self):
        self.memory = {
            "MEMVAL": 0,    # Memory value to test
            "PARITY": 0,    # Calculated parity bit
            "CHECK": 0      # Check result (0=fail, 1=pass)
        }

    def parity_check(self, value):
        """Simulate Block II self-check: Verify memory parity."""
        store_to_memory("MEMVAL", mask_15bit(value), self.memory)
        # Simple parity: count 1s, should be even (AGC uses odd parity, simplified here)
        parity = bin(value & 0x7FFF).count('1') % 2
        store_to_memory("PARITY", parity, self.memory)
        check = 1 if parity == 0 else 0  # Pass if even
        store_to_memory("CHECK", check, self.memory)
        return check

    def main(self):
        """Sanity check for AGCBlockTwoSelfCheck."""
        print(f"Initial: MEMVAL={self.memory['MEMVAL']}, PARITY={self.memory['PARITY']}, CHECK={self.memory['CHECK']}")
        result = self.parity_check(0x0055)  # Test with 01010101 binary
        print(f"Parity Check: MEMVAL={self.memory['MEMVAL']}, PARITY={self.memory['PARITY']}, CHECK={result}")

if __name__ == "__main__":
    block_two_self_check = AGCBlockTwoSelfCheck()
    block_two_self_check.main()