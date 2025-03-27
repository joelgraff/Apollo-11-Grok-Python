# agc_restarts.py
from agc_utils import mask_15bit, store_to_memory, fetch_double_precision

class AGCRestarts:
    def __init__(self):
        self.memory = {
            "JOBADDR": 0,    # Current job address
            "JOBPRI": 0,     # Job priority
            "RESTART": 0,    # Restart flag (1 = restart in progress)
            "SAVEDADDR": 0,  # Saved job address
            "SAVEDPRI": 0    # Saved job priority
        }

    def save_state(self, job_addr, job_priority):
        """Save current job state for restart."""
        store_to_memory("JOBADDR", job_addr, self.memory)
        store_to_memory("JOBPRI", job_priority, self.memory)
        store_to_memory("SAVEDADDR", job_addr, self.memory)
        store_to_memory("SAVEDPRI", job_priority, self.memory)

    def trigger_restart(self):
        """Initiate a restart, preserving saved state."""
        store_to_memory("RESTART", 1, self.memory)
        # Simulate clearing current job
        store_to_memory("JOBADDR", 0, self.memory)
        store_to_memory("JOBPRI", 0, self.memory)

    def restore_state(self):
        """Restore job state after restart."""
        if self.memory["RESTART"] == 1:
            restored_addr = self.memory["SAVEDADDR"]
            restored_pri = self.memory["SAVEDPRI"]
            store_to_memory("JOBADDR", restored_addr, self.memory)
            store_to_memory("JOBPRI", restored_pri, self.memory)
            store_to_memory("RESTART", 0, self.memory)
            return restored_addr, restored_pri
        return None, None

    def main(self):
        """Sanity check for AGCRestarts."""
        # Save a job state
        self.save_state(200, 15)
        print(f"Initial: JOBADDR={self.memory['JOBADDR']}, JOBPRI={self.memory['JOBPRI']}")
        # Trigger a restart
        self.trigger_restart()
        print(f"After Restart: JOBADDR={self.memory['JOBADDR']}, JOBPRI={self.memory['JOBPRI']}")
        # Restore state
        addr, pri = self.restore_state()
        print(f"Restored: JOBADDR={self.memory['JOBADDR']}, JOBPRI={self.memory['JOBPRI']}")

if __name__ == "__main__":
    restarts = AGCRestarts()
    restarts.main()