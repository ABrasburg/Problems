class Solution(object):
    def _gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""

        min_len = min(len(str1), len(str2))
        for i in range(min_len, 0, -1):
            candidate = str1[:i]
            if len(str1) % i == 0 and len(str2) % i == 0:
                if candidate * (len(str1) // i) == str1 and candidate * (len(str2) // i) == str2:
                    return candidate
        return ""
    
    def gcdOfStrings(self, str1, str2):
        if  str1 + str2 != str2 + str1:
            return ""
        def gcd(a, b):
            if (a == 0):
                return b
            return gcd(b % a, a)

        max_len = gcd(len(str1), len(str2))
        return str1[:max_len]