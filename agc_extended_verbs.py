# agc_extended_verbs.py
from agc_utils import mask_15bit, store_to_memory

class AGCExtendedVerbs:
    def __init__(self):
        self.memory = {
            "VERB_NUM": 0,    # Verb number
            "VERB_ARG": 0     # Verb argument (scaled)
        }

    def execute_verb(self, verb, arg):
        """Simulate an extended verb execution."""
        store_to_memory("VERB_NUM", mask_15bit(verb), self.memory)
        store_to_memory("VERB_ARG", mask_15bit(arg), self.memory)
        # Simplified: double the argument as an example action
        result = mask_15bit(arg * 2)
        store_to_memory("VERB_ARG", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCExtendedVerbs."""
        print(f"Initial: VERB_NUM={self.memory['VERB_NUM']}, VERB_ARG={self.memory['VERB_ARG']}")
        result = self.execute_verb(40, 50)  # Verb 40, arg 50
        print(f"Verb Executed: VERB_NUM={self.memory['VERB_NUM']}, VERB_ARG={result}")

if __name__ == "__main__":
    verbs = AGCExtendedVerbs()
    verbs.main()