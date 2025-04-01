# agc_q_r_axes_rcs_autopilot.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCQRaxesRCSAutopilot:
    def __init__(self):
        self.memory = AGCMemory()
        self.q_error = 0
        self.r_error = 0

    def control_qr_axes(self, q_err, r_err):
        self.q_error = q_err
        self.r_error = r_err
        cmd = mask_15bit(q_err + r_err)  # Combined control
        store_to_memory("QR_CMD", cmd, self.memory.erasable)
        print(f"QR-Axes Command: {cmd}")
        return cmd

    def main(self):
        print("Testing QR-Axes RCS")
        self.control_qr_axes(5, 7)