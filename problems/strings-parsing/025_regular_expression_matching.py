# This problem was asked by Facebook.
#
# Implement regular expression matching with the following special characters:
# . matches any single character
# * matches zero or more of the preceding element

from functools import lru_cache


def regular_expression_matching(string, regex):
    @lru_cache(maxsize=None)
    def matches(i, j):
        if j == len(regex):
            return i == len(string)

        first_matches = (
            i < len(string)
            and (regex[j] == string[i] or regex[j] == ".")
        )

        if j + 1 < len(regex) and regex[j + 1] == "*":
            return matches(i, j + 2) or (first_matches and matches(i + 1, j))

        return first_matches and matches(i + 1, j + 1)

    return matches(0, 0)


if __name__ == "__main__":
    assert regular_expression_matching("ray", "ra.")
    assert not regular_expression_matching("raymond", "ra.")
    assert regular_expression_matching("chat", ".*at")
    assert not regular_expression_matching("chats", ".*at")
