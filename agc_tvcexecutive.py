# agc_tvcexecutive.py
from agc_utils import mask_15bit, store_to_memory

class AGCTVCExecutive:
    def __init__(self):
        self.memory = {
            "TVCANGLE": 0,   # TVC gimbal angle (degrees, scaled)
            "TVCCMD": 0      # TVC command value
        }

    def execute_tvc(self, angle_cmd):
        """Execute TVC command."""
        store_to_memory("TVCANGLE", mask_15bit(angle_cmd), self.memory)
        cmd = mask_15bit(angle_cmd + 10)  # Simplified adjustment
        store_to_memory("TVCCMD", cmd, self.memory)
        return cmd

    def main(self):
        """Sanity check for AGCTVCExecutive."""
        print(f"Initial: TVCANGLE={self.memory['TVCANGLE']}, TVCCMD={self.memory['TVCCMD']}")
        cmd = self.execute_tvc(30)
        print(f"TVC Exec: TVCANGLE={self.memory['TVCANGLE']}, TVCCMD={cmd}")

if __name__ == "__main__":
    tvc_exec = AGCTVCExecutive()
    tvc_exec.main()