# agc_q_r_axes_rcs_autopilot.py
from agc_utils import mask_15bit, store_to_memory

class AGCQRaxesRCSAutopilot:
    def __init__(self):
        self.memory = {
            "Q_ERROR": 0,    # Q-axis error (degrees, scaled)
            "R_ERROR": 0,    # R-axis error (degrees, scaled)
            "QR_CMD": 0      # Q/R-axis command (scaled)
        }

    def control_qr_axes(self, q_error, r_error):
        """Simulate Q/R-axes RCS autopilot control."""
        store_to_memory("Q_ERROR", mask_15bit(q_error), self.memory)
        store_to_memory("R_ERROR", mask_15bit(r_error), self.memory)
        cmd = mask_15bit(q_error + r_error)  # Simplified combined control
        store_to_memory("QR_CMD", cmd, self.memory)
        return cmd

    def main(self):
        """Sanity check for AGCQRaxesRCSAutopilot."""
        print(f"Initial: Q_ERROR={self.memory['Q_ERROR']}, R_ERROR={self.memory['R_ERROR']}, QR_CMD={self.memory['QR_CMD']}")
        cmd = self.control_qr_axes(5, 7)
        print(f"Q/R-Axes Control: Q_ERROR={self.memory['Q_ERROR']}, R_ERROR={self.memory['R_ERROR']}, QR_CMD={cmd}")

if __name__ == "__main__":
    qr_axes = AGCQRaxesRCSAutopilot()
    qr_axes.main()