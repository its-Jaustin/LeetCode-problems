#200. Number of Islands
#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#Constraints:
#m == grid.length
#n == grid[i].length
#1 <= m, n <= 300
#grid[i][j] is '0' or '1'.

#Time Complexity: O(x*y)

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        checked = set()
        islands = 0
        m = len(grid) - 1
        n = len(grid[0]) -1
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) in checked: continue #move on if already checked
                elif grid[x][y] == '1':
                    checked.add((x,y))
                    islands += 1
                else: #if '0' move on to next
                    checked.add((x,y))
                    continue
                #bfs, checks all kids first
                level = [(x, y)]
                while level != []:
                    key = level.pop()
                    checked.add(key)
                    #this would be faster if we didn't use a custom function but I didn't want to
                    kids = [x for x in self.getAdjacent(key, m, n) if x not in checked and grid[x[0]][x[1]]== '1']
                    for k in kids:
                        level.append(k)
                        checked.add(k)
        return islands
    def getAdjacent(self, p:tuple, m, n) -> list:
        adj = []
        if p[0] > 0: adj.append((p[0]-1, p[1]))
        if p[0] < (m): adj.append((p[0]+1, p[1]))
        if p[1] > 0: adj.append((p[0], p[1]-1))
        if p[1] < (n): adj.append((p[0], p[1]+1))
        return adj
