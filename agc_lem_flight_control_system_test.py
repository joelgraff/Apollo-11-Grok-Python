# agc_lem_flight_control_system_test.py
from agc_utils import mask_15bit, store_to_memory

class AGCLemFlightControlSystemTest:
    def __init__(self):
        self.memory = {
            "FCS_STATE": 0,   # FCS test state (0=off, 1=on)
            "FCS_RESULT": 0   # Test result (scaled)
        }

    def test_fcs(self, input_val):
        """Simulate LEM flight control system test."""
        store_to_memory("FCS_STATE", 1, self.memory)
        result = mask_15bit(input_val * 2)  # Simplified scaling
        store_to_memory("FCS_RESULT", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCLemFlightControlSystemTest."""
        print(f"Initial: FCS_STATE={self.memory['FCS_STATE']}, FCS_RESULT={self.memory['FCS_RESULT']}")
        result = self.test_fcs(50)
        print(f"FCS Test: FCS_STATE={self.memory['FCS_STATE']}, FCS_RESULT={result}")

if __name__ == "__main__":
    fcs_test = AGCLemFlightControlSystemTest()
    fcs_test.main()