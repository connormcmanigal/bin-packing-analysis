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
	def __init__(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
	
	def find_pairs(self, data):
		left = 0
		right = len(data) - 1
		pairs = []
		used_indices = set()
		
		while left < right:
			if left in used_indices:
				left += 1
				continue
			if right in used_indices or right <= left:
				right -= 1
				continue
			
			sum_pair = data[left] + data[right]
			if sum_pair > 1.0:
				left += 1
			elif 0.95 <= sum_pair <= 1.0:
				pairs.append((data[left], data[right]))
				used_indices.add(left)
				used_indices.add(right)
				left += 1
				right -= 1
			elif sum_pair < 0.95:
				right -= 1
		return pairs, used_indices
	
	def pack_first_fit(self, remaining):
		for item in remaining:
			placed = False
			for bin_index, contents in enumerate(self.bins):
				if sum(contents) + item <= 1.0:
					self.bins[bin_index].append(item)
					placed = True
					break
			if not placed:
				self.bins.append([item])
				self.num_bins += 1
			
	def pack_pairs(self, pairs):
		for pair in pairs:
			placed = False
			for bin_index in range(len(self.bins)):
				bin_space = 1.0 - sum(self.bins[bin_index])
				pair_sum = sum(pair)
				if pair_sum <= bin_space:
					self.bins[bin_index].extend(pair)
					placed = True
					break
			if not placed:
				self.bins.append(list(pair))
				self.num_bins += 1

	def pair_pack(self, data):
		paired_items, used_indexes = self.find_pairs(data)
		remaining = [data[i] for i in range(len(data)) if i not in used_indexes]
		self.pack_pairs(paired_items)
		self.pack_first_fit(remaining)
	
	def measure(self, data):
		self.reset()
		self.pair_pack(data)
		optimal = sum(data) / 1.0
		waste = self.num_bins - optimal
		self.waste.append(waste)
		return waste
	
	
class CustomFit1Sorted(CustomFit1):
    def pair_pack(self, data):
        self.sorter.sort(data)
        paired_items, used_indexes = self.find_pairs(data)
        remaining = [data[i] for i in range(len(data)) if i not in used_indexes]
        self.pack_pairs(paired_items)
        self.pack_first_fit(remaining)


class CustomFit2:
	def __init__(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = None # TODO: Use the best bin packing algorithm based on the test data 

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = None # TODO: Use the best bin packing algorithm based on the test data 

	def measure(self, data):
		# TODO: Sort Data
		
		# Implement Optimization
  
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