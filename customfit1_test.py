import binpacking
import random
import time
import pandas as pd

names = ['FirstFit' ,'CustomFit1', 'CustomFit1Sorted']

packer = [None]*3
packer[0] = binpacking.FirstFit()
packer[1] = binpacking.CustomFit1()
packer[2] = binpacking.CustomFit1Sorted()

algo_df = pd.DataFrame(columns = ['Algos', 'Data Size', 'Waste', 'Runtime'])
seeds = [123, 234, 345, 456, 567]

for exp_num in range(5):
    DATA_SIZE = 50
    NUM_EXP = 9
    data = []   
    random.seed(seeds[exp_num])
    for j in range(NUM_EXP):
        # print()
        DATA_SIZE = DATA_SIZE * 2
        # print("DATA_SIZE:", DATA_SIZE)
        data = []
        for i in range(DATA_SIZE):
            data.append(round(random.uniform(0.0,0.8), 8))

        data_save = data.copy()

        # Uniformly distributed data
        for i in range(len(packer)):
            packer[i].reset()
            # print(names[i])
            data = data_save.copy()
            start_time = time.perf_counter()
            packer[i].measure(data)
            end_time = time.perf_counter()
            packer[i].times.append(end_time - start_time)

        # print()
        # print("Uniformly Distributed Random Data Waste: ")
        for i in range(len(packer)):
            waste=[]
            # print(names[i])
            waste=[f'{names[i], exp_num}', DATA_SIZE,packer[i].waste[0], packer[i].times[0]]
            algo_df = algo_df._append(pd.Series(waste, index=algo_df.columns), ignore_index=True)
            # print(names[i], packer[i].waste)

        # print()
        # print("Uniformly Distributed Random Data Time: ")
        # for i in range(len(packer)):    
            # print(names[i], packer[i].times)
    
print(algo_df)
algo_df.to_csv('cf1_results.csv', index = False)

print('done')