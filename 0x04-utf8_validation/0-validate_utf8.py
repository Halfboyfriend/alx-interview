#!/usr/bin/python3
"""
Validation
"""

def validUTF8(data):
    # Helper function to check if the current byte starts with "10"
    def check_continuation(byte):
        return (byte >> 6) == 0b10

    num_bytes_to_process = 0

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes_to_process == 0:
            # Determine the number of bytes to process for this character
            if byte >> 7 == 0b0:
                num_bytes_to_process = 1
            elif byte >> 5 == 0b110:
                num_bytes_to_process = 2
            elif byte >> 4 == 0b1110:
                num_bytes_to_process = 3
            elif byte >> 3 == 0b11110:
                num_bytes_to_process = 4
            else:
                return False
        else:
            # Check if the current byte starts with "10" (continuation byte)
            if not check_continuation(byte):
                return False

        num_bytes_to_process -= 1

    # If there are remaining bytes to process, it's an invalid encoding
    return num_bytes_to_process == 0
