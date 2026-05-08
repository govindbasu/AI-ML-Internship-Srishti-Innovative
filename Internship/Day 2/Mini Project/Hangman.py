import random

words = ["apple", "banana", "grapes", "orange", "mango", "peach"]
word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

stages = [
"""
-----
|   |
    |
    |
    |
    |
=========
""",
"""
-----
|   |
O   |
    |
    |
    |
=========
""",
"""
-----
|   |
O   |
|   |
    |
    |
=========
""",
"""
-----
|   |
O   |
/|  |
    |
    |
=========
""",
"""
-----
|   |
O   |
/|\\ |
    |
    |
=========
""",
"""
-----
|   |
O   |
/|\\ |
/    |
    |
=========
""",
"""
-----
|   |
O   |
/|\\ |
/ \\ |
    |
=========
"""
]

while wrong < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())
    
    if "_" not in display:
        print("You win")
        break
    
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed:
        print("Already guessed")
        continue
    
    guessed.append(guess)
    
    if guess in word:
        print("Correct")
    else:
        wrong += 1
        print(stages[wrong])
        print("Wrong guess! Attempts left:", max_wrong - wrong)

if wrong == max_wrong:
    print("You lose")
    print("Word was:", word)
