# agc_restart_tables.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCRestartTables:
    def __init__(self):
        self.memory = AGCMemory()
        self.restarts = {}

    def set_restart(self, rid, priority):
        self.restarts[rid] = priority
        store_to_memory(f"RESTART_{rid}", mask_15bit(priority), self.memory.erasable)
        print(f"Restart {rid} Priority: {priority}")

    def main(self):
        print("Testing Restart Tables")
        self.set_restart(1, 2)
        self.set_restart(2, 1)