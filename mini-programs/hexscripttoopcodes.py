"""
  Hex Script to Opcode Module
"""

def convert_script_to_opcodes(script_hex):
    """
      convert a script to opcodes
    """
    script_bytes = bytes.fromhex(script_hex)
    i = 0
    print(script_hex)
    print(script_bytes)

    while i < len(script_bytes):
        opcode = script_bytes[i]
        i += 1

        if opcode <= 0x4b:
            # If opcode is less than or equal to 0x4b, it represents data
            data_length = opcode
            data = script_bytes[i:i + data_length]
            print(f"OP_PUSHDATA{data_length}: {data.hex()}")
            i += data_length
        else:
            # Opcode represents an operation
            print(f"OP_{opcode:02x}")

# convert_script_to_opcode call with 010101029301038801027693010487
bitcoin_script_hex = "010101029301038801027693010487"
convert_script_to_opcodes(bitcoin_script_hex)
