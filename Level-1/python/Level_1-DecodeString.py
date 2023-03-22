## 39 ms

class Solution:
    def decodeString(self, s: str) -> str:
        ## we use an iterator because it remembers its index current position 
        ## between recursions
        return self.recursion(s, iter(s))

    def recursion(self, s, iter) -> str:
        # each stack is unique of the init-end recursion span
        # iter remembers it's position.
        stack = []
        current_number = 0 

        for char in iter:
            if char.isdigit():
                # if two digits are next to each other:
                # first  digit -> units
                # second digit -> ten
                # --- so on    -> hundreds
                current_number =  current_number * 10 + int(char)
                print(current_number)
            elif char == '[':
                stack.append(current_number * self.recursion(s,iter))
                current_number = 0
            elif char == ']':
                break
            else:
                stack.append(char)

        return "".join(stack)

## 19ms

class Solution:
    def decodeString(self, s: str) -> str:
        stack,curnum, curstr = [], '', ''
        for i in s:
            if i=='[':
                stack.append(curstr)
                stack.append(int(curnum))
                curstr = ''
                curnum=''
            elif i == ']':
                num = stack.pop()
                prevstr= stack.pop()
                curstr = prevstr + num*curstr
            elif i.isdigit():
                curnum += i
            else:
                curstr += i
        return curstr