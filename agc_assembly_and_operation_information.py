# agc_assembly_and_operation_information.py
from agc_utils import mask_15bit, store_to_memory

class AGCAssemblyAndOperationInformation:
    def __init__(self):
        self.memory = {
            "ASM_VER": 0,    # Assembly version (scaled)
            "OP_STATE": 0    # Operation state (0=off, 1=on)
        }

    def set_info(self, version):
        """Simulate assembly and operation info."""
        store_to_memory("ASM_VER", mask_15bit(version), self.memory)
        store_to_memory("OP_STATE", 1, self.memory)
        return self.memory["ASM_VER"]

    def main(self):
        """Sanity check for AGCAssemblyAndOperationInformation."""
        print(f"Initial: ASM_VER={self.memory['ASM_VER']}, OP_STATE={self.memory['OP_STATE']}")
        version = self.set_info(99)
        print(f"Info Set: ASM_VER={version}, OP_STATE={self.memory['OP_STATE']}")

if __name__ == "__main__":
    asm_info = AGCAssemblyAndOperationInformation()
    asm_info.main()