# agc_dsky.py
from agc_utils import mask_15bit, store_to_memory

class AGCDsky:
    def __init__(self):
        self.memory = {
            "VERB": 0,      # Verb code
            "NOUN": 0,      # Noun code
            "DISPREG": 0,   # Display register (combined Verb+Noun)
            "KEYIN": 0      # Last key input
        }

    def display_vn(self, verb, noun):
        """Display Verb and Noun on DSKY."""
        store_to_memory("VERB", verb, self.memory)
        store_to_memory("NOUN", noun, self.memory)
        # Combine into a single display value (simplified)
        combined = mask_15bit((verb << 8) | noun)
        store_to_memory("DISPREG", combined, self.memory)
        return combined

    def key_input(self, key):
        """Handle a keypress interrupt."""
        store_to_memory("KEYIN", key, self.memory)
        # Simulate processing key (e.g., Verb 37 = change program)
        if key == 37:  # Verb 37 example
            return "CHANGE PROGRAM"
        return "KEY ACCEPTED"

    def clear_display(self):
        """Clear DSKY display."""
        store_to_memory("VERB", 0, self.memory)
        store_to_memory("NOUN", 0, self.memory)
        store_to_memory("DISPREG", 0, self.memory)

    def main(self):
        """Sanity check for AGCDsky."""
        # Display Verb 16 Noun 65 (monitor time)
        disp_value = self.display_vn(16, 65)
        print(f"Display V16N65: VERB={self.memory['VERB']}, NOUN={self.memory['NOUN']}, DISPREG={disp_value}")
        # Simulate keypress (Verb 37)
        key_result = self.key_input(37)
        print(f"Key Input 37: {key_result}, KEYIN={self.memory['KEYIN']}")
        # Clear display
        self.clear_display()
        print(f"After Clear: DISPREG={self.memory['DISPREG']}")

if __name__ == "__main__":
    dsky = AGCDsky()
    dsky.main()