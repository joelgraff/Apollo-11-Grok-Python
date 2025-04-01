# agc_t4rupt.py
import time
from agc_utils import mask_15bit, store_to_memory, AGCMemory, InterruptManager

class AGCT4Rupt:
    def __init__(self, interrupt_mgr):
        self.memory = AGCMemory()
        self.interrupts = interrupt_mgr
        self.interrupts.register("T4", self.handle_t4)

    def handle_t4(self):
        store_to_memory("T4_TIME", mask_15bit(int(time.time() * 100)), self.memory.erasable)
        print("T4 Interrupt: System Check")

    def main(self):
        self.interrupts.trigger("T4")