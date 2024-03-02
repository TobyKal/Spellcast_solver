import numpy as np
import math

def string_to_matrix(matrix_string: str) -> np.ndarray:
    matrix_string = matrix_string.upper()
    matrix_string = list(matrix_string)
    n = math.sqrt(len(matrix_string))
    
    # checking if it can be a square matrix
    if n ** 2 == len(matrix_string):
        letter_matrix = np.array(matrix_string).reshape(int(n), int(n))
    else:
        raise ValueError('Matrix string is not valid')
    
    return letter_matrix


def matrix_from_screenshot() -> np.ndarray:
    '''Future feature'''
    pass


def get_matrix(string= False) -> np.ndarray:
    if string != False:
        try:
            matrix = string_to_matrix(string)
        except:
            print("You gave a wrong matrix_string. Try again. \n\n")
            get_matrix
        
        return matrix
    
    return matrix_from_screenshot()