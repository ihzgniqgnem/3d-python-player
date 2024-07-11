from functools import lru_cache
import math
from math import *
import numpy as np


@lru_cache(maxsize=1024)
def round(x):
    return int(x + 0.5) if x >= 0 else int(x - 0.5)

@lru_cache(maxsize=1024)
def sin(x):
    return np.sin(x)
@lru_cache(maxsize=1024)
def cos(x):
    return np.cos(x)
class list(np.ndarray):
    pass
#@lru_cache(maxsize=1024)
def matrix_multiply(A, B):
    # if isinstance(A, list):
    #     A=np.array(A)
    # if isinstance(B, list):
    #     B=np.array(B)
    C=np.dot(A,B)
    #C=tuple([tuple(i) for i in C])
    return C