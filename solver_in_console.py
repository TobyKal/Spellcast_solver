import modules as mod
import game_matrix

def main() -> None:
    string_matrix = 'hdcbasuedfodsckfurdskcbsq'
    letter_matrix = game_matrix.get_matrix(string_matrix)
   
    special_cords = {'double': None, 'triple': None, 'multiplayer': None}
    list_of_valid_words = mod.open_and_format_the_word_list('wordlist.txt')
    #mod.fill_coordinates_dict(special_cords)
    
    
    #valid_coordinate_list = find_valid_word_coordinates()
    found_scored_words = mod.find_socred_valid_word_list(letter_matrix, list_of_valid_words, special_cords)

    
    print(letter_matrix)
    for word in found_scored_words:
        if len(word[1]) >= 6 or word[0] > 30:
            print(f'Points {word[0]}  {word[1]}')

    
if __name__ == "__main__":
    print(mod.formated_words_form_sting_response())