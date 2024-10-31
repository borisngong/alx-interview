#!/usr/bin/python3
""" Module for working with UTF-8 character """


def validUTF8(data):
    """Number of bytes in the current UTF-8 character"""
    remaining_bytes = 0

    for num in data:
        # Get only the least significant 8 bits of the integer
        byte = num & 0xFF

        if remaining_bytes == 0:
            # Determine the number of bytes based on the first byte
            if (byte >> 7) == 0:
                # 1-byte character (starts with 0)
                continue
            elif (byte >> 5) == 0b110:
                # 2-byte character (starts with 110)
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character (starts with 1110)
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character (starts with 11110)
                remaining_bytes = 3
            else:
                # Invalid starting byte for UTF-8
                return False
        else:
            # Check if the byte is a valid continuation byte (starts with 10)
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # If all characters are valid, remaining_bytes should be 0
    return remaining_bytes == 0
