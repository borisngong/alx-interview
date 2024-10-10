#!/usr/bin/python3
"""Module for the lock boxes puzzle."""


def get_next_opened_box(opened_boxes):
    """
    Get keys from the next opened box.

    Args:
        opened_boxes (dict): Boxes that have been opened.

    Returns:
        list: Keys from the next opened box, or None if none available.
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (list): List of boxes containing keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    opened_boxes = {}
    while True:
        if len(opened_boxes) == 0:
            opened_boxes[0] = {'status': 'opened', 'keys': boxes[0]}

        keys = get_next_opened_box(opened_boxes)
        if keys:
            for key in keys:
                try:
                    if (opened_boxes.get(key) and
                            opened_boxes.get(key).get('status') == 'checked'):
                        continue
                    opened_boxes[key] = {'status': 'opened',
                                         'keys': boxes[key]}
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in opened_boxes.values()]:
            continue
        elif len(opened_boxes) == len(boxes):
            break
        else:
            return False

    return len(opened_boxes) == len(boxes)


def main():
    """Test function."""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
