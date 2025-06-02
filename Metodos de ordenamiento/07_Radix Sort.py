def radix_sort(arr):
    if not arr:
        return []
    max_len = len(str(max(arr)))
    for exp in range(max_len):
        bins = [[] for _ in range(10)]
        for num in arr:
            bins[(num // (10 ** exp)) % 10].append(num)
        arr = [num for bucket in bins for num in bucket]
    return arr
