# agc_self_check.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCSelfCheck:
    def __init__(self):
        self.memory = AGCMemory()

    def run_self_check(self, value):
        result = 1 if value == 42 else 0  # Test condition
        store_to_memory("CHECK_OK", mask_15bit(result), self.memory.erasable)
        print(f"Self-Check: {'Pass' if result else 'Fail'}")
        return result

    def main(self):
        print("Testing Self-Check")
        self.run_self_check(42)
        self.run_self_check(50)