import numpy as np
import math

def string_to_matrix(matrix_string: str) -> np.ndarray:
    matrix_string = list(matrix_string.upper())
    n = math.sqrt(len(matrix_string))
    
    if n ** 2 == len(matrix_string):
        letter_matrix = np.array(matrix_string).reshape(int(n), int(n))
    else:
        raise ValueError('Matrix string is not valid')
    
    return letter_matrix


def matrix_from_screenshot() -> np.ndarray:
    '''Future feature'''
    pass
