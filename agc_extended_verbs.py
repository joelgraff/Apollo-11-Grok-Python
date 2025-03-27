# agc_extended_verbs.py
from agc_utils import mask_15bit, store_to_memory

class AGCExtendedVerbs:
    def __init__(self):
        self.memory = {
            "VERB": 0,      # Verb code
            "DISPVAL": 0    # Value to display
        }

    def execute_verb(self, verb_code, value):
        """Simulate extended verb execution (e.g., V50 = display value)."""
        store_to_memory("VERB", mask_15bit(verb_code), self.memory)
        if verb_code == 50:  # V50: Display value
            store_to_memory("DISPVAL", mask_15bit(value), self.memory)
        return self.memory["DISPVAL"]

    def main(self):
        """Sanity check for AGCExtendedVerbs."""
        print(f"Initial: VERB={self.memory['VERB']}, DISPVAL={self.memory['DISPVAL']}")
        result = self.execute_verb(50, 1234)
        print(f"Verb 50: VERB={self.memory['VERB']}, DISPVAL={result}")

if __name__ == "__main__":
    extended_verbs = AGCExtendedVerbs()
    extended_verbs.main()