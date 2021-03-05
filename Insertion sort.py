{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
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
    "def insertionSort(A): \n",
    "  \n",
    "    # Traverse through 1 to len(arr) \n",
    "    for i in range(1, len(A)): \n",
    "  \n",
    "        key = A[i] \n",
    "  \n",
    "        # Move elements of A[0..i-1], that are \n",
    "        # greater than key, to one position ahead \n",
    "        # of their current position \n",
    "        j = i-1\n",
    "        while j >=0 and key < A[j] : \n",
    "                A[j+1] = A[j] \n",
    "                j -= 1\n",
    "        A[j+1] = key \n",
    "        \n",
    "        \n",
    "A = []\n",
    "n=int(input(\"Enter how  many number  to be sorted:\"))\n",
    "for  i in range(n):\n",
    "    A.append(int(input()))\n",
    "print (\"Sorted array\") \n",
    "insertionSort(A)\n",
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
