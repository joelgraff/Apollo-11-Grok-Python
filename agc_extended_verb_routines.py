# agc_extended_verb_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCExtendedVerbRoutines:
    def __init__(self):
        self.memory = {
            "VERB_CODE": 0,   # Extended verb code
            "VERB_DATA": 0    # Associated data
        }

    def execute_extended_verb(self, verb, data):
        """Simulate execution of an extended verb."""
        store_to_memory("VERB_CODE", mask_15bit(verb), self.memory)
        store_to_memory("VERB_DATA", mask_15bit(data), self.memory)
        # Simplified: increment data as an example action
        result = mask_15bit(data + 1)
        store_to_memory("VERB_DATA", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCExtendedVerbRoutines."""
        print(f"Initial: VERB_CODE={self.memory['VERB_CODE']}, VERB_DATA={self.memory['VERB_DATA']}")
        result = self.execute_extended_verb(50, 123)  # Verb 50, data 123
        print(f"Extended Verb: VERB_CODE={self.memory['VERB_CODE']}, VERB_DATA={result}")

if __name__ == "__main__":
    ext_verbs = AGCExtendedVerbRoutines()
    ext_verbs.main()