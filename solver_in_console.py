import modules as mod


def main() -> str:
    string_matrix = 'hdcbasuedfodsckfurdskcbsq'
    special_cords = {'double': (4,4), 'triple': (4,4), 'multiplier': (4,4)}
    
    print(mod.formatted_words_from_string_response(string_matrix, special_cords))

    
if __name__ == "__main__":
    main()
