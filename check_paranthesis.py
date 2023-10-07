class Solution:
    def ispar(self,x):
      stack = []
        for i in x:
            if i in "{([":
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if i =='}' and stack[-1]=='{':
                        stack.pop()
                    elif i ==')' and stack[-1]=='(':
                        stack.pop()
                    elif i ==']' and stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
        return not stack
        
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
