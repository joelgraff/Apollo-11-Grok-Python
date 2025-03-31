# agc_pinball_noun_tables.py
from agc_utils import mask_15bit, store_to_memory

class AGCPinballNounTables:
    def __init__(self):
        self.memory = {
            "NOUN_NUM": 0,    # Noun number
            "NOUN_VAL": 0     # Noun value (scaled)
        }

    def set_noun(self, noun, value):
        """Simulate setting a noun from the table."""
        store_to_memory("NOUN_NUM", mask_15bit(noun), self.memory)
        store_to_memory("NOUN_VAL", mask_15bit(value), self.memory)
        return self.memory["NOUN_NUM"], self.memory["NOUN_VAL"]

    def main(self):
        """Sanity check for AGCPinballNounTables."""
        print(f"Initial: NOUN_NUM={self.memory['NOUN_NUM']}, NOUN_VAL={self.memory['NOUN_VAL']}")
        noun, val = self.set_noun(25, 1234)  # Noun 25, value 1234
        print(f"Noun Set: NOUN_NUM={noun}, NOUN_VAL={val}")

if __name__ == "__main__":
    noun_tables = AGCPinballNounTables()
    noun_tables.main()