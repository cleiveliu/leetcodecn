class Solution:
    def fractionToDecimal(self, up: int, down: int) -> str:
        # up/down
        if up == 0:
            return "0"
        if down == 0:
            raise ValueError("fuck")
        flag = "" if up*down >= 0 else "-"
        up, down = abs(up), abs(down)
        
        ret = []
        while up >= down:
            ret.append(up//down)
            up = up % down
            if up == 0:
                return flag + ''.join(map(str, ret))
        if len(ret) == 0:
            ret.append(0)
        ret.append(".")
        pre = up*10
        pre_len = len(ret)
        record = []
        pres = set()
        
        while True:
            record.append((len(ret), pre))
            pres.add(pre)
            if pre >= down:
                ret.append(pre//down)
                pre = (pre%down)*10
                if pre == 0:
                    return flag + ''.join(map(str, ret))
                if pre in pres:
                    index = None
                    for k,v in record:
                        if v == pre:
                            index = k
                            break
                    return flag + ''.join(map(str, ret[:index])) + "(" + ''.join(map(str, ret[index:])) + ")"
                if len(ret) - pre_len > 1000_000:
                    return flag + ''.join(map(str, ret))
                
            else:
                pre = pre*10
                ret.append(0)
            
        
        