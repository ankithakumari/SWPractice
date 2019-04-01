"""Adding 1 to integers stored in a list """
import time
digits = [2, 8, 9, 9, 9 ,9, 9, 9, 9]

def addOne(digits):
	start = time.time()
	if digits == [9]*len(digits):
		return [1] + [0] * len(digits)
	elif digits[-1] == 9:
		j = len(digits) - 1
		while(digits[j] == 9):
			digits[j] = 0
			j -= 1
		digits[j] += 1
	else:
		digits[-1] += 1
	end = time.time()
	print(end-start)
	return digits

#print(addOne(digits))

#If we were to use join and split

def addOneAsInteger(digits):
	start = time.time()
	s = [str(i) for i in digits]
	r = int(''.join(s))
	r = r + 1
	end = time.time()
	print(end-start)
	return [int(i) for i in str(r)]


#print(addOneAsInteger(digits))

# - Faster! 
# worst case - O(n) when all n digits are 9

def OnePlus(digits):
	for i in reversed(range(len(digits))):
		if digits[i] == 9:
			digits[i] = 0
		else:
			digits[i] += 1
			return digits
	return [1] + digits

print(OnePlus(digits))

