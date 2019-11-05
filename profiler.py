##  For profiling any of the algorithms

import os
import io
import random

import itertools

from time import process_time, perf_counter

from algorithms import insertionsort
from algorithms import quicksort

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

#####################################################
#   Name: Execute
#   Receives: name of algorithm, type of input,
#             size of input, and number of repeats
#   Returns: a list of elapsed execution times
def Execute(algo, dist, N, repeats):

    #   The data we are about to manipulate
    data = []

    #   The list of runtimes we are going to write to file
    executionTimes = []

    #   Check whether to return an almost sorted or random list
    if(dist == "as"):
        data = GetData("as20k.in", N)
        dist = "Almost Sorted"
    else:
        data = GetData("r20k.in", N)
        dist = "Random"

    #   We have insertion sort
    if(algo == 1):
        algoName = "Insertion Sort"
        executionTimes = ExecuteInsertionSort(data, repeats)
        
    #   We have quick sort
    elif(algo == 2):
        algoName = "QuickSort"
        executionTimes = ExecuteQuickSort(data, repeats)
    
    dataItems = []
    for i in executionTimes:
        dataItem = (algoName, dist, N, i)
        dataItems.append(dataItem)
    
    
    #   Header for continuity
    print(algoName + " run time, on " 
        + dist 
        + " List of size " 
        + str(N) + " : ")
    print(*dataItems, sep='\n')


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

        #   Add it to return list 
        ret.append(elapsed)
    return ret

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

        #   Add it to return list 
        ret.append(elapsed)
    return ret








def Main():
    #   Algorithm selection options
    print()
    print("Options for Algorithm to time:")
    print("1: Insertion Sort")
    print("2: QuickSort")
    print()

    #   Get the selection from user
    algo = int( input("Select the algorithm you would like to profile: ") )
    print()

    #   Get the input file size
    N = int( input("Select input file size: ") )
    print()

    #   Get the distribution of data
    sel = input("Use an almost sorted list? (random otherwise) Y/N: ")
    print()

    #   Get the number of times to repeat execution
    repeats = int( input("Repeat the sorting how many times?: ") )

    #   Call the profiler
    Execute(algo, sel, N, repeats)


if __name__ == "__main__":
    Main()










    #   File selection options
    # print()
    # print("Options for input file:")
    # print("A: Random, N = 20k")
    # print("B: Random, N = 40k")
    # print("C: Random, N = 60k")
    # print("D: Random, N = 80k")
    # print("E: Random, N = 100k")
    # print("F: Almost Sorted, N = 20k")
    # print("G: Almost Sorted, N = 40k")
    # print("H: Almost Sorted, N = 60k")
    # print("I: Almost Sorted, N = 80k")
    # print("J: Almost Sorted, N = 100k")
    # print()


    #   Dictionary of every input file to match selection (if needed)
    # files = {"A": "r20k.in",
    #         "B": "r40k.in",
    #         "C": "r60k.in",
    #         "D": "r80k.in",
    #         "E": "r100k.in",
    #         "F": "as20k.in",
    #         "G": "as40k.in",
    #         "H": "as60k.in",
    #         "I": "as80k.in",
    #         "J": "as100k.in"}


