# agc_alarm_and_abort.py
from agc_utils import mask_15bit, store_to_memory

class AGCAlarmAndAbort:
    def __init__(self):
        self.memory = {
            "ALARM_CODE": 0,   # Alarm code
            "ABORT_FLAG": 0    # Abort status (0=off, 1=on)
        }

    def trigger_alarm(self, code):
        """Simulate triggering an alarm or abort."""
        store_to_memory("ALARM_CODE", mask_15bit(code), self.memory)
        abort = 1 if code > 1000 else 0  # Simplified abort threshold
        store_to_memory("ABORT_FLAG", abort, self.memory)
        return self.memory["ALARM_CODE"], self.memory["ABORT_FLAG"]

    def main(self):
        """Sanity check for AGCAlarmAndAbort."""
        print(f"Initial: ALARM_CODE={self.memory['ALARM_CODE']}, ABORT_FLAG={self.memory['ABORT_FLAG']}")
        code, abort = self.trigger_alarm(1202)  # Alarm 1202 (executive overflow)
        print(f"Alarm: ALARM_CODE={code}, ABORT_FLAG={abort}")

if __name__ == "__main__":
    alarm = AGCAlarmAndAbort()
    alarm.main()