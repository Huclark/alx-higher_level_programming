def magic_calculation(a, b):
    const_number = 98  # LOAD_CONST 1 (98)
    const_number = const_number ** a  # LOAD_FAST 0 (a) | BINARY_POWER
    const_number = const_number + b  # LOAD_FAST 1 (b) | BINARY_ADD
    return const_number  # RETURN_VALUE
