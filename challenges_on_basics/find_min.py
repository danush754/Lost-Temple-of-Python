def find_min(nums):
    min = float('inf')
    for value in nums:
        if(value <= min):
            min = value
    return min

print(find_min([43, 234, 65465, 234, 2343, 443, 2123, 8768]))