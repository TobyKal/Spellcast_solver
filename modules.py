import game_matrix
import numpy as np




def find_valid_word_coordinates(list_of_words: list[str], matrix: np.ndarray) -> list:
    '''
        This function is looking for valid words that can be in the matrix.
        It iterates over the entire matrix and calls a recursive function that
        finds every possible string_path that could potentially create a word.
        If such a word is found, its coordinates string_path is being appended to the
        valid_coordinates_list and returns it.

        Parameters: 
            list_of_words -> list of words to find ||
            matrix -> np.array - np.array with letters representing the gameboard

    '''
    def find_valid_and_possible_words(string_path: list[tuple[int,int]],
                                      list_of_possible_words: list[str],
                                      matrix: np.ndarray) -> list[str]:
        '''
        This function is looking for valid and possible words for a given string on a list of words.
        Function returns a smaller list of words that could be found in next iterations.
        
        Parameters: 
            string_path -> list[tuple[int,int]] - list of tuples representing matrix coordinates||
            list_of_possible_words -> list of words that could be found||
            matrix -> np.array - np.array with letters representing the gameboard
        '''
       
        string = coordinates_to_string(string_path, matrix)
       
        small_possible_list = [] 
        for word in list_of_possible_words:
            if word.startswith(string):
                small_possible_list.append(word)
        for word in small_possible_list:
            if word == string and word not in valid_coordinates_list:
                # Append the coordinate as a tuple, not a list
                valid_coordinates_list.append(list(string_path))
        
        return small_possible_list    
    def find_combinations(matrix: np.ndarray, string_path: list[tuple[int,int]], list_of_possible_words: list[str]) -> None:
        '''

        This function is a recursive function that calls itself on every possible string_path
        made by moving to the next cell in a matrix that was not stepped on and finds a
        valid word from the list

        Parameters: 
            matrix -> np.array - np.array with letters representing the gameboard ||
            string_path -> list[tuple[int,int]] - list of tuples representing the word in form of matrix coordinates||
            list_of_possible_words -> list of words that could be found

        '''

        # Assign the return value to the list_of_possible_words variable
        list_of_possible_words = find_valid_and_possible_words(string_path, list_of_possible_words, matrix)
        
        if len(list_of_possible_words) == 0:
            return None

        rows, cols = string_path[-1]
        # Directions:    up,     down,    left,     right,  up-left,  up-right,   down-left,  down-right
        directions = [(-1, 0),  (1, 0),  (0, -1),  (0, 1),  (-1,-1),   (-1,1),    (1,-1),     (1,1)]

        for direction in directions:
            n_rows, n_cols = rows + direction[0], cols + direction[1]

            # Check if the new position is valid
            if n_rows >= 0 and n_rows < len(matrix) and n_cols >= 0 and n_cols < len(matrix[0]) and (n_rows, n_cols) not in string_path:
                # Add the new position to the string_path
                string_path.append((n_rows, n_cols))
                # Recursive call
                find_combinations(matrix, string_path, list_of_possible_words)
                #pops the last coords to check next direction
                string_path.pop()

        return None
    
    global valid_coordinates_list
    valid_coordinates_list = []

    rows, cols = matrix.shape
    for row in np.arange(rows):
        for col in np.arange(cols):
            find_combinations(matrix, [(row,col)], list_of_words)

    return valid_coordinates_list


def open_and_format_the_word_list(word_list_name: str) -> list[str]:
    with open(f'{word_list_name}', 'r') as file:
        wordlist = file.readlines()
    
    for i, word in enumerate(wordlist):
    # Assign the modified word to the same position in the wordlist
        wordlist[i] = word.rstrip('\n')

    return wordlist


def coordinates_to_string(coordinates: list[tuple[int,int]], matrix: np.ndarray) -> str:
        '''
        Converst a list of coordinates into a sing using a given matrix.

        Parameters: 
            coordinates -> list[tuple[int,int]] - list of tuples representing matrix coordinates||
            matirx -> np.array - np.array wiht letter representing the gameboard
        '''     
        return ''.join(matrix[cord[0],cord[1]] for cord in coordinates)

def create_socring_leaderboard(list_of_words_to_score: list[str],
                               matrix: np.ndarray,
                               special_cords: dict[str, int] = [None, None, None]) -> list[(int, str)]:
    '''
    This funcion creates a sorted list of words with coresponding points in a tuople
    '''
   
    letter_scores = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1,
    'N': 2, 'R': 2, 'S': 2, 'T': 2,
    'D': 3, 'G': 3, 'L': 3,
    'B': 4, 'H': 4, 'P': 4, 'M': 4, 'U': 4, 'Y': 4,
    'C': 5, 'F': 5, 'V': 5, 'W': 5,
    'K': 6,
    'J': 7, 'X': 7,
    'Q': 8, 'Z': 8
}
    scores = []
    
    for word in list_of_words_to_score:
        word_score = 0
        word_multiplayer_found = False
        counter = 0

        for letter_cords in word:
            letter = matrix[letter_cords[0], letter_cords[1]]
            counter += 1
            
            # Adding points and modifires to coresponding letters
            if letter_cords == special_cords['double'] and letter_cords == special_cords['multiplayer']:
                word_score += letter_scores[f'{letter}'] * 2
                word_multiplayer_found = True

            elif letter_cords == special_cords['double']:
                word_score += letter_scores[f'{letter}'] * 2

            elif letter_cords == special_cords['triple'] and letter_cords == special_cords['multiplayer']:
                word_score += letter_scores[f'{letter}'] * 3
                word_multiplayer_found = True

            elif letter_cords == special_cords['triple']:
                word_score += letter_scores[f'{letter}'] * 3
            
            elif letter_cords == special_cords['multiplayer']  :
                word_multiplayer_found = True
                word_score += letter_scores[f'{letter}']
            else:
                word_score += letter_scores[f'{letter}']
        
        if word_multiplayer_found:
            word_score *= 2
        if counter >= 6:
            word_score += 10
        
        scores.append((word_score, coordinates_to_string(word, matrix)))

    scores.sort(reverse=True)
    return scores 

def str_to_cords_tuple(str: str) -> tuple:
    if len(str) != 2:
        return None
    else:
        return (int(str[0]), int(str[1]))

def fill_coordinates_dict(dictionary: dict) -> None:
    '''
    This funcion iterates over an object in and allows to fill in the coordinates to the dict
    '''

    def fill_in_the_object_in_dict(object_in_dic:str, dictionary: dict) -> tuple:
        cords = list(input(f'provide cords for {obj} (indexing starts at 1, only two ints no spaces, if None type "n"!!)'))
        if cords[0] == 'n':
            return None
        elif len(cords) != 2:
            return fill_in_the_object_in_dict(object_in_dic, dictionary)
        try:
            cords = tuple([int(x) for x in cords])
        except:
            return fill_in_the_object_in_dict(object_in_dic, dictionary)
        return (cords[0] - 1, cords[1] - 1)
    
    for obj in dictionary:
        dictionary[f'{obj}'] = fill_in_the_object_in_dict(obj, dictionary)




def find_socred_valid_word_list(letter_matrix: str,
                                list_of_valid_words: list[str],
                                special_cords: list[list[ (int,int) ]])-> list[(int, str)] :
    
    return create_socring_leaderboard(find_valid_word_coordinates(list_of_valid_words, letter_matrix), letter_matrix, special_cords)




def formated_words_form_sting_response(sting_matrix: str = 'disndlfhayeiowsxcnvbxjrds',special_cords = {'double': None, 'tripple': None, 'multiplayer': None}, word_list_name: str = "wordlist.txt") -> str:
    letter_matrix = game_matrix.get_matrix(sting_matrix)
    found_scored_words = find_socred_valid_word_list(letter_matrix, open_and_format_the_word_list(f'{word_list_name}'), special_cords)
    template=f""
    for i in range(5):
        template += f"""{letter_matrix[i, 0]:3}{letter_matrix[i, 1]:3}{letter_matrix[i, 2]:3}{letter_matrix[i, 3]:3}{letter_matrix[i, 4]:3} {found_scored_words[i][0]} {found_scored_words[i][1]}\n"""    
    return template

