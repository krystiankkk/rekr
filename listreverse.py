#!/bin/python3

import math
import os
import random
import re
import sys



def rev(arr):
    ret=''
    new = arr[::-1]
    for i in new:
        ret = ret+str(i)+' '
    return ret

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(rev(arr))