# agc_input_output_control.py
from agc_utils import mask_15bit, store_to_memory

class AGCInputOutputControl:
    def __init__(self):
        self.memory = {
            "CHAN_NUM": 0,   # Channel number
            "CHAN_VAL": 0    # Channel value (scaled)
        }

    def write_channel(self, channel, value):
        """Simulate writing to an I/O channel."""
        store_to_memory("CHAN_NUM", mask_15bit(channel), self.memory)
        store_to_memory("CHAN_VAL", mask_15bit(value), self.memory)
        return self.memory["CHAN_VAL"]

    def main(self):
        """Sanity check for AGCInputOutputControl."""
        print(f"Initial: CHAN_NUM={self.memory['CHAN_NUM']}, CHAN_VAL={self.memory['CHAN_VAL']}")
        val = self.write_channel(14, 255)  # Channel 14 (e.g., DSKY), value 255
        print(f"Channel Write: CHAN_NUM={self.memory['CHAN_NUM']}, CHAN_VAL={val}")

if __name__ == "__main__":
    io = AGCInputOutputControl()
    io.main()