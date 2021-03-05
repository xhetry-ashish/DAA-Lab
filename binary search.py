{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter how  many number in the list:5\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "\n",
      " Enter a number to search: 6\n",
      "[1, 2, 3, 4, 5]\n",
      "Element is not present in array\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Returns index of x in arr if present, else -1 \n",
    "def binarySearch (arr, l, r, x): \n",
    "  \n",
    "    # Check base case \n",
    "    if r >= l: \n",
    "  \n",
    "        mid = int(l + (r - l)/2)\n",
    "  \n",
    "        # If element is present at the middle itself \n",
    "        if arr[mid] == x: \n",
    "            return mid \n",
    "          \n",
    "        # If element is smaller than mid, then it can only \n",
    "        # be present in left subarray \n",
    "        elif arr[mid] > x: \n",
    "            return binarySearch(arr, l, mid-1, x) \n",
    "  \n",
    "        # Else the element can only be present in right subarray \n",
    "        else: \n",
    "            return binarySearch(arr, mid+1, r, x) \n",
    "  \n",
    "    else: \n",
    "        # Element is not present in the array \n",
    "        return -1\n",
    "\n",
    "A = []\n",
    "n=int(input(\"Enter how  many number in the list:\"))\n",
    "for  i in range(n):\n",
    "    A.append(int(input()))\n",
    "    \n",
    "x=int(input('\\n Enter a number to search: '))\n",
    "\n",
    "# Function call \n",
    "result = binarySearch(A, 0, len(A)-1, x) \n",
    "print(A)\n",
    "if result != -1: \n",
    "    print('Element is present at index ', result+1) \n",
    "else: \n",
    "    print (\"Element is not present in array\")"
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
