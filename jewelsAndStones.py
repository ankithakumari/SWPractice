""" You're given strings J representing the types of stones 
that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, 
and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a 
different type of stone from "A". """
import time

j = "acCdDxXhH"
s = "ccggggggjjjjjjrrrrttttthhhbbnnkkuussddffhhaaaaAAAAbbbb"

#Expected output 4
# One way would be to count each jewel in s by traversing through j
# Complexity would be O(len(j))



def countJewels(j, s):
	start = time.time()
	jcount = 0
	for jewel in j:
		jcount += s.count(jewel)
	end = time.time()

	print(start-end)
	return jcount

print(countJewels(j,s))


