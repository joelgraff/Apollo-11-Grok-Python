# agc_t3rupt.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, InterruptManager, time

class AGCT3Rupt:
    def __init__(self, interrupt_mgr):
        self.memory = AGCMemory()
        self.interrupts = interrupt_mgr
        self.interrupts.register("T3", self.handle_t3)

    def handle_t3(self):
        store_to_memory("T3_TIME", mask_15bit(int(time.time() * 100)), self.memory.erasable)
        print("T3 Interrupt: Timer Update")

    def main(self):
        self.interrupts.trigger("T3")