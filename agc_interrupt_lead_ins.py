# agc_interrupt_lead_ins.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory, InterruptManager

class AGCInterruptLeadIns:
    def __init__(self):
        self.memory = AGCMemory()
        self.interrupts = InterruptManager()

    def setup_interrupts(self):
        self.interrupts.register("T3", lambda: print("T3 Rupt"))
        self.interrupts.register("T4", lambda: print("T4 Rupt"))

    def main(self):
        self.setup_interrupts()
        self.interrupts.trigger("T3")
        self.interrupts.trigger("T4")