class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        self.grid = grid
        self.checked = set()
        checked = self.checked
        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) in checked: continue #move on if already checked
                if grid[x][y] == '1':
                    checked.add((x,y))
                    islands += 1
                    self.visualize(checked)
                else: #if '0' move on to next
                    checked.add((x,y))
                    continue
                #bfs, checks all kids first
                level = [(x, y)]
                while level != []:
                    key = level.pop()
                    checked.add(key)
                    kids = [x for x in self.getAdjacent(key) if x not in checked and grid[x[0]][x[1]]== '1']
                    for k in kids:
                        level.append(k)
                        checked.add(k)
                    print((x,y))
                    self.visualize(checked)
        return islands
    def getAdjacent(self, p:tuple) -> list:
        adj = []
        if p[0] > 0: adj.append((p[0]-1, p[1]))
        if p[0] < (len(self.grid) - 1): adj.append((p[0]+1, p[1]))
        if p[1] > 0: adj.append((p[0], p[1]-1))
        if p[1] < (len(self.grid[0]) - 1): adj.append((p[0], p[1]+1))
        return adj
    def visualize(self, checked):
        v_grid = [row.copy() for row in self.grid]
        for key in checked:
            v_grid[key[0]][key[1]] = 'X'
        for row in v_grid: print(row)


if __name__ == '__main__':
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
    grid2 =[
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
    grid3 = [
        ["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]
    grid4 = [
        ["1","0","1","0","1"],
        ["1","1","0","1","0"],
        ["1","0","0","1","1"]]
    for row in grid4: print(row)
    print()
    islands = Solution().numIslands(grid3)
    print("Num islands:", islands)