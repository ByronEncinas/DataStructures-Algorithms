
""" 
Input: n = 4
Output:
[
    ['.Q..','...Q','Q...','..Q.'], -> [2,4,1,3]
    ['..Q.','Q...','...Q','.Q..']  -> [3,1,4,2]
]
 """
class Solution:
    """
    example on the left: [1, 3, 0, 2]
    example on the right: [2, 0, 3, 1]
    """
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
        
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        # create a state array of length n if state = []
        if not state:
            return range(n)
        
        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))
        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):

        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            state_diagram = self.state_to_diagram(state, n)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def state_to_string(self, state, n):
        # ex. [1, 3, 0, 2]
        # output: [".Q..","...Q","Q...","..Q."]

        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret

    def state_to_diagram(self, state, n):
        
        row_diagram = dict()
        diagram = []
        count = 0
        for i in state: # state being: [1,3,0,2]
            count += 1        
            row_diagram['{} -'.format(count)] = ' [ ] ' * i + ' [Q] ' + ' [ ] ' * (n - i - 1)

            diagram.append(row_diagram)
            # print(string)
            # if count == n:
            # print('--------   |    |    |    |    |    |    |    | ')
            # print('--------   A    B    C    D    E    F    G    H ')
        return 

if __name__ == '__main__':
    four = Solution()
    string = four.solveNQueens(n=4)
    for i in string:
        print(i)
    
    
    