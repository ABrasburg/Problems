class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        dicc = {}
        min = len(cards) +1
        for i in range(len(cards)):
            if cards[i] in dicc:
                dist = i - dicc[cards[i]] +1
                if dist < min:
                    min = dist
            dicc[cards[i]] = i
        if min == (len(cards) +1):
            return -1
        return min
                                
cards = [3,4,2,3,4,7]
sol = Solution()
print(sol.minimumCardPickup(cards))