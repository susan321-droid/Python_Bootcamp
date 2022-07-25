import random
from re import A
import word_lists
from hangman import stages,logo

print(logo)



word=random.choice(word_lists.word_list)
print(word)
display=[]
lives=6
for letter in word:
    display+="_"
input_lists=[]

while lives != 0:
    guess_letter=input("Guess any letter:\n").lower()

    if guess_letter in input_lists:
        print("Letter already used")
    else:
        input_lists.append(guess_letter)
        if guess_letter not in word:
            lives -=1
            print(stages[lives])
        else:
            for guess_position in range (len(word)):
                letter=word[guess_position]
                if letter==guess_letter:
                    display[guess_position]=letter
        display_result=''.join(display)
        print(display_result)
        result=''.join(input_lists)
    if result == word:
        print("You won")
        break
else:
    print("lose")


        
       




