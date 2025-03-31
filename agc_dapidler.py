# agc_dapidler.py
from agc_utils import mask_15bit, store_to_memory

class AGCDAPIdler:
    def __init__(self):
        self.memory = {
            "DAP_STATE": 0,   # DAP state (0=idle, 1=active)
            "IDLE_TIME": 0    # Idle time counter (centiseconds, scaled)
        }

    def idle_dap(self, time_increment):
        """Simulate DAP idler incrementing time when idle."""
        if self.memory["DAP_STATE"] == 0:
            current_time = self.memory["IDLE_TIME"]
            new_time = mask_15bit(current_time + time_increment)
            store_to_memory("IDLE_TIME", new_time, self.memory)
        return self.memory["IDLE_TIME"]

    def main(self):
        """Sanity check for AGCDAPIdler."""
        print(f"Initial: DAP_STATE={self.memory['DAP_STATE']}, IDLE_TIME={self.memory['IDLE_TIME']}")
        idle_time = self.idle_dap(50)
        print(f"Idle Update: DAP_STATE={self.memory['DAP_STATE']}, IDLE_TIME={idle_time}")

if __name__ == "__main__":
    idler = AGCDAPIdler()
    idler.main()