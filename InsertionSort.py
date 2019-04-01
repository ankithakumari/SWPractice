#Function to perform insertion sort
#Takes an array input and returns a sorted array

nums = [99, 78]


def insertionSort(nums):
	for i in range(1, len(nums)):
		num = nums[i]
		j = i - 1
		while j >= 0 and num < nums[j]:
			nums[j+1] = nums[j]
			j = j - 1

		nums[j+1] = num
	
	return nums


print(insertionSort(nums))