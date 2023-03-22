## My Solution

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        self.rows, self.columns = len(grid), len(grid[0]) ## using inheritance

        return self.IslandSearch(grid, dict())

    def IslandSearch(self, grid, hashTable: dict) -> int:
        ## this will look, add and return all 1's conected to every island
        count = 0
        for i in range(self.rows):
            for j in range(self.columns):
                stringCoords = '%s %s' % (i,j)
                if grid[i][j] == "1" and stringCoords not in hashTable:
                    count += 1
                    #start depth_first_search
                    self.scavenge_island(grid, hashTable, i, j)
        return count

    def scavenge_island(self, grid, hashTable, i, j):
        # we have found grid[i,j] = 1
        # we want to find all pairs (x,y) with form the island
        stringCoords = '%s %s' % (i,j) # <- stringForm key for coordinates of the point
        if i < 0 or j < 0 or i >= self.rows or j >= self.columns:
            return        
        if grid[i][j] == "0":
            return
        if stringCoords not in hashTable:
            hashTable[stringCoords] = True # <- visited
            self.scavenge_island(grid, hashTable, i + 1, j)
            self.scavenge_island(grid, hashTable, i - 1, j)
            self.scavenge_island(grid, hashTable, i, j + 1)
            self.scavenge_island(grid, hashTable, i, j - 1)

## Best Runtime

class Solution1:
    def numIslands(self, grid: list[list[str]]) -> int:
        componentCounter = 0 
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j): 
            grid[i][j] = -1 # mark the curent node as 'visited' 
            if (i < m - 1 and grid[i + 1][j] == "1"): 
                dfs(i + 1, j)
            if (i > 0 and grid[i - 1][j] == "1"): 
                dfs(i - 1, j)
            if (j < n - 1 and grid[i][j + 1] == "1"): 
                dfs(i, j + 1)
            if (j > 0 and grid[i][j - 1] == "1"): 
                dfs(i, j - 1)
        
        for k in range(m): 
            for l in range(n): 
                if grid[k][l] == "1": 
                    componentCounter += 1
                    dfs(k, l)
        return componentCounter

## Best Memory

class Solution2:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)