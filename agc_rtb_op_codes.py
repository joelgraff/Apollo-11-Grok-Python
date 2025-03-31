# agc_rtb_op_codes.py
from agc_utils import mask_15bit, store_to_memory

class AGCRTBOpCodes:
    def __init__(self):
        self.memory = {
            "RTB_CODE": 0,    # RTB opcode
            "RTB_DATA": 0     # RTB data (scaled)
        }

    def execute_rtb(self, code, data):
        """Simulate RTB (Return to Basic) opcode execution."""
        store_to_memory("RTB_CODE", mask_15bit(code), self.memory)
        store_to_memory("RTB_DATA", mask_15bit(data), self.memory)
        # Simplified: increment data as an example
        result = mask_15bit(data + 1)
        store_to_memory("RTB_DATA", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCRTBOpCodes."""
        print(f"Initial: RTB_CODE={self.memory['RTB_CODE']}, RTB_DATA={self.memory['RTB_DATA']}")
        result = self.execute_rtb(2, 100)  # RTB code 2, data 100
        print(f"RTB Executed: RTB_CODE={self.memory['RTB_CODE']}, RTB_DATA={result}")

if __name__ == "__main__":
    rtb = AGCRTBOpCodes()
    rtb.main()