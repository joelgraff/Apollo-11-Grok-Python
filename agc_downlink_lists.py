# agc_downlink_lists.py
from agc_utils import mask_15bit, store_to_memory

class AGCDownlinkLists:
    def __init__(self):
        self.memory = {
            "DL_DATA": 0,    # Downlink data (scaled)
            "DL_SENT": 0     # Sent status (0=pending, 1=sent)
        }

    def send_downlink(self, data):
        """Simulate sending a downlink list."""
        store_to_memory("DL_DATA", mask_15bit(data), self.memory)
        store_to_memory("DL_SENT", 1, self.memory)
        return self.memory["DL_DATA"]

    def main(self):
        """Sanity check for AGCDownlinkLists."""
        print(f"Initial: DL_DATA={self.memory['DL_DATA']}, DL_SENT={self.memory['DL_SENT']}")
        data = self.send_downlink(5678)
        print(f"Downlink Sent: DL_DATA={data}, DL_SENT={self.memory['DL_SENT']}")

if __name__ == "__main__":
    downlink = AGCDownlinkLists()
    downlink.main()