# agc_rcs_failure_monitor.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCRCSFailureMonitor:
    def __init__(self):
        self.memory = AGCMemory()

    def monitor_rcs(self, check_val):
        status = 1 if check_val > 100 else 0  # Failure threshold
        store_to_memory("RCS_STATUS", mask_15bit(status), self.memory.erasable)
        print(f"RCS Status: {'Fail' if status else 'OK'}")
        return status

    def main(self):
        print("Testing RCS Failure Monitor")
        self.monitor_rcs(150)
        self.monitor_rcs(50)