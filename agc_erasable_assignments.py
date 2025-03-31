# agc_erasable_assignments.py
from agc_utils import mask_15bit, store_to_memory

class AGCErasableAssignments:
    def __init__(self):
        self.memory = {
            "E_VAR1": 0,   # Erasable variable 1 (generic, scaled)
            "E_VAR2": 0    # Erasable variable 2 (generic, scaled)
        }

    def assign_erasable(self, var1, var2):
        """Assign values to erasable memory locations."""
        store_to_memory("E_VAR1", mask_15bit(var1), self.memory)
        store_to_memory("E_VAR2", mask_15bit(var2), self.memory)
        return self.memory["E_VAR1"], self.memory["E_VAR2"]

    def main(self):
        """Sanity check for AGCErasableAssignments."""
        print(f"Initial: E_VAR1={self.memory['E_VAR1']}, E_VAR2={self.memory['E_VAR2']}")
        v1, v2 = self.assign_erasable(123, 456)
        print(f"Assigned: E_VAR1={v1}, E_VAR2={v2}")

if __name__ == "__main__":
    erasable = AGCErasableAssignments()
    erasable.main()