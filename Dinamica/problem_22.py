# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible
#  reconstruction, return any of them. If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
# ['bedbath', 'and', 'beyond'].

def find_sentence(words, s):
    vistos = {}
    result = _find_sentence(words, s, vistos, [])
    if result is None:
        return None
    return result

def _find_sentence(words, s, vistos, actual): # O(k^N)
    if s == "":
        return actual
    for i in range(len(words)):
        if i in vistos:
            continue
        if s.startswith(words[i]):
            vistos[i] = True
            actual.append(words[i])
            result = _find_sentence(words, s[len(words[i]):], vistos, actual)
            if result is not None:
                return result
            vistos.pop(i)
            actual.pop()
    return None

def find_sentence_dp(words, s): # O(N^2 * M) where M is the average length of the words
    dp = [None] * (len(s) + 1)
    dp[0] = []
    
    for i in range(1, len(s) + 1):
        for word in words:
            if s.startswith(word, i - len(word)):
                if dp[i - len(word)] is not None:
                    dp[i] = dp[i - len(word)] + [word]
                    break
    
    return dp[len(s)]

def find_sentence_si_entra_dicc(s, dictionary): # O(N^2)
    starts = {0: ''}
    for i in range(len(s) + 1):
        new_starts = starts.copy()
        for start_index, _ in starts.items():
            word = s[start_index:i]
            if word in dictionary:
                new_starts[i] = word
        starts = new_starts.copy()

    result = []
    current_length = len(s)
    if current_length not in starts:
        return None
    while current_length > 0:
        word = starts[current_length]
        current_length -= len(word)
        result.append(word)

    return list(reversed(result))


print(find_sentence(['the', 'quick', 'brown', 'fox'], "thequickbrownfox"))
print(find_sentence(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond"))

print(find_sentence_dp(['the', 'quick', 'brown', 'fox'], "thequickbrownfox"))
print(find_sentence_dp(['bed', 'bath', 'bedbath', 'and', 'beyond'], "bedbathandbeyond"))