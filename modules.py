import game_matrix
import word_finder


def bot_formatted_leaderboard(string_matrix: str = 'disndlfhayeiowsxcnvbxjrds') -> str:
    letter_matrix = game_matrix.string_to_matrix(string_matrix)
    scored_words = word_finder.find_words_form_string_matrix(string_matrix)

    template=f""
    rows, cols = letter_matrix.shape
    for i in range(cols):
        template += f"""{letter_matrix[i, 0]:3}{letter_matrix[i, 1]:3}{letter_matrix[i, 2]:3}{letter_matrix[i, 3]:3}{letter_matrix[i, 4]:3} {scored_words[i][0]} {scored_words[i][1]}\n"""    
    return template
