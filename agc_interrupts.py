# agc_interrupts.py
from agc_utils import mask_15bit, store_to_memory, transfer_control

class AGCInterrupts:
    def __init__(self):
        self.memory = {
            "T3COUNT": 0,    # T3 timer counter
            "T4COUNT": 0,    # T4 timer counter
            "T6COUNT": 0,    # T6 timer counter
            "INTVEC": 0      # Simulated interrupt vector
        }
        self.handlers = {
            3: self.t3rupt,  # T3 interrupt (e.g., timing)
            4: self.t4rupt,  # T4 interrupt (e.g., DSKY update)
            6: self.t6rupt   # T6 interrupt (thruster timing)
        }

    def trigger_interrupt(self, vector):
        """Dispatch to appropriate interrupt handler."""
        store_to_memory("INTVEC", vector, self.memory)
        if vector in self.handlers:
            return self.handlers[vector]()
        return "NO HANDLER"

    def t3rupt(self):
        """T3 interrupt handler (simplified)."""
        current = self.memory["T3COUNT"]
        store_to_memory("T3COUNT", mask_15bit(current + 1), self.memory)
        return "T3 HANDLED"

    def t4rupt(self):
        """T4 interrupt handler (simplified)."""
        current = self.memory["T4COUNT"]
        store_to_memory("T4COUNT", mask_15bit(current + 1), self.memory)
        return "T4 HANDLED"

    def t6rupt(self):
        """T6 interrupt handler (simplified)."""
        current = self.memory["T6COUNT"]
        store_to_memory("T6COUNT", mask_15bit(current + 1), self.memory)
        return "T6 HANDLED"

    def main(self):
        """Sanity check for AGCInterrupts."""
        # Trigger T3 interrupt
        result = self.trigger_interrupt(3)
        print(f"T3 Interrupt: {result}, T3COUNT={self.memory['T3COUNT']}")
        # Trigger T4 interrupt
        result = self.trigger_interrupt(4)
        print(f"T4 Interrupt: {result}, T4COUNT={self.memory['T4COUNT']}")
        # Trigger T6 interrupt
        result = self.trigger_interrupt(6)
        print(f"T6 Interrupt: {result}, T6COUNT={self.memory['T6COUNT']}")
        # Trigger unknown interrupt
        result = self.trigger_interrupt(7)
        print(f"Unknown Interrupt: {result}")

if __name__ == "__main__":
    interrupts = AGCInterrupts()
    interrupts.main()