from collections import OrderedDict


def count_and_format(s):
    # OrderedDict keeps track of characters in the order they first appear
    counts = OrderedDict()
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Build the result string by alternating count and character
    result = "".join(f"{count}{char}" for char, count in counts.items())
    return result


# Test the program
text = "running"
output = count_and_format(text)
print(f"Input={text}  Output={output}")