import random
import tkinter as tk
import sqlite3
from datetime import datetime
from pathlib import Path


def scramble():
    # Shuffle all characters in word
    word = list(entry.get())
    random.shuffle(word)
    scrambled_word = ''.join(word)
    label_scrambled.config(text=scrambled_word)


def keep_word():
    #Saves word into DB

    #Get word and shuffled word
    word = entry.get()
    scrambled = label_scrambled.cget('text')

    #Get current date
    date = datetime.today().strftime('%Y-%m-%d')

    #Insert to SQL DB
    cursor.execute("INSERT INTO words(word,scrambled,date) VALUES(?,?,?)", (word, scrambled, date))
    db.commit()


# Connects to local SQL DB
db = sqlite3.connect('scrambled-words.db')
cursor = db.cursor()

try:
    # Creates headers for DB
    cursor.execute(
        "CREATE TABLE words (id INTEGER PRIMARY KEY, word varchar(250) NOT NULL , scrambled varchar(250) NOT NULL, "
        "date DATE NOT NULL)")
    db.commit()
except sqlite3.OperationalError:
    # Passes when DB already exists
    pass

# Initiate tkinter
window = tk.Tk()
window.title("Word Scrambler")

# Entry Bar
entry = tk.Entry()
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Button to access shuffle function
button_shuffle = tk.Button(text="Shuffle", command=scramble)
button_shuffle.grid(row=1, column=0, padx=10, pady=2)

# Button to access keep function
button_keep = tk.Button(text="Keep Word", command=keep_word)
button_keep.grid(row=1, column=1, padx=10, pady=5)

# Display scrambled word
label_scrambled = tk.Label(text="Scrambled Word")
label_scrambled.grid(row=2, column=0, columnspan=2, padx=10, pady=2)

window.mainloop()
