# agc_t4rupt.py
from agc_utils import mask_15bit, store_to_memory

class AGCT4Rupt:
    def __init__(self):
        self.memory = {
            "T4COUNT": 0,    # T4 interrupt counter
            "DSKYVAL": 0,    # Value to display on DSKY
            "T4ENABLE": 0    # T4 interrupt enable flag
        }

    def enable_t4(self):
        """Enable T4 interrupts."""
        store_to_memory("T4ENABLE", 1, self.memory)

    def t4_interrupt(self):
        """Handle T4 interrupt."""
        if self.memory["T4ENABLE"] == 0:
            return False
        # Increment counter
        current_count = self.memory["T4COUNT"]
        new_count = mask_15bit(current_count + 1)
        store_to_memory("T4COUNT", new_count, self.memory)
        # Update DSKY value (simplified periodic update)
        dsky_value = mask_15bit(new_count * 10)  # Arbitrary scaling
        store_to_memory("DSKYVAL", dsky_value, self.memory)
        return True

    def disable_t4(self):
        """Disable T4 interrupts."""
        store_to_memory("T4ENABLE", 0, self.memory)

    def main(self):
        """Sanity check for AGCT4Rupt."""
        # Enable T4
        self.enable_t4()
        print(f"Initial: T4COUNT={self.memory['T4COUNT']}, DSKYVAL={self.memory['DSKYVAL']}")
        # Simulate 3 interrupts
        for i in range(3):
            result = self.t4_interrupt()
            print(f"Interrupt {i+1}: T4COUNT={self.memory['T4COUNT']}, DSKYVAL={self.memory['DSKYVAL']}, Handled={result}")
        # Disable and test
        self.disable_t4()
        result = self.t4_interrupt()
        print(f"After Disable: T4COUNT={self.memory['T4COUNT']}, Handled={result}")

if __name__ == "__main__":
    t4rupt = AGCT4Rupt()
    t4rupt.main()