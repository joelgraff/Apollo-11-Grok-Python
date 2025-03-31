# agc_tvcmaddaps.py
from agc_utils import mask_15bit, store_to_memory, double_precision_add

class AGCTVCMaddaps:
    def __init__(self):
        self.memory = {
            "TVCPOS": (0, 0),   # TVC position (double precision)
            "TVCDV": 0          # TVC delta value
        }

    def update_tvc(self, delta):
        """Update TVC position with delta."""
        store_to_memory("TVCDV", mask_15bit(delta), self.memory)
        pos_high, pos_low = self.memory["TVCPOS"]
        new_high, new_low = double_precision_add(pos_high, pos_low, delta)
        self.memory["TVCPOS"] = (new_high, new_low)
        return new_high, new_low

    def main(self):
        """Sanity check for AGCTVCMaddaps."""
        print(f"Initial: TVCPOS={self.memory['TVCPOS']}, TVCDV={self.memory['TVCDV']}")
        pos_high, pos_low = self.update_tvc(50)
        print(f"Updated: TVCPOS=({pos_high}, {pos_low}), TVCDV={self.memory['TVCDV']}")

if __name__ == "__main__":
    tvc_maddaps = AGCTVCMaddaps()
    tvc_maddaps.main()