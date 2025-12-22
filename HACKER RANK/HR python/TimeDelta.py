#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    delta = abs((dt1 - dt2).total_seconds())
    return str(int(delta))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        t1 = input().strip()
        t2 = input().strip()
        print(time_delta(t1, t2))