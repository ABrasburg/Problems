class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        min_sufijo = [''] * n
        min_sufijo[-1] = s[-1]
        for i in range(n-2, -1, -1):
            min_sufijo[i] = min(s[i], min_sufijo[i+1])

        p = ""
        t = []
        i = 0
        while i < n:
            t.append(s[i])
            while t and (i == n - 1 or t[-1] <= min_sufijo[i + 1]):
                p = p+t.pop()
            i += 1

        while t:
            p = p+t.pop()
        return p