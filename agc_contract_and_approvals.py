# agc_contract_and_approvals.py
from agc_utils import mask_15bit, store_to_memory

class AGCContractAndApprovals:
    def __init__(self):
        self.memory = {
            "CONTRACT": 0,    # Contract ID (e.g., NAS 9-4065)
            "APPROVAL": 0     # Approval status (1=approved)
        }

    def set_metadata(self, contract_id, approval_status):
        """Store contract and approval metadata."""
        store_to_memory("CONTRACT", mask_15bit(contract_id), self.memory)
        store_to_memory("APPROVAL", mask_15bit(approval_status), self.memory)
        return self.memory["CONTRACT"], self.memory["APPROVAL"]

    def main(self):
        """Sanity check for AGCContractAndApprovals."""
        print(f"Initial: CONTRACT={self.memory['CONTRACT']}, APPROVAL={self.memory['APPROVAL']}")
        contract, approval = self.set_metadata(94065, 1)  # NAS 9-4065, approved
        print(f"Metadata: CONTRACT={contract}, APPROVAL={approval}")

if __name__ == "__main__":
    contract = AGCContractAndApprovals()
    contract.main()