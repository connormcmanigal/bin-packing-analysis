# explanations for member functions are provided in requirements.py

import random as rand
import math 
from collections.abc import Iterable

# Use the provided Merge Sort for sorting

class MergeSort:
	def __init__(self):
		self.time = 0

	def sort(self, data):
		sorted_data = self.sortHelper(data, 0, len(data))
		return sorted_data

	def sortHelper(self, data, low, high):
		if high - low > 1:
			mid = low + (high-low)//2
		
			self.sortHelper(data, low, mid)	
			self.sortHelper(data, mid, high)
			self.merge(data, low, mid, high)

	def merge(self, data, low, mid, high):
		temp = []
		
		i = low
		j = mid

		while (i < mid and j < high):
			if data[i] > data[j]: 	# fixed to return decreasing
				temp.append(data[i])
				i += 1
			else:
				temp.append(data[j])
				j += 1
		while (i < mid):
			temp.append(data[i])
			i += 1
		while (j < high):
			temp.append(data[j])
			j += 1
		for k in range(len(temp)):
			data[k+low] = temp[k] 

# Implement the Next Fit Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class NextFit:
	def __init__(self):
		self.bins = []
		self.waste = []
		self.times = []
		self.num_bins = 0

	def reset(self):
		self.bins = []
		self.waste = []
		self.times = []
		self.num_bins = 0

	def measure(self, data):
		optimal = sum(data) / 1.0
		self.num_bins = self.pack(data)
		waste = self.num_bins - optimal
		self.waste.append(waste)
		return waste

	def pack(self, data):
		self.bins.append([])
		self.num_bins = 1
		for i in data:
			current = self.bins[-1]
			current_size = sum(current)
			if current_size + i <= 1.0:
				current.append(i)
			else:
				self.bins.append([i])
				self.num_bins += 1
		return self.num_bins

# Implement the First Fit Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class FirstFit:
	def __init__(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1

	def measure(self, data):
		optimal = sum(data) / 1.0
		self.num_bins = self.pack(data)
		waste = self.num_bins - optimal
		self.waste.append(waste)
		return waste

	def pack(self, data):
		for i in data:
			added=False
			for j in range(len(self.bins)):
				if self.bin_sums[j] + i <= 1.0:
					self.bins[j].append(i)
					self.bin_sums[j] += i
					added=True
					break
			if not added:
				self.bins.append([i])
				self.bin_sums.append(i)
				self.num_bins += 1
		return self.num_bins

# Implement the Best Fit Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class BestFit:
	def __init__(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1

	def measure(self, data):
		optimal = sum(data) / 1.0
		self.num_bins = self.pack(data)
		waste = self.num_bins - optimal
		self.waste.append(waste)
		return waste

	def pack(self, data):
		for i in data:
			min_space = float('inf')
			min_bin_ind = -1

			for bin_ind in range(len(self.bins)):
				bin_sum = sum(self.bins[bin_ind])
				bin_space = 1.0 - bin_sum
				if i <= bin_space and bin_space < min_space:
					min_space = bin_space
					min_bin_ind = bin_ind

			if min_bin_ind == -1:
				self.bins.append([i])
				self.bin_sums.append(i)
				self.num_bins += 1
			else:
				self.bins[min_bin_ind].append(i)
				self.bin_sums[min_bin_ind] += i
		
		return self.num_bins
	
# Implement the First Fit Decreasing Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
#	sorter:		sorting object
# 	packer:		bin packing object
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class FirstFitDec:
	def __init__(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = FirstFit()

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = FirstFit()

	def measure(self, data):
		self.sorter.sort(data)
		waste = self.packer.measure(data)
		self.bins = self.packer.bins
		self.bin_sums = self.packer.bin_sums
		self.waste = self.packer.waste
		self.times = self.packer.times
		self.num_bins = self.packer.num_bins
		return waste

# Implement the Best Fit Decreasing Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
#	sorter:		sorting object
# 	packer:		bin packing object
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class BestFitDec:
	def __init__(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = BestFit()

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = BestFit()		

	def measure(self, data):
		self.sorter.sort(data) 
		waste = self.packer.measure(data)
		self.bins = self.packer.bins
		self.bin_sums = self.packer.bin_sums
		self.waste = self.packer.waste
		self.times = self.packer.times
		self.num_bins = self.packer.num_bins
		return waste

# Implement a Custom Fit Bin Packing Algorithm
# 	The goal is to modify the best performing (fewest bins) algorithm
# 	to try to improve the packing (number of bins) for at least 1 set of the standard input data.
#	HINT: 		try modifying data after sorting 
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
#	sorter:		sorting object
# 	packer:		bin packing object
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class CustomFit1:
    def __init__(self, threshold = 0.15):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.threshold = threshold
        self.sorter = MergeSort()      

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
    
    def pack(self, data):
        for elem in data:
            for bin_index, contents in enumerate(self.bins):
                space_left = 1.0 - sum(contents)
                if space_left >= elem:
                    if space_left >= self.threshold:
                        self.bins[bin_index].append(elem)
                        break
                    else:
                        continue
            else:
                self.bins.append([elem])
                self.num_bins += 1

    def measure(self, data):
        self.reset()
        self.pack(data)
        optimal = sum(data) / 1.0
        waste = self.num_bins - optimal
        self.waste.append(waste)
        return waste
	

class CustomFit1Sorted(CustomFit1):
    def measure(self, data):
        self.reset()
        self.sorter.sort(data)
        self.pack(data)
        optimal = sum(data) / 1.0
        waste = self.num_bins - optimal
        self.waste.append(waste)
        return waste


class CustomFit2:
	def __init__(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = BestFit() # TODO: Use the best bin packing algorithm based on the test data 

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = BestFit() # TODO: Use the best bin packing algorithm based on the test data 

	def modify(self, data):
		modified_data=[]
		group_size=len(data) // 3

		small_items=data[-group_size:]
		small_group=[sum(small_items)]
		modified_data=data[:group_size]+small_group
		return modified_data

	def measure(self, data):
		# TODO: Sort Data
		self.sorter.sort(data)
		# Implement Optimization
		data=self.modify(data)
		waste = self.packer.measure(data)
		self.bins = self.packer.bins
		self.bin_sums = self.packer.bin_sums
		self.waste = self.packer.waste
		self.times = self.packer.times
		self.num_bins = self.packer.num_bins
		return waste
	
	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define