class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        max = -1
        pos = 0
        while pos < len(number):
            if number[pos] !=  digit:
                pos += 1
                continue
            numero = number[:pos] + number[pos+1:]
            if int(numero) > max:
                max = int(numero)
            pos += 1
        return str(max)
    
sol = Solution()
print(sol.removeDigit("1231", "1"))