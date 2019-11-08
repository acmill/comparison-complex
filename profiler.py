##  For profiling any of the algorithms

import os
import io
import random
import csv
import bisect
import itertools
from time import process_time, perf_counter

from algorithms import insertionsort
from algorithms import quicksort
from algorithms import hybridsort

from structures import node


#   Get the data from file (file is 20K random numbers)
def GetData(fName, N):

    #   Concatenate the filestring in order to access it
    fName = 'input/' + fName
    f = open(fName, 'r+')
    data = f.read()
    f.close()

    #   Convert into integers
    data = [int(i) for i in data.strip().split()]

    #   Return the data with the proper list size
    return(data[0:N])



#   Receives: name of algorithm, type of input, 
#             initial and final N of input, n repeats
#   Returns: a list of elapsed execution times
def Execute(algo, dist, iN, N, repeats):

    #   The data we are about to manipulate
    data = []
    dataItems = []
    algoName = ""
    n = iN

    #   Check whether to return an almost sorted or random list
    if(dist == "as"):
        fileName = "as20k.in"
        data = GetData(fileName, n)
        dist = "Almost Sorted"
    else:
        fileName = "r20k.in"
        data = GetData(fileName, n)
        dist = "Random"

    while ( n < N + 5):
         #   The list of runtimes for list size N
        executionTimes = []

        #   We have insertion sort
        if(algo == 1):
            algoName = "Insertion Sort"
            executionTimes = ExecuteInsertionSort(data, repeats)
            
        #   We have quick sort
        elif(algo == 2):
            algoName = "QuickSort"
            executionTimes = ExecuteQuickSort(data, repeats)

        #   We have hybrid sort
        elif(algo == 3):
            algoName = "Hybrid Sort"
            executionTimes = ExecuteHybridSort(data, repeats)

        #   We have hash table insertion
        elif(algo == 4):
            algoName = "Hash Table (Insertion)"
            executionTimes = ExecuteHashTableInsert(data, repeats)


        #   We have BST insertion
        elif(algo == 5):
            algoName = "BST (Insertion)"
            executionTimes = ExecuteBSTInsert(data, repeats)

        #   We have Sorted Vector insertion
        elif(algo == 6):
            algoName = "Vector (Sorted Insertion)"
            executionTimes = ExecuteVectorInsert(data, repeats)


        elif(algo == 0):
            Execute(1, dist, iN, N, repeats)
            Execute(2, dist, iN, N, repeats)
            Execute(3, dist, iN, N, repeats)
            Execute(4, dist, iN, N, repeats)
            Execute(5, dist, iN, N, repeats)
            Execute(6, dist, iN, N, repeats)

        for i in executionTimes:
            dataItem = [algoName, dist, n, i]
            dataItems.append(dataItem)

        #   Increase the size of n by 5
        n += 5

        #   Fetch the data using new N value before looping again
        data = GetData(fileName, n )
    

        #   Write to CSV file
        with open( algoName + 'Test.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(dataItems)
        csvFile.close()

        #   Header for continuity
        print(algoName + " runtime, on " 
            + dist 
            + " List of numbers, increasing by 5 each run starting at "
            + str(iN) + " and ending at " 
            + str(N) + " : ")
        #print(*dataItems, sep='\n')





#   This calls quicksort on the data R number of times
def ExecuteQuickSort(data, R):
    ret = []

    for _ in itertools.repeat(None, R):
        #   Randomize the data
        random.shuffle(data)

        #   Get current time of the performance counter
        t1 = perf_counter()

        #   Invoke quicksort
        quicksort.QuickSort(data, 0, len(data) - 1)

        #   Get current time of the performance counter (again)
        t2 = perf_counter()

        #   Subtract the two times we just recorded
        elapsed = (t2-t1)

        #   Add milliseconds value to return list 
        ret.append(elapsed*1000)
    return ret





#   This calls insertion sort on the data R number of times
def ExecuteInsertionSort(data, R):
    ret = []

    for _ in itertools.repeat(None, R):
        #   Randomize the data
        random.shuffle(data)

        #   Get current time of the performance counter
        t1 = perf_counter()

        #   Invoke quicksort
        insertionsort.InsertionSort(data)

        #   Get current time of the performance counter (again)
        t2 = perf_counter()

        #   Subtract the two times we just recorded
        elapsed = (t2-t1)

        #   Add milliseconds value to return list 
        ret.append(elapsed*1000)
    return ret





#   This is a quicksort/insertionsort hybrid R number of times
def ExecuteHybridSort(data, R):
    ret = []

    for _ in itertools.repeat(None, R):
        #   Randomize the data
        random.shuffle(data)

        #   Get current time of the performance counter
        t1 = perf_counter()

        #   Invoke quicksort
        hybridsort.HybridSort(data, 0, len(data) - 1)

        #   Get current time of the performance counter (again)
        t2 = perf_counter()

        #   Subtract the two times we just recorded
        elapsed = (t2-t1)

        #   Add milliseconds value to return list 
        ret.append(elapsed*1000)
    return ret





#   This inserts each item in data into hash table, R number of times
#   We just use the python dictionary, and the hash() built-in for this
def ExecuteHashTableInsert(data, R):
    ret = []

    for _ in itertools.repeat(None, R):
        #   Randomize the data
        random.shuffle(data)

        hashTable = dict()

        #   Get current time of the performance counter
        t1 = perf_counter()

        #   Invoke insertion into hashmap
        for item in data:
            hashTable.update({ hash(item): item})
            
        #   Get current time of the performance counter (again)
        t2 = perf_counter()

        #   Subtract the two times we just recorded
        elapsed = (t2-t1)

        #   Add milliseconds value to return list 
        ret.append(elapsed*1000)
    return ret





#   This inserts each item in data into BST, R number of times
#   We use a simple node class and binary insertion can be simulated
def ExecuteBSTInsert(data, R):
    ret = []

    for _ in itertools.repeat(None, R):
        #   Randomize the data
        random.shuffle(data)

        root = node.Node(data[0])
        
        #   Get current time of the performance counter
        t1 = perf_counter()

        #   Invoke insertion into BST
        for item in data:
            node.insert(root, node.Node(item))

        #   Get current time of the performance counter (again)
        t2 = perf_counter()

        #   Subtract the two times we just recorded
        elapsed = (t2-t1)

        #   Add milliseconds value to return list 
        ret.append(elapsed*1000)
    return ret





#   This inserts each item in data (maintaining) order into list, R number of times
#   We use a the python module bisect.insort_left() for sorted insertion
def ExecuteVectorInsert(data, R):
    ret = []

    for _ in itertools.repeat(None, R):
        #   Randomize the data
        random.shuffle(data)

        L = []
        
        #   Get current time of the performance counter
        t1 = perf_counter()

        #   Invoke insertion into BST
        for item in data:
            bisect.insort_left(L, item)

        #   Get current time of the performance counter (again)
        t2 = perf_counter()

        #   Subtract the two times we just recorded
        elapsed = (t2-t1)

        #   Add milliseconds value to return list 
        ret.append(elapsed*1000)
    return ret








def Main():


    #   Algorithm selection options
    print()
    print("Options for Algorithm to time:")
    print("1: Insertion Sort")
    print("2: QuickSort")
    print("3: Hybrid Sort")
    print("4: Insertion into Hash Table")
    print("5: Insertion into BST")
    print("6: Insertion into C++like Vector")
    print("0: Everything")
    print()

    #   Get the selection from user
    target = int( input("Select the algorithm/data structure you would like to profile: ") )
    print()

    #   Get the input file size to start at
    iN = int( input("Select input file (start) size: ") )
    print()


    #   Get the input file size to end at
    N = int( input("Select input file (end) size: ") )
    print()

    #   Get the distribution of data
    sel = input("Use an almost sorted list? (random otherwise) Y/N: ")
    print()

    #   Get the number of times to repeat execution
    repeats = int( input("Repeat the operation how many times?: ") )

    #   Call the profiler
    Execute(target, sel, iN, N, repeats)


if __name__ == "__main__":
    Main()
