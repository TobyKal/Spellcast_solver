import numpy as np
import math







def sting_to_matrix(matrix_stirng: str) -> np.ndarray:
    matrix_stirng = matrix_stirng.upper()
    matrix_stirng = list(matrix_stirng)
    n = math.sqrt(len(matrix_stirng))
    
    # checking if it can be a square matrix
    if n ** 2 == len(matrix_stirng):
        letter_matrix = np.array(matrix_stirng).reshape(int(n), int(n))
    else:
        raise ValueError('Matrix sting is not valid')
    
    return letter_matrix


def matirx_form_screenshot() -> np.ndarray:
    matrix = None

    return matrix












def get_matrix(stirng= False) -> np.ndarray:
    if stirng != False:
        try:
            matrix = sting_to_matrix(stirng)
        except:
            print("You gave a wrong matrix_string you dumb ass!!! Try again. \n\n\n")
            get_matrix
        
        return matrix
    
    return matirx_form_screenshot()
