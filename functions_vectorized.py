import time
import random
import matplotlib.pyplot as plt
import numpy as np


def prod_non_zero_diag_vectorized(x):
    
    answer = np.prod(np.diagonal(x)[np.diagonal(x) > 0])
    
    return answer

    pass

def are_multisets_equal(x, y):
    
    np.sort(x)
    np.sort(y)
    
    return x.all() == y.all()

    pass


def max_after_zero(x):
    
    return np.max(x[1:][np.nonzero(x[:-1] == 0)]) 

    pass


def convert_image(img, coefs):
    
    return np.dot(img, coefs)

    pass


def run_length_encoding(x):
    
    diff_x = np.diff(x)

    ind = [-1]
    ind = np.append(ind, np.nonzero(diff_x))
    ind += 1
    
    values = x[ind]
    ind = np.append(ind, len(x))
    cnt_values = np.diff(ind)
    return [values, cnt_values]

    pass


def pairwise_distance(x, y):
    len_x = len(x)
    len_y = len(y)
    x = np.repeat(x, len_y, axis = 0)
    x.reshape((len_x * 2, len_y))
    y = np.tile(y, (len_x, 1))
    y.reshape((len_x * 2, len_y))
    x -= y
    x = x ** 2
    return np.vectorize(np.sqrt)(np.dot(x, np.array([1, 1])))

    pass
