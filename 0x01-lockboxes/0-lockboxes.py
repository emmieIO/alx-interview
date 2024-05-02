#!/usr/bin/python3
"""0-lockboxes.py"""

def canUnlockAll(boxes):
    """
    This function checks if all the boxes
    (elements) can be unlocked (accessed)
    given a list of keys for each element.
    """

    # Initialize a list to track accessed elements.
    # Start with all elements as unaccessed (False).
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True  # Mark the first element as accessed (unlocked)

    # Iterate until no new elements are accessed.
    added_boxes = 1  # Start with 1 to enter the loop
    while added_boxes > 0:
        added_boxes = 0
        for i in range(len(boxes)):
            # If an element is already accessed, check its keys.
            if opened_boxes[i]:
                for key in boxes[i]:
                    # Try to access the element pointed to
                    # by the key (avoid potential IndexError).
                    if 0 <= key < len(boxes) and not opened_boxes[key]:
                        opened_boxes[key] = True
                        added_boxes += 1

    # Return True if all elements are accessed, False otherwise.
    return all(opened_boxes)
