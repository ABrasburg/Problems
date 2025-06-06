class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        flores = flowerbed
        cant = 0
        for i in range(len(flowerbed)):
            if flores[i] == 1 or (i != 0 and flores[i-1] == 1) or (i != len(flowerbed)-1 and flores[i+1] == 1):
                continue
            flores[i] = 1
            cant+=1
            if cant == n:
                return True
        return False