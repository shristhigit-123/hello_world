#!/bin/python3
#comment
import numpy
=======
import math 
import random

import math
import os
import random
import re
import sys
for i in range (1,5):
    print (i)
   
# Complete the angryProfessor function below.
def angryProfessor(k, a):
    temp=0
    for i in a:
        if i<=0:
            temp+=1
    if temp>=k:
        return "NO"
    return "YES"            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
