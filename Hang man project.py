#

import random
from logo import stages
end_of_game = False
from word_list import word_list
List = word_list
chosen_word = random.choice(List)
Lives = 6

from logo import logo
print(logo)

print(f"Psst the word is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(word_length)

while not end_of_game:
    guess = input("Enter: ").lower()
    for p in range(word_length):
        letter = chosen_word[p]
        #print(f"Current position: {p}\
        # Current letter: {letter}\
        #Guessed letter: {guess}")
        if letter == guess:
            display[p] = letter
    if guess not in chosen_word:
        Lives -= 1
   
    print(display)
    print(Lives) 

    if "_" not in display:
        end_of_game = True
        print("You won")
    if Lives == 0:
            end_of_game = True
            print("You lost")
    print (stages[Lives])




   

