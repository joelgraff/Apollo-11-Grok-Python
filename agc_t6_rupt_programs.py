# agc_t6_rupt_programs.py
from agc_utils import mask_15bit, store_to_memory

class AGCT6RuptPrograms:
    def __init__(self):
        self.memory = {
            "T6_TIME": 0,    # T6 interrupt time (centiseconds, scaled)
            "T6_FLAG": 0     # T6 task flag (0=pending, 1=done)
        }

    def t6_interrupt(self, time):
        """Simulate T6 interrupt execution."""
        store_to_memory("T6_TIME", mask_15bit(time), self.memory)
        store_to_memory("T6_FLAG", 1, self.memory)
        return self.memory["T6_TIME"]

    def main(self):
        """Sanity check for AGCT6RuptPrograms."""
        print(f"Initial: T6_TIME={self.memory['T6_TIME']}, T6_FLAG={self.memory['T6_FLAG']}")
        time = self.t6_interrupt(75)
        print(f"T6RUPT: T6_TIME={time}, T6_FLAG={self.memory['T6_FLAG']}")

if __name__ == "__main__":
    t6rupt = AGCT6RuptPrograms()
    t6rupt.main()