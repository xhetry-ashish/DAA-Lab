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
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "Sorted list is: [3, 4, 5, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "def bubbleSort(nlist):\n",
    "    for passnum in range(len(nlist)-1,0,-1):\n",
    "        for i in range(passnum):\n",
    "            if nlist[i]>nlist[i+1]:\n",
    "                temp = nlist[i]\n",
    "                nlist[i] = nlist[i+1]\n",
    "                nlist[i+1] = temp\n",
    "\n",
    "nlist = []\n",
    "a=int(input(\"Enter how  many number  to be sorted:\"))\n",
    "for  i in range(a):\n",
    "    nlist.append(int(input()))\n",
    "bubbleSort(nlist)\n",
    "print(\"Sorted list is:\",nlist)"
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
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "8\n",
      "6\n",
      "4\n",
      "2\n"
     ]
    }
   ],
   "source": []
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
