import random
from collections import Counter

def hangman():
    # with open ("./woordenlijst.txt", "r") as wordlist:
    #     alleTekst = wordlist.readlines()
    #     word = (random.choice(alleTekst)).strip()
    word = "appelsien"
    galgje1 = "  ___"
    galgje2 = " /  |"
    galgje3 = " |"
    galgje4 = " |"
    galgje5 = " |"
    galgje6 = "_|_"

    
    # abc = ("abcdefghijklmnopqrstuvwxyz")
    # alphabet = list(abc)
    word_list = list(word)
    word_list2 = list(word)
    rights = []
    wrongs = []
    tries = 0
    combo = " "
    bonus = 0

    while len(word_list2) > 0:
        print(bonus)
        print(galgje1)
        print(galgje2)
        print(galgje3)
        print(galgje4)
        print(galgje5)
        print(galgje6)
        print(combo)
        if bonus >= 3:
            print("\nJoker is in effect now.\n")
        
        if tries == 6:
            print("Sorry, you ran out of ""life"".")
            print("The word we were looking for was:", word)
            again = (input("do you want to play again? y/n "))
            if again == "y":
                hangman()
            else:
                exit("See you in another life, bruvva!")

        for m in word:
            if m in rights:
                print(m, end='')
            else:
                print('_', end='')
        
        print(" ", wrongs)

        guess = input("\nGuess a letter or the right word... ")

        if guess in rights:
            print("\nYou already used that one chief.")
            continue
        elif guess == word:
            print("correct")
            toGuess = word
            print("You guessed it right")
            print("The word we were looking for was ", toGuess, ".")
            again = (input("do you want to play again? y/n "))
            if again == "y":
                hangman()
            else:
                exit()
            
        elif guess in word_list:
            if len(guess) == len(word):
                if guess == word:
                    print("You guessed it right")
                    print("The word we were looking for was ", toGuess, ".")
                    again = (input("do you want to play again? y/n "))
                    if again == "y":
                        hangman()
                    else:
                        exit()

            elif guess.isalpha() == True:
                bonus += 1
                if bonus == 0:
                    combo == ""
                elif bonus == 1:
                    combo = "\nNice!\n"
                elif bonus == 2:
                    combo = "\nGREAT! 2 right letters in a row!!\n"
                elif bonus == 3:
                    combo = "\nC-C-C-C-COMBO!!! 3 right letters in a row!! You've earned a joker.\n"
                else:
                    combo = ("")

                rights.append(guess)
                for l in word_list:
                    if l == guess:
                        word_list2.remove(guess)
                continue
            else:
                print("Please one letter at a time!")
        
        elif guess not in word_list:
            if guess in wrongs:
                print("You already used that letter")
                continue
            else:
                wrongs.append(guess)
                if bonus >= 3:
                    print("You got spared by your joker.")
                    bonus = 0

                else:
                    tries += 1
                    if tries == 1:
                        galgje3 = " |  O"
                    elif tries == 2:
                        galgje4 = " |  |"
                    elif tries == 3:
                        galgje4 = " | /|"
                    elif tries == 4:
                        galgje4 = " | /|\\"
                    elif tries == 5:
                        galgje5 = " | /"
                    else:
                        galgje5 = " | / \\"
                        print("You dead!")
                    continue
        else:
            print("please use a letter")
            continue

hangman()

    