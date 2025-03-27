# agc_rtb_opcodes.py
from agc_utils import mask_15bit, store_to_memory, transfer_control

class AGCRTBOpCodes:
    def __init__(self):
        self.memory = {
            "INTERP_REG": 0,  # Interpretive register
            "RETURN_ADDR": 0, # Address to return to
            "OPCODE": 0       # Current opcode
        }

    def execute_rtb(self, opcode, return_addr):
        """Execute an RTB opcode and return to basic address."""
        store_to_memory("OPCODE", opcode, self.memory)
        store_to_memory("RETURN_ADDR", return_addr, self.memory)
        # Simulate interpretive operation (e.g., add 100 to INTERP_REG)
        if opcode == 1:  # Arbitrary RTB opcode for addition
            current = self.memory["INTERP_REG"]
            store_to_memory("INTERP_REG", mask_15bit(current + 100), self.memory)
        # Return to basic address
        return transfer_control("RETURN_ADDR", self.memory)

    def set_interp_reg(self, value):
        """Set interpretive register for testing."""
        store_to_memory("INTERP_REG", value, self.memory)

    def main(self):
        """Sanity check for AGCRTBOpCodes."""
        # Set initial interpretive register
        self.set_interp_reg(50)
        print(f"Initial: INTERP_REG={self.memory['INTERP_REG']}, RETURN_ADDR={self.memory['RETURN_ADDR']}")
        # Execute RTB with opcode 1, return to address 200
        return_addr = self.execute_rtb(1, 200)
        print(f"After RTB: INTERP_REG={self.memory['INTERP_REG']}, RETURN_ADDR={return_addr}")

if __name__ == "__main__":
    rtb_opcodes = AGCRTBOpCodes()
    rtb_opcodes.main()