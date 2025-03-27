# AGC Utility Functions
def mask_15bit(value):
    return value & 0x7FFF

def double_add(high, low, operand):
    result_low = low + operand
    overflow = 0
    if result_low > 0x7FFF:
        overflow = 1
        result_low &= 0x7FFF
    return mask_15bit(high + overflow), mask_15bit(result_low)

# Test it
if __name__ == "__main__":
    high, low = double_add(0, 1000, 500)
    print(f"Result: {high}, {low}")