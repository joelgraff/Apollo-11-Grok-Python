# agc_rr_leadin_and_trysw.py
from agc_utils import mask_15bit, store_to_memory

class AGCRRLeadinAndTrysw:
    def __init__(self):
        self.memory = {
            "RR_DATA": 0,    # Rendezvous Radar data (scaled)
            "TRYSW": 0       # Try switch status (0=off, 1=on)
        }

    def update_rr(self, data):
        """Simulate RR lead-in and try switch."""
        store_to_memory("RR_DATA", mask_15bit(data), self.memory)
        store_to_memory("TRYSW", 1, self.memory)
        return self.memory["RR_DATA"]

    def main(self):
        """Sanity check for AGCRRLeadinAndTrysw."""
        print(f"Initial: RR_DATA={self.memory['RR_DATA']}, TRYSW={self.memory['TRYSW']}")
        data = self.update_rr(3000)
        print(f"RR Update: RR_DATA={data}, TRYSW={self.memory['TRYSW']}")

if __name__ == "__main__":
    rr = AGCRRLeadinAndTrysw()
    rr.main()