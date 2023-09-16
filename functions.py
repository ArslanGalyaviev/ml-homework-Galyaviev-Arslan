import time
import random
import matplotlib.pyplot as plt
import numpy as np

def prod_non_zero_diag(x):
    
    answer = 1
    
    for i in range(len(x)):
        if (i < len(x[i]) and x[i][i] > 0):
            answer = answer * x[i][i]
            
    return answer

    pass


def are_multisets_equal(x, y):
    
    x.sort()
    y.sort()
    
    is_equal = False
   
    if x.all() == y.all():
        is_equal = True
            
    return is_equal

    pass


def max_after_zero(x):
    
    answer = -1
    
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            answer = max(answer, x[i])
        
    return answer

    pass


def convert_image(img, coefs):
    
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j] = float(img[i][j][0]) * coefs[0] + float(img[i][j][1]) * coefs[1] + float(img[i][j][2]) * coefs[2]
            
    return img

    pass


def run_length_encoding(x):
    
    cur_el = -1
    cur_cnt = 0
    el = []
    el_cnt = []
    for i in range (0, len(x)):
        if x[i] != cur_el:
            if cur_cnt > 0:
                el.append(cur_el)
                el_cnt.append(cur_cnt)
            cur_cnt = 0
        if x[i] == cur_el:
            cur_cnt += 1
            
    if cur_cnt > 0:
        el.append(cur_el)
        el_cnt.append(cur_cnt)
    
    return [el, el_cnt]

    pass


def pairwise_distance(x, y):
    
    res = [[0] * len(y) for i in range(len(x))]
    
    for i in range(len(x)):
        for j in range(len(y)):
            dx = x[i][0] - y[i][0]
            dy = x[i][1] - y[i][1]
            dist = (dx * dx + dy * dy) ** 0.5
            res[i][j] = dist
            
    return res

    pass
