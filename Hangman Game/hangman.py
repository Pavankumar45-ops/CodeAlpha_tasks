import random

word_list=["python","hangman","computer","programming","devloper"]

stages = [
    r"""
       ------
       |    |
       |    O
       |   /|\
       |   / \
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |   /|\
       |   / 
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |   /|\
       |    
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |   /|
       |    
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |    |
       |    
    ---------
    """,
    r"""
       ------
       |    |
       |    O
       |    
       |    
    ---------
    """,
    r"""
       ------
       |    |
       |    
       |    
       |    
    ---------
    """
]
chosen_word=random.choice(word_list)
display=["-"]*len(chosen_word)
guessed_letters=[]
lives=6

print("---WELCOME TO HANGMAN---")

while "-" in display and lives>0:
    print(stages[lives])
    print(f"word:{''.join(display)}")
    print(f"gussed so far:{','.join(guessed_letters)}")
    guess=input("Guess a Letter:").lower()
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different one!")
        continue
    guessed_letters.append(guess)
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i]==guess:
                display[i]=guess
                print("Good guess")
            else:
                lives-=1
                print(f"wrong '{guess}'is not in the word.lives remaining:{lives}")
if "-" not in display:
    print(f"\nCongratulations You guessed'{chosen_word}'")
else:
    print(stages[0])
    print(f"\GAME OVER. YOU ran out of lives.The word was '{chosen_word}'.")

