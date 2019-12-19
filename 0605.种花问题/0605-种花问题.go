func canPlaceFlowers(flowerbed []int, n int) bool {
    arr := make([]int, len(flowerbed)+2)
    arr[0] = 0
    copy(arr[1:], flowerbed)
    arr[len(arr)-1] = 0
    // fmt.Println(arr)
    count := 0
    i := 1
    for i < len(arr)-1 {
        if arr[i-1] == 0 && arr[i] == 0 && arr[i+1] == 0 {
            arr[i] = 1
            count += 1
            if count >= n {
                return true
            }
        }
        i += 1
    }
    
    return count >= n
}