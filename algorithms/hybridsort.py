import sys
from algorithms import insertionsort
from algorithms import quicksort
sys.setrecursionlimit(5000)
## Adapted from:
## https://www.geeksforgeeks.org/python-program-for-quicksort/
## Python program for implementation of HybridSort 




def HybridSort(data, hi, lo):
    if(lo >= hi):
        return
    elif((hi - lo ) < 36):
        insertionsort.InsertionSort(data) 
        return
    else:
        quicksort.QuickSort(data, hi, lo)