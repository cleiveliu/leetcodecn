class Solution:
    def calculate(self, s: str) -> int:
        ops = "+-*/"
        s = s.replace(' ', '')
        theops = []
        thenums = []
        index = 0
        while index < len(s):
            tem = s[index]
            while index + 1< len(s) and s[index+1] not in ops:
                index += 1
                tem += s[index]
            thenums.append(tem)
            index += 1
            if index < len(s):
                theops.append(s[index])
                index += 1
        #print(thenums)
        #print(theops)
        s = [' '.join([num, op]) for num, op in zip(thenums, theops)]
        
        s.append(thenums[-1])
        
        s = ' '.join(s)
        
        return Calculator().evaluate(s)

# my solution on codewars
class Calculator(object):
    def evaluate(self, string:str):
        #eaxmple Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
        operators={
            "-":lambda x,y:x-y,
            "+":lambda x,y:x+y,
            "/":lambda x,y:x//y,
            "*":lambda x,y:x*y
        }
        
        lst=string.split(' ')
        lst=map(lambda x: int(x) if x not in operators.keys() else x, lst)
        
        def is_num(x):
            return type(x)==int or type(x)==float
        def is_second_level(x):
            return x in ("-","+")
        def is_top_level(x):
            return x in ("/","*")
        
        stack=[]
        for x in lst:
            if is_num(x):
                if stack and is_top_level(stack[-1]):
                    opt=stack.pop()
                    y=stack.pop()
                    tem=operators[opt](y,x)
                    stack.append(tem)
                else:
                    stack.append(x)
            elif is_second_level(x):
                mark=x
                if len(stack)==3:
                    x=stack.pop()
                    opt=stack.pop()
                    y=stack.pop()
                    tem=operators[opt](y,x)
                    stack.append(tem)
                stack.append(mark)
            elif is_top_level(x):
                stack.append(x)
        res=0
        if len(stack)==3:
            x=stack.pop()
            opt=stack.pop()
            y=stack.pop()
            res=operators[opt](y,x)
        elif len(stack)==1:
            res=stack[-1]
        
        return res