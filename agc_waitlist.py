# agc_waitlist.py
from agc_utils import mask_15bit, store_to_memory, PriorityQueue, AGCMemory, time

class AGCWaitlist:
    def __init__(self):
        self.memory = AGCMemory()
        self.waitlist = PriorityQueue()  # (time, task_id)

    def add_task(self, task_id, delay_cs):
        time_to_run = int(time.time() * 100) + delay_cs
        self.waitlist.put((time_to_run, task_id))
        store_to_memory(f"WAIT_{task_id}", mask_15bit(task_id), self.memory.erasable)

    def check_tasks(self):
        current_time = int(time.time() * 100)
        while not self.waitlist.empty():
            time_to_run, task_id = self.waitlist.queue[0]
            if current_time >= time_to_run:
                self.waitlist.get()
                print(f"Running Waitlist Task {task_id}")
            else:
                break

    def main(self):
        self.add_task(1, 50)  # 0.5s delay
        self.add_task(2, 100) # 1s delay
        for _ in range(15):
            self.check_tasks()
            time.sleep(0.1)