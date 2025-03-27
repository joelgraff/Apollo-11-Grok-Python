# agc_alarm_abort.py
from agc_utils import mask_15bit, store_to_memory

class AGCAlarmAbort:
    def __init__(self):
        self.memory = {
            "ALARM_CODE": 0,  # Alarm code (e.g., 1201 for IMU failure)
            "ABORT_FLAG": 0,  # 1 = abort condition triggered
            "FAILREG": 0      # Failure register for diagnostics
        }

    def trigger_alarm(self, code):
        """Set an alarm code."""
        store_to_memory("ALARM_CODE", code, self.memory)
        store_to_memory("FAILREG", code, self.memory)  # Simplified logging
        return True

    def trigger_abort(self, code):
        """Trigger an abort condition with an alarm."""
        self.trigger_alarm(code)
        store_to_memory("ABORT_FLAG", 1, self.memory)
        return True

    def check_status(self):
        """Check if an abort is active."""
        return self.memory["ABORT_FLAG"] == 1

    def reset(self):
        """Reset alarm and abort state."""
        store_to_memory("ALARM_CODE", 0, self.memory)
        store_to_memory("ABORT_FLAG", 0, self.memory)
        store_to_memory("FAILREG", 0, self.memory)

    def main(self):
        """Sanity check for AGCAlarmAbort."""
        # Trigger a minor alarm (e.g., 212 for gyro drift)
        self.trigger_alarm(212)
        print(f"Alarm Triggered: ALARM_CODE={self.memory['ALARM_CODE']}, ABORT_FLAG={self.memory['ABORT_FLAG']}")
        # Trigger an abort (e.g., 1202 for program overflow)
        self.trigger_abort(1202)
        print(f"Abort Triggered: ALARM_CODE={self.memory['ALARM_CODE']}, ABORT_FLAG={self.memory['ABORT_FLAG']}, FAILREG={self.memory['FAILREG']}")
        # Check status
        abort_active = self.check_status()
        print(f"Abort Active: {abort_active}")
        # Reset and verify
        self.reset()
        print(f"After Reset: ALARM_CODE={self.memory['ALARM_CODE']}, ABORT_FLAG={self.memory['ABORT_FLAG']}")

if __name__ == "__main__":
    alarm_abort = AGCAlarmAbort()
    alarm_abort.main()