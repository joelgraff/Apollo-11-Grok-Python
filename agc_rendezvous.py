# agc_rendezvous.py
from agc_utils import mask_15bit, store_to_memory, double_precision_subtract

class AGCRendezvous:
    def __init__(self):
        self.memory = {
            "VEL_LM": (0, 100),    # LM velocity (m/s, double precision)
            "VEL_CSM": (0, 120),   # CSM velocity (m/s, double precision)
            "RELVEL": (0, 0),      # Relative velocity (m/s, double precision)
            "TIME": 0              # Update time (seconds)
        }

    def update_rendezvous(self, delta_time):
        """Simulate rendezvous guidance: Calculate relative velocity."""
        # Update time
        store_to_memory("TIME", mask_15bit(self.memory["TIME"] + delta_time), self.memory)

        # Calculate relative velocity: V_CSM - V_LM
        lm_high, lm_low = self.memory["VEL_LM"]
        csm_high, csm_low = self.memory["VEL_CSM"]
        rel_high, rel_low = double_precision_subtract(csm_high, csm_low, lm_low)
        if lm_low > csm_low:  # Adjust for borrow
            rel_high = mask_15bit(rel_high - 1)
        self.memory["RELVEL"] = (rel_high, rel_low)

        return self.memory["RELVEL"]

    def main(self):
        """Sanity check for AGCRendezvous."""
        print(f"Initial: VEL_LM={self.memory['VEL_LM']}, VEL_CSM={self.memory['VEL_CSM']}, RELVEL={self.memory['RELVEL']}")
        # Update rendezvous after 5 seconds
        rel_vel = self.update_rendezvous(5)
        print(f"Rendezvous Update: RELVEL={rel_vel}, TIME={self.memory['TIME']}")

if __name__ == "__main__":
    rendezvous = AGCRendezvous()
    rendezvous.main()