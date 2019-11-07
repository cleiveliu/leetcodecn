import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        pat = r"[+-]{0,1}[\d*x*]+"
        left = re.findall(pat, left)
        right = re.findall(pat, right)
        l = [0,0] #[x,num]
        r = [0,0]
        #print(left,right)
        for i in left:
            if 'x' in i:
                temp = i.replace('x','')
                temp = temp.strip()
                if ('+' in temp or '-' in temp) and len(temp) == 1:
                    if '+' in temp:
                        l[0] += 1
                    else:
                        l[0] += -1
                elif len(temp) == 0:
                    l[0] += 1
                else:
                    l[0] += int(temp)
                    
            else:
                l[1] += int(i)
        for i in right:
            if 'x' in i:
                temp = i.replace('x','')
                temp = temp.strip()
                if ('+' in temp or '-' in temp) and len(temp) == 1:
                    if '+' in temp:
                        r[0] += 1
                    else:
                        r[0] += -1
                elif len(temp) == 0:
                    r[0] += 1
                else:
                    r[0] += int(temp)
            else:
                r[1] += int(i)
        xs = l[0] - r[0]
        nums = r[1] - l[1]
        #print(xs,nums)
        if xs == 0 and nums == 0:
            return "Infinite solutions"
        elif (xs == 0 and nums != 0):
            return "No solution"
        else:
            return f"x={nums//xs}"
            