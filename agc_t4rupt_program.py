# agc_t4rupt_program.py
from agc_utils import mask_15bit, store_to_memory

class AGCT4RuptProgram:
    def __init__(self):
        self.memory = {
            "T4_TIME": 0,   # T4 interrupt time (centiseconds, scaled)
            "T4_TASK": 0    # T4 task status (0=pending, 1=done)
        }

    def t4_interrupt(self, time):
        """Simulate T4RUPT task execution."""
        store_to_memory("T4_TIME", mask_15bit(time), self.memory)
        store_to_memory("T4_TASK", 1, self.memory)
        return self.memory["T4_TIME"]

    def main(self):
        """Sanity check for AGCT4RuptProgram."""
        print(f"Initial: T4_TIME={self.memory['T4_TIME']}, T4_TASK={self.memory['T4_TASK']}")
        time = self.t4_interrupt(100)
        print(f"T4RUPT: T4_TIME={time}, T4_TASK={self.memory['T4_TASK']}")

if __name__ == "__main__":
    t4rupt = AGCT4RuptProgram()
    t4rupt.main()