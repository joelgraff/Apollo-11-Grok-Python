# agc_csm_docked_dap.py
from agc_utils import mask_15bit, store_to_memory

class AGCCSMDockedDAP:
    def __init__(self):
        self.memory = {
            "ERROR": 0,    # Attitude error (degrees, scaled)
            "COMMAND": 0   # DAP command (scaled)
        }

    def correct_attitude(self, error):
        """Simulate CSM docked DAP attitude correction."""
        store_to_memory("ERROR", mask_15bit(error), self.memory)
        cmd = mask_15bit(error * 2)  # Simplified proportional control
        store_to_memory("COMMAND", cmd, self.memory)
        return cmd

    def main(self):
        """Sanity check for AGCCSMDockedDAP."""
        print(f"Initial: ERROR={self.memory['ERROR']}, COMMAND={self.memory['COMMAND']}")
        cmd = self.correct_attitude(20)
        print(f"DAP Correction: ERROR={self.memory['ERROR']}, COMMAND={cmd}")

if __name__ == "__main__":
    dap = AGCCSMDockedDAP()
    dap.main()