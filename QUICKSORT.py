# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:27:46 2018

@author: Mithilesh
"""
def quicksort(arr):
    quicksort2(arr,0,len(arr)-1)
    return(arr)

def partition(arr,start,end):           #used for partitioning
    pivot=arr[end]                      #intializing right most value of array as pivot
    index=start                         #intializing index as start value
    for i in range(start,end):          #loop for swaping the values if condition is satisfied
        if arr[i]<=pivot:
            arr[i],arr[index]=arr[index],arr[i]
            index+=1
    arr[end],arr[index]=arr[index],arr[end]      #swaping pivot with the value at index 
    return(index)

def quicksort2(arr,start,end):
    if start<end:
        index=partition(arr,start,end)
        quicksort2(arr,start,index-1)
        quicksort2(arr,index+1,end)
    return(arr)
arr=list(map(int,input("Enter the array please : ").split()))
start,end=0,len(arr)
sorted_array=quicksort(arr)
print(sorted_array)
