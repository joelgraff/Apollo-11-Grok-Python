# agc_restarts_routine.py
from agc_utils import mask_15bit, store_to_memory

class AGCRestartsRoutine:
    def __init__(self):
        self.memory = {
            "RESTART_COUNT": 0,   # Number of restarts
            "RESTART_FLAG": 0     # Restart status (0=off, 1=on)
        }

    def perform_restart(self):
        """Simulate a restart increment."""
        current_count = self.memory["RESTART_COUNT"]
        new_count = mask_15bit(current_count + 1)
        store_to_memory("RESTART_COUNT", new_count, self.memory)
        store_to_memory("RESTART_FLAG", 1, self.memory)
        return new_count

    def main(self):
        """Sanity check for AGCRestartsRoutine."""
        print(f"Initial: RESTART_COUNT={self.memory['RESTART_COUNT']}, RESTART_FLAG={self.memory['RESTART_FLAG']}")
        count = self.perform_restart()
        print(f"Restarted: RESTART_COUNT={count}, RESTART_FLAG={self.memory['RESTART_FLAG']}")

if __name__ == "__main__":
    restarts = AGCRestartsRoutine()
    restarts.main()