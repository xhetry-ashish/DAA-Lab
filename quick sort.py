{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This function takes last element as pivot, places \n",
    "# the pivot element at its correct position in sorted \n",
    "# array, and places all smaller (smaller than pivot) \n",
    "# to left of pivot and all greater elements to right \n",
    "# of pivot \n",
    "def partition(arr,low,high): \n",
    "    i = ( low-1 )         # index of smaller element \n",
    "    pivot = arr[high]     # pivot \n",
    "  \n",
    "    for j in range(low , high): \n",
    "  \n",
    "        # If current element is smaller than the pivot \n",
    "        if   arr[j] < pivot: \n",
    "          \n",
    "            # increment index of smaller element \n",
    "            i = i+1 \n",
    "            arr[i],arr[j] = arr[j],arr[i] \n",
    "  \n",
    "    arr[i+1],arr[high] = arr[high],arr[i+1] \n",
    "    return ( i+1 ) \n",
    "  \n",
    "# The main function that implements QuickSort \n",
    "# arr[] --> Array to be sorted, \n",
    "# low  --> Starting index, \n",
    "# high  --> Ending index \n",
    "  \n",
    "# Function to do Quick sort \n",
    "def quickSort(arr,low,high): \n",
    "    if low < high: \n",
    "  \n",
    "        # pi is partitioning index, arr[p] is now \n",
    "        # at right place \n",
    "        pi = partition(arr,low,high) \n",
    "  \n",
    "        # Separately sort elements before \n",
    "        # partition and after partition \n",
    "        quickSort(arr, low, pi-1) \n",
    "        quickSort(arr, pi+1, high) \n",
    "  \n",
    "# Driver code to test above \n",
    "A = []\n",
    "n=int(input(\"Enter how  many number in the list:\"))\n",
    "for  i in range(n):\n",
    "    A.append(int(input())) \n",
    "    \n",
    "quickSort(A,0,n-1) \n",
    "print (\"Sorted array is:\") \n",
    "for i in range(n): \n",
    "    print (\"%d\" %A[i]), "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
