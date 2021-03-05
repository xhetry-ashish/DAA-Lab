{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of elements you want to enter: 5\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "The list is: [1, 2, 3, 4, 5]\n",
      "Enter a number  to be searched: 3\n",
      "Found and its position is: 3\n"
     ]
    }
   ],
   "source": [
    "def Sequential_Search(lst,b):\n",
    "\n",
    "    pos = 0\n",
    "    found = False\n",
    "    for pos in range(n):\n",
    "        if lst[pos] == b:\n",
    "            found = True\n",
    "            break\n",
    "        else:\n",
    "            pos = pos + 1\n",
    "    return found,pos\n",
    "\n",
    "\n",
    "lst = [] \n",
    "# number of elemetns as input \n",
    "n = int(input(\"Enter number of elements you want to enter: \")) \n",
    "  \n",
    "# iterating till the range \n",
    "for i in range(n): \n",
    "    ele = int(input()) \n",
    "    lst.append(ele) # adding the element \n",
    "      \n",
    "print(\"The list is:\",lst) \n",
    "b=int(input(\"Enter a number  to be searched: \"))\n",
    "c,d = Sequential_Search(lst,b)\n",
    "if c==True:\n",
    "    print(\"Found and its position is:\",d+1)\n",
    "else:\n",
    "    print(\"Not Found\")"
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
