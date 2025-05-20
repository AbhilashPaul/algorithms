def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid_point = len(nums) // 2
    left_half = nums[:mid_point]
    right_half = nums[mid_point:]
    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)
    return merge(left_half_sorted, right_half_sorted)
    
def merge(first, second):
    result = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    if i < len(first):
        result = result + first[i:]
    if j < len(second):
        result = result + second[j:]
    return result

