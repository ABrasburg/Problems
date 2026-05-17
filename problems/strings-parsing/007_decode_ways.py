# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def num_encodings_1(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])
    return total

def num_encodings(s):
    lista = [1] * len(s)
    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            lista[i] = 0
        elif i == len(s) - 1:
            lista[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                if i+2 < len(s):
                    lista[i] = lista[i + 2]
            lista[i] += lista[i + 1]
    return lista[0]

print(num_encodings('111'))
print(num_encodings('10'))
print(num_encodings('01'))
print(num_encodings('101'))