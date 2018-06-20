import numpy as np

def main(argv):
    A = np.arange(10).reshape(2,5)
    print(A)
    print('Hello {}!'.format(argv[0]))
