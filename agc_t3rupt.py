# agc_t3rupt.py
from agc_utils import mask_15bit, store_to_memory

class AGCT3Rupt:
    def __init__(self):
        self.memory = {
            "TIME3": 0,      # T3 timer counter (10ms ticks)
            "T3ENABLE": 0,   # T3 interrupt enable flag
            "JOBCHECK": 0    # Flag to signal job scheduling
        }

    def enable_t3(self):
        """Enable T3 interrupts."""
        store_to_memory("T3ENABLE", 1, self.memory)

    def t3_interrupt(self):
        """Handle T3 interrupt."""
        if self.memory["T3ENABLE"] == 0:
            return False
        # Increment TIME3
        current_time = self.memory["TIME3"]
        new_time = mask_15bit(current_time + 1)
        store_to_memory("TIME3", new_time, self.memory)
        # Signal job check every 5 ticks (arbitrary)
        if new_time % 5 == 0:
            store_to_memory("JOBCHECK", 1, self.memory)
        else:
            store_to_memory("JOBCHECK", 0, self.memory)
        return True

    def disable_t3(self):
        """Disable T3 interrupts."""
        store_to_memory("T3ENABLE", 0, self.memory)

    def main(self):
        """Sanity check for AGCT3Rupt."""
        # Enable T3
        self.enable_t3()
        print(f"Initial: TIME3={self.memory['TIME3']}, JOBCHECK={self.memory['JOBCHECK']}")
        # Simulate 6 interrupts
        for i in range(6):
            result = self.t3_interrupt()
            print(f"Interrupt {i+1}: TIME3={self.memory['TIME3']}, JOBCHECK={self.memory['JOBCHECK']}, Handled={result}")
        # Disable and test
        self.disable_t3()
        result = self.t3_interrupt()
        print(f"After Disable: TIME3={self.memory['TIME3']}, Handled={result}")

if __name__ == "__main__":
    t3rupt = AGCT3Rupt()
    t3rupt.main()