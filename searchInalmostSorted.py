

def search(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if target == nums[i]:
            return i
        elif target == nums[j]:
            return j
        else:
            mid = i + (j - i) // 2
            if target >= nums[mid] or target < nums[j]:
                i = mid
                j -= 1
            elif nums[i] < target <= nums[mid]:
                j = mid
                i += 1
            else:
                return -1
    return -1

nums = [4,5,6,7,0,1,2]
print(search(nums, 1))

