class Solution:
    def simplifyPath(self, path: str) -> str:
        # define search paradigm
        # we will traverse the path and .append()
        # to a result list
        pathList = path.split('/')
        directoryNames = [] # delete all slash
        doubleLoc = []
        for char in pathList:
            if char != '.':
                if char != '':
                    directoryNames.append(char) 

        # directoryNames is not modified here, method with no real effect on result
        locIndex, loclocIndex = 0, 0
        for index, elem in enumerate(directoryNames):
            if elem == '.':
                locIndex = index
            if elem == '..':
                doubleLoc.append(index)
                loclocIndex = index
        
        # Now I can discriminate based on the last '..' element in directoryNames
        # since I know it's on locIndex position

        absPath = []
        # ignore all '.'
        # if directoryNames[index] = '..' then eliminate directoryNames[index] and directoryNames[index - 1]
        pos_min, pos_max = 0, len(directoryNames) - 1
        
        # three options -> ['..', --] or ['a', '..', --] or ['a', 'b', '..', or in greater than index = 1 position]
        # if '..' at index = 0 then eliminate index 0 elements and continue
        # if '..' at index = 1 eliminate index 1 and 0 

        for index, elem in enumerate(directoryNames):
            absPath.append(elem) ## append current element
            if elem == '..':
                loc = absPath.index('..')
                if loc != 0:
                    absPath.pop(loc)
                    absPath.pop(loc - 1)
                else:
                    absPath.pop(0)

        return '/' + "/".join(absPath)

""" 
path = "/a/./b/../../c/d/f/../h   --> ['a','.','b','..','..','c','d','f','..','h'] "
from left to right
'/a/. -- ' <-- stay at 'a' folder --> ['a','b','..','..','c','d','f','..','h']
new_path = "/a/b/.. --" double dot, go to 'a' --> ['a','..','c','d','f','..','h']
new_path = "/a/../../c/d/f/../h" double_dot go to start of path  --> ['c','d','f','..','h']
new_path = "/../c/d/f/../h" double_dot go to start of path --> ['c','d','f','..','h']
new_path = "/c/d/f/../h" double_dot go to  --> ['c','d','f','..','h']
new_path = "/c/d/f/.. --" double_dot go to 'd' --> ['c','d','h']
new_path = "/c/d/h" no more dots or double dots --> ['c','d','h']
return new_path = "/"+"".join(['c','d','h'])
"""

# 40 ms

class Solution:
    def simplifyPath(self, path: str) -> str:
        # define search paradigm
        # we will traverse the path and .append()
        # to a result list
        pathList = path.split('/')
        directoryNames = [] # delete all slash

        self.filtrate(pathList, directoryNames)
        # def filtrate
        # input: pathList
        # output: directoryNames

        absPath = []
        pos_min, pos_max = 0, len(directoryNames) - 1
        self.depure(absPath, directoryNames)
        # def depure
        # input: directoryNames
        # output: absPath 

        return '/' + "/".join(absPath)
    
    def filtrate(self, pathList: list, directoryNames: list):
        for char in pathList:
            if char != '.':
                if char != '':
                    directoryNames.append(char)

    def depure(self, absPath: list, directoryNames: list):

        for index, elem in enumerate(directoryNames):
            absPath.append(elem) ## append current element
            if elem == '..':
                loc = absPath.index('..')
                if loc != 0:
                    absPath.pop(loc)
                    absPath.pop(loc - 1)
                else:
                    absPath.pop(0)

## 15 ms

class Solution2:
    def simplifyPath(self, path: str) -> str:
        # data structure: pop() last item in 
        stack = []
        print(path.split('/'))
        
        # path.split('/') = ["", "Folder", "", "Subfolder", "", ...]
        for directory in path.split('/'):
            
            if directory == "" or directory == ".": 
                # if "" or "." don't add to the stack
                continue
            elif directory == "..": 
                # if ".." don't add to the stack and eliminate current last
                if stack: stack.pop()
            else:
                # if directory is indeed a folder
                stack.append(directory)
        
        return f"/{'/'.join(stack)}"


