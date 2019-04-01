# Perform Merge sort

nums = [4, 7, 5, 8, 2, 3, 1]





def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        Left = nums[:mid]
        Right = nums[mid:]

        mergeSort(Left)
        mergeSort(Right)
        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] > Right[j]:
                nums[k] = Right[j]
                j = j + 1
            else:
                nums[k] = Left[i]
                i = i + 1
            k += 1

        # Any remaining elements in L

        while i < len(Left):
            nums[k] = Left[i]
            i += 1
            k += 1

        # Any remaining elements in R
        while j < len(Right):
            nums[k] = Right[j]
            j += 1
            k += 1


        print nums

mergeSort(nums)
print(nums)
