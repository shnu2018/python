def binary_search(data, k):
    low, high = 0, len(data) - 1
    
    import pdb        # 插入pdb调试代码
    pdb.set_trace()
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid] < k:
            low = mid + 1
        elif data[mid] > k:
            high = mid - 1
        else:
            return mid
    return -1

data = [3, 4, 5, 6, 6, 8, 9, 100]
rs = binary_search(data, 9)
print("hello")
print(rs)
