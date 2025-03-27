# agc_downlink.py
from agc_utils import mask_15bit, store_to_memory, pack_word, shift_left

class AGCDownlink:
    def __init__(self):
        self.memory = {
            "DNTABLE": {},  # Simulated downlink table (address: value)
            "DNADR": 0,     # Current downlink address
            "DNPTR": 0      # Pointer to next item
        }
        self.telemetry = []  # Buffer for transmitted data

    def load_table(self, table_data):
        """Load telemetry data into DNTABLE."""
        for addr, value in table_data.items():
            store_to_memory(addr, value, self.memory["DNTABLE"])

    def send_word(self, address):
        """Send a single word to telemetry."""
        value = self.memory["DNTABLE"].get(address, 0)
        self.telemetry.append(value)
        store_to_memory("DNADR", address, self.memory)
        return value

    def pack_and_send(self, high_addr, low_addr):
        """Pack two values into one word and send."""
        high = self.memory["DNTABLE"].get(high_addr, 0)
        low = self.memory["DNTABLE"].get(low_addr, 0)
        packed = pack_word(high & 0x7F, low & 0xFF)  # 7+8 bits
        self.telemetry.append(packed)
        return packed

    def main(self):
        """Sanity check for AGCDownlink."""
        # Sample telemetry data
        table = {100: 50, 101: 200, 102: 15}
        self.load_table(table)
        # Send single word
        sent = self.send_word(100)
        print(f"Sent word from 100: {sent}")  # 50
        # Pack and send two words
        packed = self.pack_and_send(101, 102)
        print(f"Packed 101+102: {packed}")  # 200<<8 + 15 = 51215 & 0x7FFF = 1279
        print(f"Telemetry buffer: {self.telemetry}")  # [50, 1279]

if __name__ == "__main__":
    downlink = AGCDownlink()
    downlink.main()