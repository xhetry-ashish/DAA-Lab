{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter how  many number in the list:5\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "Sorted array is\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "# To heapify subtree rooted at index i. \n",
    "# n is size of heap \n",
    "def heapify(arr, n, i): \n",
    "    largest = i # Initialize largest as root \n",
    "    l = 2 * i + 1     # left = 2*i + 1 \n",
    "    r = 2 * i + 2     # right = 2*i + 2 \n",
    "  \n",
    "    # See if left child of root exists and is \n",
    "    # greater than root \n",
    "    if l < n and arr[i] < arr[l]: \n",
    "        largest = l \n",
    "  \n",
    "    # See if right child of root exists and is \n",
    "    # greater than root \n",
    "    if r < n and arr[largest] < arr[r]: \n",
    "        largest = r \n",
    "  \n",
    "    # Change root, if needed \n",
    "    if largest != i: \n",
    "        arr[i],arr[largest] = arr[largest],arr[i] # swap \n",
    "  \n",
    "        # Heapify the root. \n",
    "        heapify(arr, n, largest) \n",
    "  \n",
    "# The main function to sort an array of given size \n",
    "def heapSort(arr): \n",
    "    n = len(arr) \n",
    "  \n",
    "    # Build a maxheap. \n",
    "    for i in range(n, -1, -1): \n",
    "        heapify(arr, n, i) \n",
    "  \n",
    "    # One by one extract elements \n",
    "    for i in range(n-1, 0, -1): \n",
    "        arr[i], arr[0] = arr[0], arr[i] # swap \n",
    "        heapify(arr, i, 0) \n",
    "  \n",
    "# Driver code to test above \n",
    "A = []\n",
    "n=int(input(\"Enter how  many number in the list:\"))\n",
    "for  i in range(n):\n",
    "    A.append(int(input())) \n",
    "    \n",
    "heapSort(A) \n",
    "print (\"Sorted array is\") \n",
    "for i in range(n): \n",
    "    print (\"%d\" %A[i]), \n"
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
