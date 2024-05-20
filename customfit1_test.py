import binpacking
import random
import time
import pandas as pd

names = ['NextFit', 'FirstFit', 'BestFit', 'CustomFit1']

packer = [None]*4
packer[0] = binpacking.NextFit()
packer[1] = binpacking.FirstFit()
packer[2] = binpacking.BestFit()
packer[3] = binpacking.CustomFit1()

algo_df = pd.DataFrame(columns = ['Algos', 'Data Size', 'Waste', 'Runtime'])
seeds = [123, 234, 345, 456, 567]

for exp_num in range(5):
    DATA_SIZE = 50
    NUM_EXP = 9
    data = []   
    random.seed(seeds[exp_num])
    for j in range(NUM_EXP):
        DATA_SIZE = DATA_SIZE * 2
        data = []
        for i in range(DATA_SIZE):
            data.append(round(random.uniform(0.0,0.8), 8))

        data_save = data.copy()

        # Uniformly distributed data
        for i in range(len(packer)):
            packer[i].reset()
            data = data_save.copy()
            start_time = time.perf_counter()
            packer[i].measure(data)
            end_time = time.perf_counter()
            packer[i].times.append(end_time - start_time)

        for i in range(len(packer)):
            waste=[]
            waste=[f'{names[i], exp_num}', DATA_SIZE,packer[i].waste[0], packer[i].times[0]]
            algo_df = algo_df._append(pd.Series(waste, index=algo_df.columns), ignore_index=True)
    
print(algo_df)
algo_df.to_csv('cf1_results.csv', index = False)

print('done')