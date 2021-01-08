# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import multiprocessing as mp
import time
import pdb
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def howmany(row, left=4, right=8):
    count = 0
    for x in row:
        if left <= x <= right:
            count+= 1
    return count

def howmany_async(i, row, left = 4, right = 8):
    count = 0
    for x in row:
        if left <= x <= right:
            count+= 1
    return (i,count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    np.random.RandomState(100)
    data = np.random.randint(0,10,[5,100000]).tolist()

    results = []
    t0 = time.time()
    for row in data:
        results.append(howmany(row, 4,8))
    print(time.time()-t0)
    print(results[:10])


    pool_inst = mp.Pool(mp.cpu_count())
    t1 = time.time()
    resultsp = pool_inst.map(howmany, [row for row in data])
    print(time.time() - t1)
    print(resultsp[:10])

    results_async = []
    def collect_results(result):
        global results_async
        results_async.append(result)

    t3 = time.time()
    for i, row in enumerate(data):
        pool_inst.apply_async(howmany_async, args=(i, row, 4, 8), callback=collect_results)

    # Step 4: Close Pool and let all the processes complete
    pool_inst.close()
    pool_inst.join()
    print(time.time()-t3)
    print(results_async[:10])
    pdb.set_trace()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
