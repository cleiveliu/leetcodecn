class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        arr = [0] + flowerbed + [0]
        i = 1 
        count = 0
        while i < len(arr)-1:
            if arr[i-1] == 0 and arr[i] == 0 and arr[i+1] == 0:
                arr[i] = 1
                count += 1
                if count >= n:
                    return True
            i += 1
        return count >= n