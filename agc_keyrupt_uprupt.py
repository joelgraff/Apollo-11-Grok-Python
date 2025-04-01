# agc_keyrupt_uprupt.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, InterruptManager

class AGCKeyruptUprupt:
    def __init__(self, interrupt_mgr):
        self.memory = AGCMemory()
        self.interrupts = interrupt_mgr
        self.interrupts.register("KEY", self.handle_key)

    def handle_key(self):
        store_to_memory("KEY_VAL", mask_15bit(5), self.memory.erasable)
        print("Keyrupt: Key Pressed")

    def main(self):
        self.interrupts.trigger("KEY")