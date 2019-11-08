import sys
from algorithms import insertionsort
sys.setrecursionlimit(5000)
## Adapted from:
## https://www.geeksforgeeks.org/python-program-for-quicksort/
## Python program for implementation of HybridSort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def HybridSort(arr,low,high):

    if low >= high:
        return

    #   If our partition <= 50
    elif( high - low < 10):
        #   Switch over to insertion sort
        insertionsort.InsertionSort(arr)


    elif low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        
        pi = partition(arr,low,high) 
        # Separately sort elements before 
        # partition and after partition 
        HybridSort(arr, low, pi-1) 
        HybridSort(arr, pi+1, high) 