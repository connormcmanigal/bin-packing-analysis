from binpacking import FirstFitDec, BestFitDec
import math
import random
import time

numlist=[0.90,0.75,0.70,0.63,0.48,0.35,0.29,0.19,0.07]

def find_closest(numbers, target=1.0):
    closest_num = None
    min_diff = float('inf')
    
    for num in numbers:
        if num < target:
            diff = target - num
            if diff < min_diff:
                closest_num = num
                min_diff = diff
    
    return closest_num

def summing(list):
    newlist=[]
    while list:
        if len(list) == 1:
            newlist.append(list[0])
            break
        target=round(1-list[0],2)
        closest=find_closest(list, target)
        newlist.append(round(list[0]+closest,2))
        del list[list.index(closest)]
        del list[0]
    return newlist

def group_items(items):
    # Define the size ranges
    ranges = [(0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1)]
    
    # Group items by size range
    grouped_items = {range_: [] for range_ in ranges}
    for item in items:
        for range_ in ranges:
            if range_[0] <= item < range_[1]:
                grouped_items[range_].append(item)
                break
    
    return grouped_items


data = [round(random.uniform(0.0,0.8), 2) for i in range(100)]

ranges_=[(0, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 1)]
grouped=group_items(data)
ffd=FirstFitDec()
for ranges_ in grouped:
    ffd.measure(grouped[ranges_])

# print(ffd.num_bins)
newlist=[]
for i in ffd.bins:
    newlist.append(sum(i))
print(newlist)
bfd=BestFitDec()
bfd.measure(newlist)
print(f'\nnew num buckets={bfd.num_bins}')
# print(ffd.waste)
print(f'optimal buckets={sum(data)}')
ffdz=FirstFitDec()
ffdz.measure(data)
print(f'FFD waste: {ffdz.waste[0]} \nFFD bins: {ffdz.num_bins}')
	

	