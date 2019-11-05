##  For profiling any of the algorithms

import io, timeit
from pstats import SortKey
import random

from time import process_time, perf_counter, perf_counter_ns


from algorithms import insertionsort
from algorithms import quicksort

def Execute(algo, fName, repeats):

    #   Populate the array
    fName = 'input/' + fName
    f = open(fName, 'r+')
    data = f.read()
    f.close()

    data = [int(i) for i in data.strip().split()]

    executionTimes = []

    #print(data)

    algo = int(algo)
    repeats = int(repeats)
    if(algo == 1):
        #print(timeit(stmt = data.algorithms.InsertionSort(), repeat=repeats) )
        pass
    elif(algo == 2):
        while (repeats > 0):
            random.shuffle(data)
            print("first few items in data (randomness check): ", data[0:3])
            print("Quick sort times, on " + fName + " : ")
            t1 = perf_counter()
            quicksort.QuickSort(data, 0, len(data) - 1)
            t2 = perf_counter()
            elapsed = (t2-t1)
            print("Elapsed: ", elapsed, " Seconds." )
            executionTimes.append(elapsed)
            repeats = repeats - 1
    
    


def Main():
    #   Algorithm selection options
    print()
    print("Options for Algorithm to time:")
    print("1: Insertion Sort")
    print("2: QuickSort")
    print()

    #   Get the selection from user
    algo = input("Select the algorithm you would like to profile: ")
    print()


    #   File selection options
    print()
    print("Options for input file:")
    print("A: Random, N = 20k")
    print("B: Random, N = 40k")
    print("C: Random, N = 60k")
    print("D: Random, N = 80k")
    print("E: Random, N = 100k")
    print("F: Almost Sorted, N = 20k")
    print("G: Almost Sorted, N = 40k")
    print("H: Almost Sorted, N = 60k")
    print("I: Almost Sorted, N = 80k")
    print("J: Almost Sorted, N = 100k")
    print()

    #   Get the selection from user
    sel = input("Select the input file you would like to use: ")
    print()

    #   Dictionary of every input file to match selection
    files = {"A": "r20k.in",
            "B": "r40k.in",
            "C": "r60k.in",
            "D": "r80k.in",
            "E": "r100k.in",
            "F": "as20k.in",
            "G": "as40k.in",
            "H": "as60k.in",
            "I": "as80k.in",
            "J": "as100k.in"}


    repeats = input("Repeat how many times?: ")


    #   Call the profiler
    Execute(algo,files[sel], repeats)


if __name__ == "__main__":
    Main()