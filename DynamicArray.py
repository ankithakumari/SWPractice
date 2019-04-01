# Implementation of a dynamic array in python
# This is how a list operates in python

import ctypes

class DynamicArray(object):

	def __init__(self):
		self.n = 0
		self.capacity = 1
		self.arr = self.make_array(self.capacity)

	def __len__(self):
		return self.n

	def __get_item__(self, i):
		if i < n:
			return self.arr[i]
		else:
			return "Index out of range"

	def append(self, item):
		if self.n == self.capacity:
			self.capacity *= 2
			temp_arr = self.make_array(self.capacity)
			for i in range(self.n):
				temp_arr[i] = self.arr[i]
			self.arr = temp_arr
		 
		self.arr[self.n] = item
		self.n += 1


	def make_array(self, capacity):
		return (capacity * ctypes.py_object)()
		
