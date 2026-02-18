import random 

stages = [
    # Stage 7 - Full Hangman (Game Over)
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
    
    # Stage 6
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    
    # Stage 5
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    
    # Stage 4
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    
    # Stage 3
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    
    # Stage 2
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    
    # Stage 1 - Just the gallows
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]


hangman_logo = ["""
 _   _                                   
| | | |                                   
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\\_| |_/\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/           
"""
]
                                                                          
word_list=["sreejeeta","abir","india"]
Lives = 6

print(hangman_logo)

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder= " "
word_len = len(chosen_word)
for position in range(word_len):
    placeholder += "_"
print("Word to guess: " + placeholder)


game_over = False
correct_list = []

while not game_over:
    print(f"*****************{Lives}/6 Lives left*********************")
    
    Guess= input("Guess a letter: ").lower()   #.lower() is used to make the chosen leeter in lower case even if we had given the leeter in capital letters.
    
    if Guess in correct_list:
        print(f"you have already guessed {Guess}")
        
    
    display= ""
    for letter in chosen_word :
        if letter == Guess:
            display += letter
            correct_list.append(letter)
        elif letter in correct_list:
            display += letter
        else:
            display += "_"
            
    print("Word to guess:" + display)  
    
    if Guess not in chosen_word:
       Lives -= 1
       print(f"You guessed {Guess}, that's not in the word. You Loose a life")
       if letter==0:
           game_over = True
       print(f"*******************IT WAS {chosen_word}!You lose**********************")
       
      
    if "_" not in display:
        game_over = True
        print("******************You Win***********************")

    print(stages[Lives])
        