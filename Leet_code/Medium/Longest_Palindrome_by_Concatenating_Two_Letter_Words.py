class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        freqs = {}
        for word in words:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1

        total = 0
        has_center = False

        for word in list(freqs.keys()):
            rev = word[::-1]
            if word == rev:
                count = freqs[word]
                pairs = count // 2
                total += pairs * 4
                freqs[word] -= pairs * 2
                if freqs[word] == 1:
                    has_center = True
            elif rev in freqs:
                pair_count = min(freqs[word], freqs[rev])
                total += pair_count * 4
                freqs[word] -= pair_count
                freqs[rev] -= pair_count

        if has_center:
            total += 2

        return total

    
sol = Solution()
words = ["lc","cl","gg"]
print(sol.longestPalindrome(words))