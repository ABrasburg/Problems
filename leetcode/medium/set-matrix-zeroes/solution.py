class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        columna = set()
        fila = set()
        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[f][c] == 0:
                    print(f, c)
                    columna.add(c)
                    fila.add(f)
        for f in range(len(matrix)):
            for c in range(len(matrix[0])):
                if f in fila or c in columna:
                    matrix[f][c] = 0
    
sol = Solution()
matrix =  [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix)
print(matrix)