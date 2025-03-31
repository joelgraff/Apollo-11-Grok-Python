# agc_fresh_start_subroutines.py
from agc_utils import mask_15bit, store_to_memory

class AGCFreshStartSubroutines:
    def __init__(self):
        self.memory = {
            "FS_STATE": 0,    # Fresh start state (0=normal, 1=started)
            "FS_COUNT": 0     # Fresh start counter
        }

    def perform_fresh_start(self):
        """Simulate a fresh start subroutine."""
        store_to_memory("FS_STATE", 1, self.memory)
        current_count = self.memory["FS_COUNT"]
        new_count = mask_15bit(current_count + 1)
        store_to_memory("FS_COUNT", new_count, self.memory)
        return new_count

    def main(self):
        """Sanity check for AGCFreshStartSubroutines."""
        print(f"Initial: FS_STATE={self.memory['FS_STATE']}, FS_COUNT={self.memory['FS_COUNT']}")
        count = self.perform_fresh_start()
        print(f"Fresh Start: FS_STATE={self.memory['FS_STATE']}, FS_COUNT={count}")

if __name__ == "__main__":
    fresh_subs = AGCFreshStartSubroutines()
    fresh_subs.main()