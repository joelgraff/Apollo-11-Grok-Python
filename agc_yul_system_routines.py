# agc_yul_system_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCYulSystemRoutines:
    def __init__(self):
        self.memory = {
            "DATA": 0,    # System data
            "RESULT": 0   # Processed result
        }

    def process_system(self, input_data):
        """Process system data (e.g., bit manipulation)."""
        store_to_memory("DATA", mask_15bit(input_data), self.memory)
        result = mask_15bit(input_data & 0xFF)  # Example operation: lower 8 bits
        store_to_memory("RESULT", result, self.memory)
        return result

    def main(self):
        """Sanity check for AGCYulSystemRoutines."""
        print(f"Initial: DATA={self.memory['DATA']}, RESULT={self.memory['RESULT']}")
        result = self.process_system(500)
        print(f"Processed: DATA={self.memory['DATA']}, RESULT={result}")

if __name__ == "__main__":
    yul = AGCYulSystemRoutines()
    yul.main()