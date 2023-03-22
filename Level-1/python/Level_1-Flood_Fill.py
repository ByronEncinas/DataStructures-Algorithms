#https://leetcode.com/problems/flood-fill/solutions/3188583/simple-recursive-solution-in-python/

class Solution:
    def floodFill(self, image, sr, sc, color):
        
        self.flood(image, sr, sc, len(image), len(image[0]), image[sr][sc], color)
        
        return image
    
    def flood(self, image, sr, sc, rows, columns, color, new_color):
        
        if (sr < 0) or (sr >= rows) or (sc < 0) or (sc >= columns):
            return
        if image[sr][sc] != color or image[sr][sc] == new_color:
            return
            
        image[sr][sc] = new_color
            
        self.flood(image, sr+1, sc, rows, columns, color, new_color)
        self.flood(image, sr-1, sc, rows, columns, color, new_color)
        self.flood(image, sr, sc+1, rows, columns, color, new_color)
        self.flood(image, sr, sc-1, rows, columns, color, new_color)

        """
        Input: 
            image = [ [1,1,1],
                      [1,1,0],
                      [1,0,1] ], 
        
        Method:        
            start position = (sr,sc) = (1,1)
            1st Iteration 
                    - change color of horizontal and verical 
                      colors equal to prev color
            image = [ [1,2,1],
                      [2,2,0],
                      [1,0,1] ], 
            Now, (sr,sc) -> two possibilities: (1,0) and (0,1)
            2nd iteration 
            - branch to (sr,sc) = (1,0)
                1st branch (sr,sc) = (1,0)
                    - change color of horizontal and verical 
                      colors equal to prev color
                    image = [ [2,2,1],
                              [2,2,0],
                              [2,0,1] ], 
                return to 2nd iteration
            - branch to (sr,sc) = (0,1)
                2nd branch (sr,sc) = (0,1)
                    - change color of horizontal and verical 
                      colors equal to prev color
                    image = [ [2,2,2],
                              [2,2,0],
                              [2,0,1] ], 
            No more branching to be done. Finish
        Output:
            image = [ [2,2,2],
                      [2,2,0],
                      [2,0,1] ]
        """