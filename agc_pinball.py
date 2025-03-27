# agc_pinball.py
from agc_utils import mask_15bit, store_to_memory, transfer_control, bit_test

class AGCPinball:
    def __init__(self):
        self.memory = {
            "VERBREG": 0,   # Verb register
            "NOUNREG": 0,   # Noun register
            "DSKY": 0,      # Simulated DSKY output (simplified)
            "CADR": 0       # Current address
        }
        self.input_buffer = []

    def nvsub(self, verb, noun):
        """Set verb and noun (NVSUB routine)."""
        store_to_memory("VERBREG", verb, self.memory)
        store_to_memory("NOUNREG", noun, self.memory)
        self.update_dsky()

    def update_dsky(self):
        """Simulate DSKY display update."""
        # In AGC, this writes to channels; here, we combine verb/noun
        display_value = (self.memory["VERBREG"] << 7) | self.memory["NOUNREG"]
        store_to_memory("DSKY", display_value, self.memory)

    def charin(self, char_code):
        """Process a single character input (CHARIN simplified)."""
        self.input_buffer.append(char_code)
        if char_code == 0o21:  # Verb key (octal 21 in AGC)
            return self.process_verb()
        elif char_code == 0o22:  # Noun key (octal 22)
            return self.process_noun()
        return None

    def process_verb(self):
        """Handle verb input."""
        verb = self.input_buffer[-2] if len(self.input_buffer) >= 2 else 0
        store_to_memory("VERBREG", verb, self.memory)
        self.update_dsky()
        return verb

    def process_noun(self):
        """Handle noun input."""
        noun = self.input_buffer[-2] if len(self.input_buffer) >= 2 else 0
        store_to_memory("NOUNREG", noun, self.memory)
        self.update_dsky()
        return noun

    def main(self):
        """Sanity check for AGCPinball."""
        self.nvsub(10, 20)  # Set verb 10, noun 20
        print(f"DSKY after nvsub: {self.memory['DSKY']}")  # Should be 1300 (10<<7 + 20)
        self.charin(0o21)   # Simulate verb key
        self.charin(15)     # Verb 15
        print(f"Verb set to: {self.memory['VERBREG']}")  # Should be 15
        self.charin(0o22)   # Noun key
        self.charin(25)     # Noun 25
        print(f"Noun set to: {self.memory['NOUNREG']}")  # Should be 25
        print(f"Final DSKY: {self.memory['DSKY']}")     # Should be 2045 (15<<7 + 25)

if __name__ == "__main__":
    pinball = AGCPinball()
    pinball.main()