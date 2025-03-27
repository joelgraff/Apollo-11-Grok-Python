# agc_down_telemetry.py
from agc_utils import mask_15bit, store_to_memory

class AGCDownTelemetry:
    def __init__(self):
        self.memory = {
            "TIME": 0,         # Current time (seconds)
            "DATA": 0,         # Sample data (e.g., velocity)
            "TELEWORD": 0      # Assembled telemetry word
        }

    def assemble_telemetry(self, time, data):
        """Assemble a telemetry word from time and data."""
        # Store time and data
        store_to_memory("TIME", mask_15bit(time), self.memory)
        store_to_memory("DATA", mask_15bit(data), self.memory)

        # Pack into telemetry word (simplified: 7 bits time, 8 bits data)
        teleword = (time & 0x7F) << 8 | (data & 0xFF)
        store_to_memory("TELEWORD", mask_15bit(teleword), self.memory)
        return self.memory["TELEWORD"]

    def main(self):
        """Sanity check for AGCDownTelemetry."""
        print(f"Initial: TIME={self.memory['TIME']}, DATA={self.memory['DATA']}, TELEWORD={self.memory['TELEWORD']}")
        # Assemble telemetry with time=100s, data=200
        teleword = self.assemble_telemetry(100, 200)
        print(f"Telemetry: TIME={self.memory['TIME']}, DATA={self.memory['DATA']}, TELEWORD={teleword}")

if __name__ == "__main__":
    down_telemetry = AGCDownTelemetry()
    down_telemetry.main()