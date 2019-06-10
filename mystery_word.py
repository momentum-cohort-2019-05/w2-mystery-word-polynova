import random

#gah why was it not working, keeps giving me syntax error 

def show_instructions():
        print("Welcome to a new game, please select the level you would like to play.")
        print("Easy level plays 4-6 characters long. ")
        print("Normal level plays 6-8 characters long. ")
        print("Hard level plays 8+ characters long. ")

easy_words = []
normal_words = []
hard_words = []

with open ('words.txt') as word_file:
        for list_words in word_file.readlines():
                all_list_words = list_words.split()


                if len(all_list_words) >= 4 and len(all_list_words) <= 6:
                        easy_words.append(all_list_words)
                elif len(all_list_words) >= 6 and len(all_list_words) <= 8:
                        normal_words.append(all_list_words)
                elif len(all_list_words) >= 8:
                         hard_words.append(all_list_words)
        
        print('easy_words')
        print('normal_words')
        print('hard_words')


def get_selection():
        user_selection = input(
        "Please select the level you would like to play. Enter 1 for easy level, 2 for normal level and 3 for hard level."

)

        if user_selection == "1":
               all_list_words = random.choice(easy_words)
        elif user_selection == "2":
                all_list_words = random.choice(normal_words)
        elif user_selection == "3":
                all_list_words = random.choice(hard_words)

        return user_selection

        show_word = (get_selection)
        print(show_word)


def display_letter(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"


def get_guess():
    guess = input ("Give me a letter")
    return str

def checkguess(g,str):
    if g == str:
        return True
        else:
        return False 
        
mystery = random.randint(word):

While True:

guess = get_guess()

if checkguess (guess)


        