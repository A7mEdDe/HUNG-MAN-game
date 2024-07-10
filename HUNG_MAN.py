# HUNG MAN GAME
import random

# importaword
def importaword():
    with open("words.txt","r") as file :
        words = file.read().split() # list 
        word = random.choice(words)
        sorted_word = sorted(word)
    return word , sorted_word    

# print(importaword())                     


# checker 
def checker(gussed_letter , new_word , correct , my_word ,number_of_tries) :
    if gussed_letter in new_word :
        correct.append(gussed_letter)
        my_word = hd(new_word , correct , 0)
    else :
        number_of_tries -= 1    
        print(f"Incorrect guess!!. Try again , You have {number_of_tries} tries .")
    return correct , my_word , number_of_tries

def hd(new_word , correct , flage ) :
    display = ''.join(char if char in correct else '_' for char in new_word)
    if flage :
     print(f"Current Word : {display}")
    return display

# input_litter
def input_litter(History,number_of_tries) :
    new_letter = input("Guess a letter :")
    if new_letter:
             new_letter = new_letter[0]
    else:
         print("Please enter a letter.")
         
     
    if new_letter in History:
         print(f"You've already guessed the letter '{new_letter}'. Try again.")
         
     
    History.append(new_letter)

    return new_letter , History , number_of_tries    
     
        


# printer
def printer(my_word,new_word) :
    if my_word == new_word :
        return True
    else :
          return False


     
# Main Game
def  Main_Game():
    new_word , sorted_chars = importaword()
    number_of_tries = 10
    History = []
    correct = []
    my_word = []
    

    print(new_word)
    
    while number_of_tries > 0 and (my_word) != new_word:
       hd(new_word , correct , 1 )
       new_letter , History , number_of_tries = input_litter(History,number_of_tries)
       correct , my_word , number_of_tries = checker(new_letter, new_word , correct , my_word ,number_of_tries )
       
       
       if printer(new_word , my_word) : 
        break

    if(printer(new_word , my_word)) :
        print("Congratulations you won !!")   
    else :
        print(f"Game Over !!  You've run out of tries. The correct word was '{new_word}'.") 


    
Main_Game()