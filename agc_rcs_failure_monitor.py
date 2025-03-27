# agc_rcs_failure_monitor.py
from agc_utils import mask_15bit, store_to_memory

class AGCRCSFailureMonitor:
    def __init__(self):
        self.memory = {
            "RCSSTATUS": 0,  # Bitfield: 1=jet on, 0=jet failed
            "ALARM": 0       # Alarm code (0=no failure, 1=failure)
        }

    def check_rcs(self, jet_status):
        """Simulate RCS failure check."""
        store_to_memory("RCSSTATUS", mask_15bit(jet_status), self.memory)
        # Check if any jet failed (simplified: alarm if status != 0xFFFF)
        alarm = 1 if jet_status != 0x7FFF else 0
        store_to_memory("ALARM", alarm, self.memory)
        return alarm

    def main(self):
        """Sanity check for AGCRCSFailureMonitor."""
        print(f"Initial: RCSSTATUS={self.memory['RCSSTATUS']}, ALARM={self.memory['ALARM']}")
        result = self.check_rcs(0x7FFD)  # One jet failed (bit 1 off)
        print(f"RCS Check: RCSSTATUS={self.memory['RCSSTATUS']}, ALARM={result}")

if __name__ == "__main__":
    rcs_failure_monitor = AGCRCSFailureMonitor()
    rcs_failure_monitor.main()