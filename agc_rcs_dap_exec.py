# agc_rcs_dap_exec.py
from agc_utils import mask_15bit, store_to_memory

class AGCRCSDAPExec:
    def __init__(self):
        self.memory = {
            "JETCMD": 0,     # Jet firing command (bitfield)
            "DAPSTATE": 0    # DAP state (0=off, 1=on)
        }

    def rcs_command(self, jet_mask):
        """Simulate RCS DAP execution: Fire jets."""
        store_to_memory("JETCMD", mask_15bit(jet_mask), self.memory)
        store_to_memory("DAPSTATE", 1, self.memory)
        return self.memory["JETCMD"]

    def main(self):
        """Sanity check for AGCRCSDAPExec."""
        print(f"Initial: JETCMD={self.memory['JETCMD']}, DAPSTATE={self.memory['DAPSTATE']}")
        cmd = self.rcs_command(0x000F)  # Fire jets 1-4
        print(f"RCS Command: JETCMD={cmd}, DAPSTATE={self.memory['DAPSTATE']}")

if __name__ == "__main__":
    rcs_dap_exec = AGCRCSDAPExec()
    rcs_dap_exec.main()