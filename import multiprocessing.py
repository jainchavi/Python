'''import multiprocessing
import time

def worker(num):
    """worker function"""
    print(f'Worker {num}')
    time.sleep(1)
    


if __name__ =='__main__':
    jobs = []
    for i in range (5):
        p = multiprocessing.Process(target = worker, args =(i,))
        jobs.append(p)
        p.start()
    for p in jobs:
        p.join()'''
      

#DATA SCIENCE----NUMBER CRUNCHING USING NUMPY

import numpy as np
OneD_arr = np.array([1,2,3,4,5])
print("1:D Array: \n", OneD_arr)

print(OneD_arr[2])

TwoD_arr = np.array(
                [
                    [1,2,3],
                    [4,5,6]
                    ]
                )
print("2:D Array: \n", TwoD_arr)

Three_D = np.array(
    [
        [
            [1,2,3],
            [4,5,6]
        ],
        [
            [7,8,9],
            [0,1,2]
        ]
    ]
)
print("3_D array: \n", Three_D)
print(Three_D[1][1][2])

#dimensions
print(OneD_arr.ndim)
print(TwoD_arr.ndim)
print(Three_D.ndim)