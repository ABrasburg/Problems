# This problem was asked by Facebook.
#
# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced.

def is_balanced(brackets):
    pila = []
    for c in brackets:
        if c in "({[":
            pila.append(c)
            continue
        if not pila:
            return False
        if pila[-1] == "(" and c == ")" or \
           pila[-1] == "{" and c == "}" or \
           pila[-1] == "[" and c == "]":
           pila.pop()
           continue
        return False
    if pila:
        return False
    return True


if __name__ == "__main__":
    assert is_balanced("([])[]({})")
    assert not is_balanced("([)]")
    assert not is_balanced("((()")
