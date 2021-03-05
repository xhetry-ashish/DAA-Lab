{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter how  many number  to be sorted:5\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "Sorted array\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "import sys \n",
    "\n",
    "# Traverse through all array elements \n",
    "def selectionsort(A):\n",
    "    for i in range(len(A)): \n",
    "      \n",
    "    # Find the minimum element in remaining  \n",
    "    # unsorted array \n",
    "        min_idx = i \n",
    "        for j in range(i+1, len(A)): \n",
    "            if A[min_idx] > A[j]: \n",
    "                min_idx = j \n",
    "              \n",
    "    # Swap the found minimum element with  \n",
    "    # the first element         \n",
    "        A[i], A[min_idx] = A[min_idx], A[i] \n",
    "  \n",
    "# Driver code to test above \n",
    "A = []\n",
    "n=int(input(\"Enter how  many number  to be sorted:\"))\n",
    "for  i in range(n):\n",
    "    A.append(int(input()))\n",
    "print (\"Sorted array\") \n",
    "selectionsort(A)\n",
    "for i in range(len(A)): \n",
    "    print(\"%d\" %A[i]),  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
