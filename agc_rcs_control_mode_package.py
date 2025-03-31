# agc_rcs_control_mode_package.py
from agc_utils import mask_15bit, store_to_memory

class AGCRCSControlModePackage:
    def __init__(self):
        self.memory = {
            "RCS_MODE": 0,    # RCS mode (0=off, 1=on)
            "RCS_CMD": 0      # RCS command (scaled)
        }

    def set_rcs_mode(self, mode, command):
        """Simulate RCS control mode setting."""
        store_to_memory("RCS_MODE", mask_15bit(mode), self.memory)
        store_to_memory("RCS_CMD", mask_15bit(command), self.memory)
        return self.memory["RCS_MODE"], self.memory["RCS_CMD"]

    def main(self):
        """Sanity check for AGCRCSControlModePackage."""
        print(f"Initial: RCS_MODE={self.memory['RCS_MODE']}, RCS_CMD={self.memory['RCS_CMD']}")
        mode, cmd = self.set_rcs_mode(1, 50)  # Mode on, command 50
        print(f"RCS Set: RCS_MODE={mode}, RCS_CMD={cmd}")

if __name__ == "__main__":
    rcs_mode = AGCRCSControlModePackage()
    rcs_mode.main()