import numpy as np
import game_matrix

def format_word_list(word_list_name: str) -> list[str]:
    with open(word_list_name, 'r') as file:
        wordlist = [word.strip() for word in file]
    return wordlist


def coordinates_to_string(letter_combination_path: list[tuple[int,int]], matrix: np.ndarray) -> str:
    string = ""
    for cords in letter_combination_path:
        string += matrix[cords]
    return string


def find_valid_and_possible_words(letter_combination_path: list[tuple[int,int]],
                                  possible_words: list[str],
                                  matrix: np.ndarray) -> list[str]:

    letter_combination = coordinates_to_string(letter_combination_path, matrix)
    possible_words = [word for word in possible_words if word.startswith(letter_combination)]

    for word in possible_words:
        if word == letter_combination and word not in valid_coordinates:
            valid_coordinates.append(tuple(letter_combination_path))
    
    return possible_words  


def find_combinations(matrix: np.ndarray, letter_combination_path: list[tuple[int,int]], possible_words: list[str]) -> None:
    # resetting the list for each recursive call
    possible_words = find_valid_and_possible_words(letter_combination_path, possible_words, matrix)
    
    if len(possible_words) == 0:
        return None

    current_row, current_col = letter_combination_path[-1]
    # Directions:    up,     down,    left,     right,  up-left,  up-right,   down-left,  down-right
    directions = [(-1, 0),  (1, 0),  (0, -1),  (0, 1),  (-1,-1),   (-1,1),    (1,-1),     (1,1)]

    for direction in directions:
        next_row, next_col = current_row + direction[0], current_col + direction[1]

        # checking if next coordinates are valid
        if next_row >= 0 and next_row < len(matrix) and next_col >= 0 and next_col < len(matrix[0]) and (next_row, next_col) not in letter_combination_path:
            
            letter_combination_path.append((next_row, next_col))
            find_combinations(matrix, letter_combination_path, possible_words)
            letter_combination_path.pop()

    return None


def find_valid_word_coordinates(list_of_words: list[str], matrix: np.ndarray) -> list[tuple[int, int]]:
    global valid_coordinates
    valid_coordinates = []
    rows, cols = matrix.shape
    
    for row in np.arange(rows):
        for col in np.arange(cols):
            find_combinations(matrix, [(row,col)], list_of_words)

    return valid_coordinates


def score_word(word: list[(int,int)], letter_matrix: np.ndarray) -> tuple[int, str]:
    letter_points = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1,
    'N': 2, 'R': 2, 'S': 2, 'T': 2,
    'D': 3, 'G': 3, 'L': 3,
    'B': 4, 'H': 4, 'P': 4, 'M': 4, 'U': 4, 'Y': 4,
    'C': 5, 'F': 5, 'V': 5, 'W': 5,
    'K': 6,
    'J': 7, 'X': 7,
    'Q': 8, 'Z': 8}
    
    score = 0
    for letter_coordinates in word:
        score += letter_points[letter_matrix[letter_coordinates]]

    

    return (score, coordinates_to_string(word, letter_matrix)) 


def find_words_form_string_matrix(string_matrix: str) -> list[tuple[int,str]]:
    list_of_words = format_word_list("wordlist.txt")
    letter_matrix = game_matrix.string_to_matrix(string_matrix)
    valid_words = find_valid_word_coordinates(list_of_words, letter_matrix)

    # scoring words
    valid_words = [score_word(word, letter_matrix) for word in valid_coordinates]
    valid_words.sort(reverse = True)

    return valid_words

    



