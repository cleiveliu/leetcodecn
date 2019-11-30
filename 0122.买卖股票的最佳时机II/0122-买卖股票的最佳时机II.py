class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def window(arr, n=2):
            pre = arr[0]
            for a in arr[1:]:
                yield pre, a
                pre = a

        return sum(max(cur - pre, 0) for pre, cur in window(prices)) if prices else 0
