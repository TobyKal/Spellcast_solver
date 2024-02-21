# Importing the modules
import tkinter as tk

# Creating the main window
root = tk.Tk()
root.title("Spell Cast Solver")
root.geometry("600x450")

# Creating the matrix frame
matrix_frame = tk.Frame(root, borderwidth=2, relief="groove")
matrix_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Creating the matrix labels and entries
matrix_labels = []
matrix_entries = []
for i in range(5):
    matrix_labels.append(tk.Label(matrix_frame, text=f"Row {i+1}"))
    matrix_labels[i].grid(row=i, column=0, padx=5, pady=5)
    for j in range(5):
        matrix_entries.append(tk.Entry(matrix_frame, width=4, relief="sunken", font=("Arial", 20)))
        matrix_entries[i*5+j].grid(row=i, column=j+1, padx=5, pady=5)





# Creating the leaderboard frame
leaderboard_frame = tk.Frame(root, borderwidth=2, relief="groove")
leaderboard_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Creating the leaderboard labels
leaderboard_label = tk.Label(leaderboard_frame, text="Leaderboard")
leaderboard_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
word_label = tk.Label(leaderboard_frame, text="Word")
word_label.grid(row=1, column=0, padx=5, pady=5)
point_label = tk.Label(leaderboard_frame, text="Point")
point_label.grid(row=1, column=1, padx=5, pady=5)

# Creating the leaderboard values
word_values = []
point_values = []
for i in range(10):
    word_values.append(tk.Label(leaderboard_frame, text="-"))
    word_values[i].grid(row=i+2, column=0, padx=5, pady=5)
    point_values.append(tk.Label(leaderboard_frame, text="-"))
    point_values[i].grid(row=i+2, column=1, padx=5, pady=5)

# Defining the update function
def update_leaderboard():
    # Getting the matrix input
    matrix = []
    for i in range(5):
        row = ""
        for j in range(5):
            row += matrix_entries[i*5+j].get().upper()
        matrix.append(row)
    
    # Validating the matrix input
    if len(matrix) != 5 or any(len(row) != 5 for row in matrix):
        tk.messagebox.showerror("Invalid input", "The matrix must be 5x5")
        return
    
    # Finding the words and points
    #words, points = spellcast.find_words_and_points(matrix)
    
    # Updating the leaderboard values
    for i in range(10):
        if i < len(words):
            word_values[i].config(text=words[i])
            point_values[i].config(text=points[i])
        else:
            word_values[i].config(text="-")
            point_values[i].config(text="-")

# Creating the update button
update_button = tk.Button(root, text="Update", command=update_leaderboard)
update_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Starting the main loop
root.mainloop()
