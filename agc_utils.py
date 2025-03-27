# agc_utils.py
def mask_15bit(value):
    """Mask a value to 15 bits (AGC word size)."""
    return value & 0x7FFF

def double_precision_add(high, low, operand):
    """Double-precision addition with AGC overflow handling."""
    result_low = low + operand
    overflow = 0
    if result_low > 0x7FFF:
        overflow = 1
        result_low &= 0x7FFF
    result_high = high + overflow
    return mask_15bit(result_high), mask_15bit(result_low)

def double_precision_subtract(high, low, operand):
    """Double-precision subtraction with borrow."""
    result_low = low - operand
    borrow = 0
    if result_low < 0:
        borrow = 1
        result_low &= 0x7FFF
    result_high = high - borrow
    return mask_15bit(result_high), mask_15bit(result_low)

def double_precision_multiply(high, low, factor):
    """Simplified double-precision multiply."""
    total = (high << 15) + low
    result = total * factor // 0x4000
    high = (result >> 15) & 0x7FFF
    low = result & 0x7FFF
    return high, low

def double_precision_accumulate(acc_high, acc_low, value_high, value_low):
    """Accumulate a double-precision value into an accumulator."""
    low = mask_15bit(acc_low + value_low)
    carry = 1 if (acc_low + value_low) > 0x7FFF else 0
    high = mask_15bit(acc_high + value_high + carry)
    return high, low

def transfer_control(address, memory):
    """Simulate TC (Transfer Control)."""
    return memory.get(address, 0)

def store_to_memory(location, value, memory):
    """Store a value in memory (TS instruction)."""
    memory[location] = mask_15bit(value)

def fetch_double_precision(address, memory):
    """Fetch a double-precision value from memory."""
    high = memory.get(address, 0)
    low = memory.get(address + 1, 0)
    return high, low

def bit_test(value, bit_position):
    """Test a specific bit (like MASK in AGC)."""
    return (value & (1 << (bit_position - 1))) != 0

def pack_word(high_bits, low_bits):
    """Pack two values into a 15-bit word (e.g., 7+8 bits)."""
    return mask_15bit((high_bits << 8) | low_bits)

def shift_left(value, positions):
    """Shift bits left, masking to 15 bits."""
    return mask_15bit(value << positions)

def sine_approx(angle):
    """Simplified sine approximation."""
    if angle > 0x4000:
        angle = 0x8000 - angle
    result = (angle * 10000) // 0x4000
    return mask_15bit(result)

def error_magnitude(high1, low1, high2, low2):
    """Calculate magnitude of difference between two double-precision values."""
    diff_high, diff_low = double_precision_subtract(high1, low1, low2)
    diff_high = diff_high - high2 if low1 < low2 else diff_high  # Adjust for borrow
    if diff_high < 0:  # Absolute value
        diff_high, diff_low = double_precision_subtract(0, 0, diff_low)
        diff_high = mask_15bit(-diff_high)
    return diff_high, diff_low

def main():
    """Sanity check for agc_utils."""
    memory = {}
    store_to_memory(100, 1234, memory)
    high, low = fetch_double_precision(100, memory)
    high, low = double_precision_add(high, low, 567)
    print(f"Add: {high}, {low}")
    high, low = double_precision_accumulate(high, low, 0, 300)
    print(f"Accumulate 300: {high}, {low}")
    sine_val = sine_approx(0x2000)
    print(f"Sine approx (pi/4): {sine_val}")
    err_high, err_low = error_magnitude(0,1000,0,850)
    print(f"Error magnitude (1000-850): {err_high}, {err_low}") #should be 0, 150

if __name__ == "__main__":
    main()