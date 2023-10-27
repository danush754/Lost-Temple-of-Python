def rem_non_int(nums):
    changed_list = []
    for value in nums:
        if(type(value) == int):
            changed_list.append(value)
        else:
            continue
    return changed_list
    

print(rem_non_int([300, 300, 2, False, "otherstring", 6, {}, 16]))

