# agc_interpreter.py
from agc_utils import (
    mask_15bit, double_precision_add, double_precision_subtract,
    transfer_control, store_to_memory, fetch_double_precision
)

class AGCInterpreter:
    def __init__(self):
        self.memory = {
            "MPAC": 0,      # Multi-purpose accumulator (high)
            "MPAC+1": 0,    # Low word
            "MODE": 0,      # 0 = scalar, 1 = vector
            "LOC": 0        # Current instruction pointer
        }
        self.opcodes = {
            0o01: self._dadd,  # Double Add
            0o02: self._dsub   # Double Subtract (simplified example)
        }

    def load_operand(self, address):
        """Load a double-precision operand from memory."""
        high, low = fetch_double_precision(address, self.memory)
        return high, low

    def store_result(self, high, low):
        """Store result back to MPAC."""
        store_to_memory("MPAC", high, self.memory)
        store_to_memory("MPAC+1", low, self.memory)

    def _dadd(self, operand_addr):
        """Interpretive DADD operation."""
        op_high, op_low = self.load_operand(operand_addr)
        high, low = double_precision_add(
            self.memory["MPAC"], self.memory["MPAC+1"], op_low
        )
        # In AGC, high word is adjusted separately; simplified here
        high = mask_15bit(high + op_high)
        self.store_result(high, low)
        return high, low

    def _dsub(self, operand_addr):
        """Interpretive DSU operation."""
        op_high, op_low = self.load_operand(operand_addr)
        high, low = double_precision_subtract(
            self.memory["MPAC"], self.memory["MPAC+1"], op_low
        )
        high = mask_15bit(high - op_high)
        self.store_result(high, low)
        return high, low

    def execute(self, opcode, operand_addr):
        """Execute an interpretive instruction."""
        if opcode in self.opcodes:
            return self.opcodes[opcode](operand_addr)
        return None

    def main(self):
        """Sanity check for AGCInterpreter."""
        self.store_result(0, 1000)  # Set initial MPAC value
        # Simulate memory with operand at address 200
        self.memory[200] = 0
        self.memory[201] = 500
        # Execute DADD (opcode 01 octal)
        result = self.execute(0o01, 200)
        print(f"DADD result: {result}")  # Should be (0, 1500)
        # Execute DSU (opcode 02 octal)
        result = self.execute(0o02, 200)
        print(f"DSU result: {result}")  # Should be (0, 1000)

if __name__ == "__main__":
    interp = AGCInterpreter()
    interp.main()