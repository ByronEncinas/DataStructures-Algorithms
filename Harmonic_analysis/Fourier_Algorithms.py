## We have to understand the DFT theory, and then the algorithm

import numpy as np
import matplotlib.pyplot as plt

def data_from_file(test_file):

    with open(test_file, 'r', encoding='utf8') as data_file:
        sample = []

        for line in data_file:
            sample.append(float(line.strip()))
    
    return sample


def Dfourier_transform(data_list):
    
    data_size = int(len(data_list))

    freq_domain = []

    for k in range(data_size):
        
        _freq = 0
        
        for n in range(data_size):

                b_k = 2*np.pi*k/data_size
                _freq += data_list[n]*np.exp(-1.j*b_k*n) 
        
        freq_domain.append(np.around(_freq,3))

    return freq_domain

def Ffourier_transform(Amps):
    data_size = int(len(Amps))
    freq_domain = []

    return freq_domain

""" 
real_file = "acceleration_field_koyna.txt"
test_file = "test.txt"
"""

if __name__ == '__main__':

    sample = data_from_file("test.txt")
    
    Frecuency_space = Dfourier_transform(sample)

    for freq in Frecuency_space:
        print(freq.imag)
