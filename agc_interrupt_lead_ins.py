# agc_interrupt_lead_ins.py
from agc_utils import mask_15bit, store_to_memory

class AGCInterruptLeadIns:
    def __init__(self):
        self.memory = {
            "INT_TYPE": 0,   # Interrupt type (e.g., 1=T4RUPT)
            "INT_FLAG": 0    # Interrupt flag (0=inactive, 1=active)
        }

    def trigger_interrupt(self, int_type):
        """Simulate an interrupt lead-in."""
        store_to_memory("INT_TYPE", mask_15bit(int_type), self.memory)
        store_to_memory("INT_FLAG", 1, self.memory)
        return self.memory["INT_TYPE"]

    def main(self):
        """Sanity check for AGCInterruptLeadIns."""
        print(f"Initial: INT_TYPE={self.memory['INT_TYPE']}, INT_FLAG={self.memory['INT_FLAG']}")
        int_type = self.trigger_interrupt(1)  # Simulate T4RUPT
        print(f"Interrupt: INT_TYPE={int_type}, INT_FLAG={self.memory['INT_FLAG']}")

if __name__ == "__main__":
    interrupts = AGCInterruptLeadIns()
    interrupts.main()