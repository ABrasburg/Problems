# This problem was asked by Palantir.
#
# Given a sequence of words and an integer line length k, return a list of
# fully justified strings.

def group_words(words, k):
    packs = [[]]
    line_len = 0
    for word in words:
        extra_space = 0 if not packs[-1] else 1
        if line_len + extra_space + len(word) <= k:
            line_len += extra_space + len(word)
            packs[-1].append(word)
            continue
        line_len = len(word)
        packs.append([word])
    return packs


def justify_text(words, k):
    matrix = group_words(words, k)
    result = []
    for line in matrix:
        spaces_to_place = k-sum(len(word) for word in line)
        if len(line) == 1:
            result.append(line[0] + " " * spaces_to_place)
            continue
        actual = ""
        spaces = spaces_to_place // (len(line) - 1)
        for i, word in enumerate(line):
            if i == len(line)-1:
                actual += word
                continue
            if spaces_to_place % (len(line) - 1) == 0:
                actual += word + " " * spaces
            else:
                actual += word + " " * (spaces + 1)
                spaces_to_place -= 1
        result.append(actual)
    return result

if __name__ == "__main__":
    result = justify_text(
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        16,
    )
    assert result == [
        "the  quick brown",
        "fox  jumps  over",
        "the   lazy   dog",
    ]

    assert justify_text(["hello"], 8) == ["hello   "]

    assert justify_text(["a", "b", "a"], 5) == ["a b a"]
