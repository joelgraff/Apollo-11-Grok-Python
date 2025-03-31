# agc_down_telemetry_program.py
from agc_utils import mask_15bit, store_to_memory

class AGCDownTelemetryProgram:
    def __init__(self):
        self.memory = {
            "TELE_DATA": 0,   # Telemetry data (scaled)
            "TELE_SENT": 0    # Sent status (0=pending, 1=sent)
        }

    def send_telemetry(self, data):
        """Simulate sending telemetry data."""
        store_to_memory("TELE_DATA", mask_15bit(data), self.memory)
        store_to_memory("TELE_SENT", 1, self.memory)
        return self.memory["TELE_DATA"]

    def main(self):
        """Sanity check for AGCDownTelemetryProgram."""
        print(f"Initial: TELE_DATA={self.memory['TELE_DATA']}, TELE_SENT={self.memory['TELE_SENT']}")
        data = self.send_telemetry(5678)
        print(f"Telemetry Sent: TELE_DATA={data}, TELE_SENT={self.memory['TELE_SENT']}")

if __name__ == "__main__":
    telemetry = AGCDownTelemetryProgram()
    telemetry.main()