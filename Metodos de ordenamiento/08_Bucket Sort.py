def bucket_sort(arr):
    if not arr:
        return []
    bucket_count = 10
    max_val = max(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int(num / max_val * (bucket_count - 1))
        buckets[index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(insertion_sort(bucket))
    return sorted_arr
