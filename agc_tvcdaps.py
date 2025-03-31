# agc_tvcdaps.py
from agc_utils import mask_15bit, store_to_memory

class AGCTVCDaps:
    def __init__(self):
        self.memory = {
            "TVCTHRUST": 0,  # TVC thrust command (N, scaled)
            "TVCACT": 0      # TVC actuator position
        }

    def adjust_daps(self, thrust):
        """Adjust TVC actuator based on thrust."""
        store_to_memory("TVCTHRUST", mask_15bit(thrust), self.memory)
        act_pos = mask_15bit(thrust // 10)  # Simplified scaling
        store_to_memory("TVCACT", act_pos, self.memory)
        return act_pos

    def main(self):
        """Sanity check for AGCTVCDaps."""
        print(f"Initial: TVCTHRUST={self.memory['TVCTHRUST']}, TVCACT={self.memory['TVCACT']}")
        pos = self.adjust_daps(1000)
        print(f"DAPS Adjust: TVCTHRUST={self.memory['TVCTHRUST']}, TVCACT={pos}")

if __name__ == "__main__":
    tvc_daps = AGCTVCDaps()
    tvc_daps.main()