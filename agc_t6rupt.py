# agc_t6rupt.py
from agc_utils import mask_15bit, store_to_memory

class AGCT6Rupt:
    def __init__(self):
        self.memory = {
            "T6TIME": 0,    # Time remaining for thruster firing
            "THRUST": 0,    # Thruster state (on/off)
            "T6ENABLE": 0   # T6 interrupt enable flag
        }

    def set_thruster(self, duration, thrust):
        """Set thruster firing duration and state."""
        store_to_memory("T6TIME", duration, self.memory)
        store_to_memory("THRUST", thrust, self.memory)
        store_to_memory("T6ENABLE", 1, self.memory)  # Enable interrupt

    def t6_interrupt(self):
        """Simulate T6 clock interrupt."""
        if self.memory["T6ENABLE"] == 0 or self.memory["T6TIME"] == 0:
            return False  # No interrupt if disabled or time’s up
        # Decrement timer (single word)
        current_time = self.memory["T6TIME"]
        new_time = mask_15bit(current_time - 1)
        store_to_memory("T6TIME", new_time, self.memory)
        if new_time == 0:
            store_to_memory("THRUST", 0, self.memory)
            store_to_memory("T6ENABLE", 0, self.memory)
            return True  # Interrupt complete
        return False  # Still firing

    def main(self):
        """Sanity check for AGCT6Rupt."""
        self.set_thruster(5, 100)
        print(f"Initial: T6TIME={self.memory['T6TIME']}, THRUST={self.memory['THRUST']}")
        for i in range(6):
            complete = self.t6_interrupt()
            print(f"Interrupt {i+1}: T6TIME={self.memory['T6TIME']}, THRUST={self.memory['THRUST']}, Complete={complete}")

if __name__ == "__main__":
    t6rupt = AGCT6Rupt()
    t6rupt.main()