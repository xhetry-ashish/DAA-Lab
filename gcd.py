{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter one number: 234\n",
      "Enter one number: 456\n",
      "GCD is: 6\n"
     ]
    }
   ],
   "source": [
    "def gcd(a, b): \n",
    "    while (a != b): \n",
    "        if (a > b): \n",
    "            a = a - b \n",
    "        else: \n",
    "            b = b - a \n",
    "    return a \n",
    "\n",
    "a=int(input(\"Enter one number: \"))\n",
    "b=int(input(\"Enter one number: \"))\n",
    "print(\"GCD is:\",gcd(a,b))\n"
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
