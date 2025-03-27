# agc_dap_interface.py
from agc_utils import mask_15bit, store_to_memory

class AGCDAPInterface:
    def __init__(self):
        self.memory = {
            "ATTCMD": 0,    # Attitude command (degrees, scaled)
            "DAPFLAG": 0    # DAP status (0=inactive, 1=active)
        }

    def dap_command(self, attitude):
        """Simulate DAP interface: Send attitude command."""
        store_to_memory("ATTCMD", mask_15bit(attitude), self.memory)
        store_to_memory("DAPFLAG", 1, self.memory)
        return self.memory["ATTCMD"]

    def main(self):
        """Sanity check for AGCDAPInterface."""
        print(f"Initial: ATTCMD={self.memory['ATTCMD']}, DAPFLAG={self.memory['DAPFLAG']}")
        cmd = self.dap_command(30)  # 30-degree attitude command
        print(f"DAP Command: ATTCMD={cmd}, DAPFLAG={self.memory['DAPFLAG']}")

if __name__ == "__main__":
    dap_interface = AGCDAPInterface()
    dap_interface.main()