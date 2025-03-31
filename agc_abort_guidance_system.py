# agc_abort_guidance_system.py
from agc_utils import mask_15bit, store_to_memory

class AGCAbortGuidanceSystem:
    def __init__(self):
        self.memory = {
            "ABORT_THRUST": 0,   # Abort thrust (scaled)
            "ABORT_STATE": 0     # Abort state (0=off, 1=on)
        }

    def run_abort(self, thrust):
        """Simulate abort guidance system."""
        store_to_memory("ABORT_THRUST", mask_15bit(thrust), self.memory)
        store_to_memory("ABORT_STATE", 1, self.memory)
        return self.memory["ABORT_THRUST"]

    def main(self):
        """Sanity check for AGCAbortGuidanceSystem."""
        print(f"Initial: ABORT_THRUST={self.memory['ABORT_THRUST']}, ABORT_STATE={self.memory['ABORT_STATE']}")
        thrust = self.run_abort(700)
        print(f"Abort Ran: ABORT_THRUST={thrust}, ABORT_STATE={self.memory['ABORT_STATE']}")

if __name__ == "__main__":
    abort = AGCAbortGuidanceSystem()
    abort.main()