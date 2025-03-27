# agc_io_control.py
from agc_utils import mask_15bit, store_to_memory

class AGCIOControl:
    def __init__(self):
        self.memory = {
            "CHAN14": 0,    # Channel 14 (DSKY input)
            "CHAN5": 0,     # Channel 5 (RCS thruster output)
            "INPUT": 0      # Simulated DSKY input
        }

    def read_dsky(self, simulated_input):
        """Simulate reading from DSKY (Channel 14)."""
        store_to_memory("INPUT", simulated_input, self.memory)
        store_to_memory("CHAN14", simulated_input, self.memory)
        return self.memory["CHAN14"]

    def write_channel(self, channel, value):
        """Write to an output channel."""
        if channel == 5:  # RCS thruster channel
            store_to_memory("CHAN5", value, self.memory)
        # Add more channels as needed
        return self.memory.get(f"CHAN{channel}", 0)

    def clear_channel(self, channel):
        """Clear a channel’s value."""
        self.write_channel(channel, 0)

    def main(self):
        """Sanity check for AGCIOControl."""
        # Simulate DSKY input (e.g., Verb 16 Noun 65)
        dsky_value = self.read_dsky(1665)
        print(f"DSKY Input (CHAN14): {dsky_value}")
        # Write to Channel 5 (RCS thruster)
        self.write_channel(5, 101)  # Arbitrary thruster command
        print(f"CHAN5 Output: {self.memory['CHAN5']}")
        # Clear Channel 5
        self.clear_channel(5)
        print(f"CHAN5 After Clear: {self.memory['CHAN5']}")

if __name__ == "__main__":
    io_control = AGCIOControl()
    io_control.main()