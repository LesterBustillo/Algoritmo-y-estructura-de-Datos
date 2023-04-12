def find_runs(arr):
    n = len(arr)
    start = 0
    increasing = True
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            if increasing:
                yield (start, i-1)
                increasing = False
                start = i-1
        else:
            if not increasing:
                yield (start, i-1)
                increasing = True
                start = i-1
    if increasing:
        yield (start, n-1)
    else:
        yield (start, n-1)


def merge_runs(arr, start1, end1, start2, end2):
    if arr[end1] <= arr[start2]:
        return
    mid = bisect.bisect_right(arr, arr[start2], start1, end1)
    len1, len2 = mid-start1, end2-start2+1
    if len1 < len2:
        arr[start2+len1:end2+1], arr[start1:start2+len1] = arr[start1:end1+1], arr[start2:end2+1]
    else:
        arr[start1:end1-mid+start2+1], arr[mid:end2+1] = arr[start2:end2+1], arr[start1:end1-mid+start2+1]


def timsort(arr):
    for start, end in find_runs(arr):
        for start2, end2 in find_runs(arr[start:end+1]):
            merge_runs(arr, start, end, start+start2, start+end2)
    return arr
