import random
import sys
from pyfiglet import Figlet


def main():
    global name

    title_figlet()
    name = say_name()
    category = choose_category() #choose category
    lista = set_category(category) #chosse list from category
    global magic_word #the secret word
    magic_word = sort_word(lista) #sort word
    #print(magic_word)
    played_letters = []
    win = True
    game = True
    lives = 8
    points = 0




    while game:
        for letter in magic_word:
            if letter.upper() in played_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
        guess = input("Guess the letter of the magic word: ")
        if guess.isalpha() == False:
            print("Only letters, please!")
        if len(guess) == len(magic_word):
            if guess.upper() == magic_word:

                print("YOU WON! THE MAGIC WORD WAS", magic_word)
                points = lives * 25
                print(f"Score: {points} points")
                sys.exit()
            else:
                print("Wrong word!")

        elif len(guess) > 1:
            lts = len(magic_word)
            print(f"Try 1 letter or {lts} letters to guess the word")
        else:
            played_letters.append(guess.upper())
            if guess.upper() not in magic_word.upper():
                lives -= 1
                if lives > 0:
                    print(f"Wrong letter! You've got {lives} lives left")

        win = True
        for letter in magic_word:
            if letter.upper() not in played_letters:
                win = False

        if lives == 0 or win:
            break

    if win:
        print("YOU WON! THE MAGIC WORD WAS", magic_word)
        points = lives * 25
        print(f"Score: {points} points")
    else:
        print("YOU LOST! THE MAGIC WORD WAS", magic_word)

def say_name():
    name_loop = True
    while name_loop == True:

        name = input("Say your name: ")
        if len(name) == 0:
            print("Don't be shy! Please say your name")
        else:
            name_loop == False
            return name


def title_figlet():

    f = Figlet(font="doom")
    hangame_art = f.renderText("Hangame")
    print(hangame_art)

def choose_category():
    c = True
    print("Hello,", name)
    while c:

        print("1 - Fruits")
        print("2 - Colors")
        print("3 - Animals")
        print("4 - Countries")
        print("5 - Professions")
        category = (input("Choose the category from 1 to 5: "))
        if category.isdigit() == False:
            continue
        else:
            category = int(category)
            if category  < 1 or category > 5:
                print("Out of range!")
            else:
                c = False
                return int(category)

def set_category(c):
    match c:
        case 1:
            words = ["APPLE", "LEMON", "AVOCADO", "GRAPE", "PINNEAPPLE", "ORANGE","STRAWBERRY", "CHERRY", "WATERMELON", "PEACH"]
        case 2:
            words = ["ORANGE", "GREEN", "VIOLET", "YELLOW", "BURGUNDY", "BLACK", "WHITE", "PURPLE", "TURQUOISE", "BROWN"]
        case 3:
            words = ["ZEBRA", "COUGAR", "ELEPHANT", "PARROT", "SNAKE", "MONKEY", "GIRAFFE", "HAMSTER", "CHAMELEON", "BUMBLEBEE"]
        case 4:
            words = ["SPAIN", "MEXICO", "JAMAICA", "BRAZIL", "INDIA", "ARGENTINA", "EGYPT", "PORTUGAL", "MOROCCO", "FRANCE"]
        case 5:
            words = ["DOCTOR", "LAWYER", "ENGINEER", "FARMER", "DRIVER", "FIREMAN", "TEACHER", "DETECTIVE", "DENTIST", "WRITER"]
    return words

def sort_word(l):
    magic_word = random.choice(l)
    return magic_word



if __name__ == "__main__":
    main()


