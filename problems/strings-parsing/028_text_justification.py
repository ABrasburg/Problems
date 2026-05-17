# This problem was asked by Palantir.
#
# Given a sequence of words and an integer line length k, return a list of
# fully justified strings.


def justify_text(words, k):
    pass


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
