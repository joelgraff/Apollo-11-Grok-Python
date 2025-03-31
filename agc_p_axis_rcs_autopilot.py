# agc_p_axis_rcs_autopilot.py
from agc_utils import mask_15bit, store_to_memory

class AGCPAxisRCSAutopilot:
    def __init__(self):
        self.memory = {
            "P_ERROR": 0,    # P-axis error (degrees, scaled)
            "P_CMD": 0       # P-axis command (scaled)
        }

    def control_p_axis(self, error):
        """Simulate P-axis RCS autopilot control."""
        store_to_memory("P_ERROR", mask_15bit(error), self.memory)
        cmd = mask_15bit(error * 3)  # Simplified proportional control
        store_to_memory("P_CMD", cmd, self.memory)
        return cmd

    def main(self):
        """Sanity check for AGCPAxisRCSAutopilot."""
        print(f"Initial: P_ERROR={self.memory['P_ERROR']}, P_CMD={self.memory['P_CMD']}")
        cmd = self.control_p_axis(10)
        print(f"P-Axis Control: P_ERROR={self.memory['P_ERROR']}, P_CMD={cmd}")

if __name__ == "__main__":
    p_axis = AGCPAxisRCSAutopilot()
    p_axis.main()