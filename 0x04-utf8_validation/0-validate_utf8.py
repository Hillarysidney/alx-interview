#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method to determines if the given data set represents a valid
    UTF-8 encoding.
    """
    bytes_num = 0

    taks_1 = 1 << 7
    task_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if bytes_num == 0:

            while mask_byte & i:
                bytes_num += 1
                mask_byte = mask_byte >> 1

            if bytes_num == 0:
                continue

            if bytes_num == 1 or bytes_num > 4:
                return False

        else:
            if not (i & taks_1 and not (i & task_2)):
                    return False

        bytes_num -= 1

    if bytes_num == 0:
        return True

    return False
