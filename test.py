from binpacking import NextFit

data = [0.4, 0.3, 0.6, 0.41, 0.8, 0.3]
print(sum(data))
nf = NextFit()

waste = nf.measure(data)
print(waste)

