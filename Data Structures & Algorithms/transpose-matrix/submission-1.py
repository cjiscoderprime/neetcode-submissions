class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0]) #matrix[0] goes through each element in first row

        res = [[0] * rows for i in range(cols)] #create as many rows as there are columns

        for r in range(rows):
            for c in range(cols):
                res[c][r] = matrix[r][c]
            
        return res
