from binpacking import BestFitDec, BestFit, CustomFit1

data = [0.4, 0.5, 0.25, 0.6, 0.2, 0.05, 0.45, 0.8, 0.65, 0.75]
print(sum(data))
bf = BestFit()
bfd = BestFitDec()
cf1 = CustomFit1()
waste1 = bf.measure(data)
waste2 = bfd.measure(data)
waste3 = cf1.measure(data)
print("BF:", waste1, "BFD:", waste2, "CF1:", waste3)

