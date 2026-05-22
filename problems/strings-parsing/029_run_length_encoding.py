# This problem was asked by Amazon.
#
# Implement run-length encoding and decoding.
# The string to encode has no digits and only contains alphabetic characters.
# The string to decode is valid.

def encode(value):
    if not value: return value
    res = ""
    count = 0
    actual = ""
    for c in value:
        if c == actual:
            count += 1
            continue
        if actual != "":
            res += f"{count}{actual}"
        actual = c
        count = 1
    res += f"{count}{actual}"
    return res

def decode(value):
    res = ""
    num = 0
    for c in value:
        if c.isdigit():
            num = num * 10
            num += int(c)
        else:
            res += num * c
            num = 0
    return res


if __name__ == "__main__":
    assert encode("") == ""
    assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
    assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"
