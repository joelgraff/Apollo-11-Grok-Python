# agc_dapa_and_dapb_data.py
from agc_utils import mask_15bit, store_to_memory

class AGCDAPAandDAPBData:
    def __init__(self):
        self.memory = {
            "DAPA_RATE": 0,   # DAP A rate (degrees/sec, scaled)
            "DAPB_RATE": 0    # DAP B rate (degrees/sec, scaled)
        }

    def set_dap_rates(self, rate_a, rate_b):
        """Set DAP A and B rates."""
        store_to_memory("DAPA_RATE", mask_15bit(rate_a), self.memory)
        store_to_memory("DAPB_RATE", mask_15bit(rate_b), self.memory)
        return self.memory["DAPA_RATE"], self.memory["DAPB_RATE"]

    def main(self):
        """Sanity check for AGCDAPAandDAPBData."""
        print(f"Initial: DAPA_RATE={self.memory['DAPA_RATE']}, DAPB_RATE={self.memory['DAPB_RATE']}")
        rate_a, rate_b = self.set_dap_rates(10, 15)
        print(f"DAP Rates: DAPA_RATE={rate_a}, DAPB_RATE={rate_b}")

if __name__ == "__main__":
    dap_data = AGCDAPAandDAPBData()
    dap_data.main()