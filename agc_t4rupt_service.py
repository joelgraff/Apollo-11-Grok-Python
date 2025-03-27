# agc_t4rupt_service.py
from agc_utils import mask_15bit, store_to_memory

class AGCT4RuptService:
    def __init__(self):
        self.memory = {
            "RCSCMD": 0,    # RCS command register (bitfield for jets)
            "T4TIME": 0,    # T4 interrupt time (centiseconds)
            "STATE": 0      # Interrupt state (0=idle, 1=active)
        }

    def t4_service_rcs(self, time, jet_mask):
        """Simulate T4 interrupt servicing RCS firing."""
        # Update T4 time
        store_to_memory("T4TIME", mask_15bit(time), self.memory)
        # Set RCS command (simplified jet firing bitmask)
        store_to_memory("RCSCMD", mask_15bit(jet_mask), self.memory)
        # Mark interrupt active
        store_to_memory("STATE", 1, self.memory)
        return self.memory["RCSCMD"]

    def main(self):
        """Sanity check for AGCT4RuptService."""
        print(f"Initial: RCSCMD={self.memory['RCSCMD']}, T4TIME={self.memory['T4TIME']}, STATE={self.memory['STATE']}")
        # Service T4 at 120cs with jet mask 0x0003 (fire jets 1 and 2)
        cmd = self.t4_service_rcs(120, 0x0003)
        print(f"T4 Service: RCSCMD={cmd}, T4TIME={self.memory['T4TIME']}, STATE={self.memory['STATE']}")

if __name__ == "__main__":
    t4rupt_service = AGCT4RuptService()
    t4rupt_service.main()