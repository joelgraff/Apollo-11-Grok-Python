# agc_inter_bank_communication.py
from agc_utils import mask_15bit, store_to_memory

class AGCInterBankCommunication:
    def __init__(self):
        self.memory = {
            "BANK_SRC": 0,    # Source bank number
            "BANK_DEST": 0,   # Destination bank number
            "DATA": 0         # Data to transfer (scaled)
        }

    def transfer_data(self, src_bank, dest_bank, data):
        """Simulate inter-bank data transfer."""
        store_to_memory("BANK_SRC", mask_15bit(src_bank), self.memory)
        store_to_memory("BANK_DEST", mask_15bit(dest_bank), self.memory)
        store_to_memory("DATA", mask_15bit(data), self.memory)
        return self.memory["DATA"]

    def main(self):
        """Sanity check for AGCInterBankCommunication."""
        print(f"Initial: BANK_SRC={self.memory['BANK_SRC']}, BANK_DEST={self.memory['BANK_DEST']}, DATA={self.memory['DATA']}")
        data = self.transfer_data(2, 3, 456)  # Transfer from bank 2 to 3
        print(f"Transferred: BANK_SRC={self.memory['BANK_SRC']}, BANK_DEST={self.memory['BANK_DEST']}, DATA={data}")

if __name__ == "__main__":
    inter_bank = AGCInterBankCommunication()
    inter_bank.main()