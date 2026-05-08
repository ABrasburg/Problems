class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        resul = ""
        largo = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(largo):
            resul += word1[i] + word2[i]
        if len(word1) > len(word2):
            for i in range(largo, len(word1)):
                resul += word1[i]
        elif len(word1) < len(word2):
            for i in range(largo, len(word2)):
                resul += word2[i]
        return resul
        