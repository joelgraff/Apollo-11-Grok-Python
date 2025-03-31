# agc_upper_stage_dap.py
from agc_utils import mask_15bit, store_to_memory

class AGCUpperStageDAP:
    def __init__(self):
        self.memory = {
            "ATTITUDE": 0,   # Current attitude (degrees, scaled)
            "COMMAND": 0     # DAP command value
        }

    def adjust_attitude(self, att_cmd):
        """Adjust upper stage attitude."""
        store_to_memory("COMMAND", mask_15bit(att_cmd), self.memory)
        new_att = mask_15bit(self.memory["ATTITUDE"] + att_cmd)
        store_to_memory("ATTITUDE", new_att, self.memory)
        return new_att

    def main(self):
        """Sanity check for AGCUpperStageDAP."""
        print(f"Initial: ATTITUDE={self.memory['ATTITUDE']}, COMMAND={self.memory['COMMAND']}")
        att = self.adjust_attitude(45)
        print(f"Adjusted: ATTITUDE={att}, COMMAND={self.memory['COMMAND']}")

if __name__ == "__main__":
    upper_dap = AGCUpperStageDAP()
    upper_dap.main()