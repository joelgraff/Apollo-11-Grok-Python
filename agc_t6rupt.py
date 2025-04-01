# agc_t6rupt.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, InterruptManager, time

class AGCT6Rupt:
    def __init__(self, interrupt_mgr):
        self.memory = AGCMemory()
        self.interrupts = interrupt_mgr
        self.interrupts.register("T6", self.handle_t6)

    def handle_t6(self):
        store_to_memory("T6_TIME", mask_15bit(int(time.time() * 100)), self.memory.erasable)
        print("T6 Interrupt: Jet Control")

    def main(self):
        self.interrupts.trigger("T6")