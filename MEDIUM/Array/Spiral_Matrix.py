class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        row_pointer = 0
        col_pointer = 0

        if rows < 2 or cols < 2:
          for i in range(rows):
            for j in range(cols):
              ans.append(matrix[i][j])
          return ans

        while row_pointer < rows//2 and col_pointer < cols//2:
            i = row_pointer
            for j in range(col_pointer, cols - col_pointer - 1):
                ans.append(matrix[i][j])

            j = cols - col_pointer - 1
            for i in range(row_pointer, rows - row_pointer - 1):
                ans.append(matrix[i][j])

            i = rows - row_pointer - 1
            for j in range(cols - col_pointer - 1, col_pointer, -1):
                ans.append(matrix[i][j])

            j = col_pointer
            for i in range(rows - row_pointer - 1, row_pointer, -1):
                    ans.append(matrix[i][j])

            row_pointer += 1
            col_pointer += 1

        if rows//2 != cols//2:
          if row_pointer >= rows//2 and rows > 2:
              i = row_pointer
              for j in range(col_pointer, cols - col_pointer):
                  ans.append(matrix[i][j])
          elif col_pointer >= cols//2 and cols > 2:
              j = col_pointer
              for i in range(row_pointer, rows - row_pointer):
                  ans.append(matrix[i][j])

        if rows == cols and rows % 2 != 0:
          ans.append(matrix[rows//2][cols//2])

        return ans

matrix = [[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]
sol = Solution()
for x in range(len(matrix)):
  for y in range(len(matrix[x])):
    print(matrix[x][y],end=" ")
  print()
print(sol.spiralOrder(matrix))

'''
if row_pointer >= 3:
            i = row_pointer
            for j in range(col_pointer, cols - col_pointer):
                ans.append(matrix[i][j])
        elif col_pointer >= 3:
            j = col_pointer
            for i in range(row_pointer, rows - row_pointer):
                ans.append(matrix[i][j])
'''
'''
Test Case
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
[[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]
'''