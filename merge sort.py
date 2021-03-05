{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
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
      "Given array is\n",
      "5 4 3 2 1 \n",
      "Sorted array is: \n",
      "1 2 3 4 5 \n"
     ]
    }
   ],
   "source": [
    "def mergeSort(arr): \n",
    "    if len(arr) >1: \n",
    "        mid = len(arr)//2 #Finding the mid of the array \n",
    "        L = arr[:mid] # Dividing the array elements  \n",
    "        R = arr[mid:] # into 2 halves \n",
    "  \n",
    "        mergeSort(L) # Sorting the first half \n",
    "        mergeSort(R) # Sorting the second half \n",
    "  \n",
    "        i = j = k = 0\n",
    "          \n",
    "        # Copy data to temp arrays L[] and R[] \n",
    "        while i < len(L) and j < len(R): \n",
    "            if L[i] < R[j]: \n",
    "                arr[k] = L[i] \n",
    "                i+=1\n",
    "            else: \n",
    "                arr[k] = R[j] \n",
    "                j+=1\n",
    "            k+=1\n",
    "          \n",
    "        # Checking if any element was left \n",
    "        while i < len(L): \n",
    "            arr[k] = L[i] \n",
    "            i+=1\n",
    "            k+=1\n",
    "          \n",
    "        while j < len(R): \n",
    "            arr[k] = R[j] \n",
    "            j+=1\n",
    "            k+=1\n",
    "  \n",
    "# Code to print the list \n",
    "def printList(arr): \n",
    "    for i in range(len(arr)):         \n",
    "        print(arr[i],end=\" \") \n",
    "    print() \n",
    "  \n",
    "# driver code to test the above code \n",
    "if __name__ == '__main__': \n",
    "    A = []\n",
    "    n=int(input(\"Enter how  many number in the list:\"))\n",
    "    for  i in range(n):\n",
    "        A.append(int(input())) \n",
    "        \n",
    "    print (\"Given array is\", end=\"\\n\")  \n",
    "    printList(A) \n",
    "    mergeSort(A) \n",
    "    print(\"Sorted array is: \", end=\"\\n\") \n",
    "    printList(A) \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n"
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
