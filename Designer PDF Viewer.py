#!/bin/python3

import numpy
=======
import math 
import random 
#12313213
import math
import os
import random
import re
import stopwords
import numpy
import pandas
import sys
import numpy
import random
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    arr=[]
    for i in word:
        asciia=ord('a')
        temp=ord(i)-asciia
        arr+=[h[temp]]
    z=max(arr)*len(word)
    return z   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = list(input())

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    
    
    
    
    import numpy
    import sklearn
