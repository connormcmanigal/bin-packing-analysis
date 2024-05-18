from binpacking import FirstFitDec, CustomFit1
import math
import random

data = []
for i in range(100):
    data.append(round(random.uniform(0.0,0.8), 2))

ffd = FirstFitDec()
cf1 = CustomFit1()
waste2 = ffd.measure(data)
waste3 = cf1.measure(data)
print("Optimal # bins:", math.ceil(sum(data)))
print()
print("FFD bin assignments:", ffd.bins)
print("FFD # Bins:", ffd.num_bins)
print()
print("CF1 bin assignments:", cf1.bins)
print("CF1 # Bins:", cf1.num_bins)
print()
print("wastes = ", "FFD:", waste2, "CF1:", waste3)

