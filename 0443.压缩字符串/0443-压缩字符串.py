class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        cnt = 0
        cur = 0
        while cur < len(chars):
            pre = chars[cur]
            cur += 1
            cnt += 1
            while cur < len(chars) and chars[cur] == pre:
                cur += 1
                cnt += 1
            if cnt > 1:
                str_nums = list(str(cnt))
                chars[index] = pre
                index += 1
                chars[index:index+len(str_nums)] = str_nums
                index += len(str_nums)
            else:
                chars[index] = pre
                index += 1
            cnt = 0
        return index