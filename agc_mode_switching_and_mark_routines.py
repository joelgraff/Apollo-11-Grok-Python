# agc_mode_switching_and_mark_routines.py
from agc_utils import mask_15bit, store_to_memory

class AGCModeSwitchingAndMarkRoutines:
    def __init__(self):
        self.memory = {
            "MODE": 0,     # Current mode (e.g., 0=standby, 1=active)
            "MARK": 0      # Mark status (0=none, 1=marked)
        }

    def switch_mode(self, new_mode):
        """Simulate mode switching and marking."""
        store_to_memory("MODE", mask_15bit(new_mode), self.memory)
        store_to_memory("MARK", 1 if new_mode > 0 else 0, self.memory)
        return self.memory["MODE"]

    def main(self):
        """Sanity check for AGCModeSwitchingAndMarkRoutines."""
        print(f"Initial: MODE={self.memory['MODE']}, MARK={self.memory['MARK']}")
        mode = self.switch_mode(1)  # Switch to active
        print(f"Mode Switch: MODE={mode}, MARK={self.memory['MARK']}")

if __name__ == "__main__":
    mode_switch = AGCModeSwitchingAndMarkRoutines()
    mode_switch.main()