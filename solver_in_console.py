import modules as m
import word_finder

def main() -> str:
    string_matrix = 'hdcbasuedfodsckfurdskcbsq'
    
    print(m.bot_formatted_leaderboard(string_matrix))
    print("\n")
    print(word_finder.find_words_form_string_matrix(string_matrix))

if __name__ == "__main__":
    main()
