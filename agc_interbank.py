# agc_interbank.py
from agc_utils import mask_15bit, store_to_memory

class AGCInterBank:
    def __init__(self):
        self.memory = {
            "BANK1": 0,    # Source bank register
            "BANK2": 0,    # Destination bank register
            "TEMP": 0      # Temporary register for transfer
        }

    def transfer_bank(self, source_value, source_bank, dest_bank):
        """Simulate inter-bank data transfer."""
        # Store source value in source bank
        store_to_memory(source_bank, mask_15bit(source_value), self.memory)
        # Transfer to temp register
        store_to_memory("TEMP", self.memory[source_bank], self.memory)
        # Move from temp to destination bank
        store_to_memory(dest_bank, self.memory["TEMP"], self.memory)
        return self.memory[dest_bank]

    def main(self):
        """Sanity check for AGCInterBank."""
        print(f"Initial: BANK1={self.memory['BANK1']}, BANK2={self.memory['BANK2']}, TEMP={self.memory['TEMP']}")
        # Transfer value 500 from BANK1 to BANK2
        result = self.transfer_bank(500, "BANK1", "BANK2")
        print(f"After Transfer: BANK1={self.memory['BANK1']}, BANK2={result}, TEMP={self.memory['TEMP']}")

if __name__ == "__main__":
    interbank = AGCInterBank()
    interbank.main()