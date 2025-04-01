# agc_p_axis_rcs_autopilot.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCPAxisRCSAutopilot:
    def __init__(self):
        self.memory = AGCMemory()
        self.error = 0

    def control_p_axis(self, error):
        self.error = error
        cmd = mask_15bit(error * 3)  # Proportional control
        store_to_memory("P_CMD", cmd, self.memory.erasable)
        print(f"P-Axis Command: {cmd}")
        return cmd

    def main(self):
        print("Testing P-Axis RCS")
        self.control_p_axis(10)
        self.control_p_axis(-5)