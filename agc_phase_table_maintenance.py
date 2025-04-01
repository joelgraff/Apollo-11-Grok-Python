# agc_phase_table_maintenance.py
from agc_utils import mask_15bit, store_to_memory, AGCMemory

class AGCPhaseTableMaintenance:
    def __init__(self):
        self.memory = AGCMemory()
        self.phases = {}

    def update_phase(self, phase_id, state):
        self.phases[phase_id] = state
        store_to_memory(f"PHASE_{phase_id}", mask_15bit(state), self.memory.erasable)
        print(f"Phase {phase_id} Updated to {state}")

    def main(self):
        print("Testing Phase Table Maintenance")
        self.update_phase(1, 1)
        self.update_phase(2, 0)