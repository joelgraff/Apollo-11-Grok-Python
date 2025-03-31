# agc_utils.py
from queue import PriorityQueue
import time

def mask_15bit(value):
    return value & 0x7FFF

def store_to_memory(key, value, memory):
    memory[key] = value

class AGCMemory:
    def __init__(self):
        self.erasable = {}  # Simulates erasable memory (address: value)
        self.fixed = {}    # Simulates fixed memory banks

    def allocate_vac(self, size):
        addr = max(self.erasable.keys(), default=-1) + 1
        for i in range(size):
            self.erasable[addr + i] = 0
        return addr

    def read(self, addr):
        return self.erasable.get(addr, 0)

class InterruptManager:
    def __init__(self):
        self.handlers = {}

    def register(self, rupt_id, handler):
        self.handlers[rupt_id] = handler

    def trigger(self, rupt_id):
        if rupt_id in self.handlers:
            self.handlers[rupt_id]()

class DSKYMock:
    def __init__(self):
        self.display = ""

    def show(self, data):
        self.display = str(data)
        print(f"DSKY: {self.display}")