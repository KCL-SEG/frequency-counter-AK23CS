#"""Frequencies function."""
#"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    # Use a for loop to iterate through the items
    for item in items:
        # Convert each item into a string
        item_str = str(item)

        if item_str not in frequencies:
            frequencies[item_str] = 1
        else:
            frequencies[item_str] += 1

    return frequencies
