# agc_bankcall.py
from agc_utils import mask_15bit, store_to_memory, transfer_control

class AGCBankCall:
    def __init__(self):
        self.memory = {
            "BANK": 0,     # Current memory bank
            "ADDR": 0      # Target address in bank
        }

    def bank_call(self, bank_num, address):
        """Simulate a bank call to switch memory banks."""
        store_to_memory("BANK", mask_15bit(bank_num), self.memory)
        store_to_memory("ADDR", mask_15bit(address), self.memory)
        return transfer_control("ADDR", self.memory)

    def main(self):
        """Sanity check for AGCBankCall."""
        print(f"Initial: BANK={self.memory['BANK']}, ADDR={self.memory['ADDR']}")
        result = self.bank_call(2, 1500)  # Bank 2, address 1500
        print(f"Bank Call: BANK={self.memory['BANK']}, ADDR={self.memory['ADDR']}, Result={result}")

if __name__ == "__main__":
    bankcall = AGCBankCall()
    bankcall.main()