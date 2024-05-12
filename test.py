from binpacking import BestFitDec, BestFit, CustomFit1
import math
import random

data = []
for i in range(100):
    data.append(round(random.uniform(0.0,0.8), 8))

bfd = BestFitDec()
cf1 = CustomFit1()
waste2 = bfd.measure(data)
waste3 = cf1.measure(data)
print("Optimal # bins:", math.ceil(sum(data)))
print()
print("BFD bin assignments:", bfd.bins)
print("BFD # Bins:", bfd.num_bins)
print()
print("CF1 bin assignments:", cf1.bins)
print("CF1 # Bins:", cf1.num_bins)
print()
print("wastes = ", "BFD:", waste2, "CF1:", waste3)

