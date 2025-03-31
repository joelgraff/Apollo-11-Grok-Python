# agc_dap_interface_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCDAPInterfaceSubroutines:
    def __init__(self):
        self.memory = {
            "DAP_INPUT": 0,   # DAP input value (scaled)
            "DAP_OUTPUT": 0   # DAP output command (scaled)
        }

    def process_dap(self, input_val):
        """Process DAP input to output command."""
        store_to_memory("DAP_INPUT", mask_15bit(input_val), self.memory)
        output = mask_15bit(input_val * 3)  # Simplified scaling
        store_to_memory("DAP_OUTPUT", output, self.memory)
        return output

    def main(self):
        """Sanity check for AGCDAPInterfaceSubroutines."""
        print(f"Initial: DAP_INPUT={self.memory['DAP_INPUT']}, DAP_OUTPUT={self.memory['DAP_OUTPUT']}")
        output = self.process_dap(20)
        print(f"DAP Processed: DAP_INPUT={self.memory['DAP_INPUT']}, DAP_OUTPUT={output}")

if __name__ == "__main__":
    dap_interface = AGCDAPInterfaceSubroutines()
    dap_interface.main()