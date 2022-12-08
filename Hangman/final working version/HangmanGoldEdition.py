import random
from collections import Counter

def hangman():
    with open (".woordenlijst.txt", "r") as wordlist:
        alleTekst = wordlist.readlines()
        word = (random.choice(alleTekst)).strip()

    galgje1 = "  ___"
    galgje2 = " /  |"
    galgje3 = " |"
    galgje4 = " |"
    galgje5 = " |"
    galgje6 = "_|_"
    word_list = list(word)
    word_list2 = list(word)
    rights = []
    wrongs = []
    tries = 0
    combo = " "
    bonus = 0

    while len(word_list2) > 0:

        if bonus == 0:
            combo = ""
        elif bonus == 1:
            combo = "\nNice!\n"
        elif bonus == 2:
            combo = "\nGREAT! 2 right letters in a row!!\n"
        elif bonus == 3:
            combo = "\nC-C-C-C-COMBO!!! 3 right letters in a row!! You've earned a joker.\n"
        else:
            combo = ("")

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
        elif tries == 6:
            galgje5 = " | / \\"

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
            print("\nSorry, you ran out of 'life'.")
            print("The word we were looking for was:", word)
            again = (input("Do you want to be hanged again eehh... I mean play again? y/n "))
            if again == "y":
                hangman()
            else:
                exit("See you in the after life, bruvva!")
        
        for m in word:
            if m in rights:
                print(m, end='')
            else:
                print('_', end='')
        
        print(" ", wrongs)

        guess = input("\nGuess a letter or the right word... ")
        

        if guess.isalpha() == True:
            if len(guess) == 1:
                if guess in rights:
                    print("\nYou already used that one chief.\n")

                elif guess in wrongs:
                        print("\nYou already used that letter\n")

                elif guess in word_list:
                    bonus += 1
                    rights.append(guess)
                    for l in word_list:
                        if l == guess:
                            word_list2.remove(guess)

                elif guess not in word_list:
                    if bonus >= 3:
                        print("\nYou got spared by your joker.\n")
                        bonus = 0

                    else:
                        wrongs.append(guess)
                        tries += 1
                        bonus = 0

            elif len(guess) == len(word):
                if guess == word:
                    print("\nCongrats, you didn't get hanged .... yet!")
                    print("The word we were looking for was indeed ", word, ".")
                    again = (input("Waddya say? Again? y/n "))
                    if again == "y":
                        hangman()
                    else:
                        exit("Too bad, I really wanted to see you get hanged ehh  I mean win again... <_<")
            elif len(guess) >= len(word):
                print("Try a word with less letters...!!")
                tries += 1
                bonus = 0

            elif len(guess) <= len(word):
                print("Try a word with more letters..!!")
                tries += 1
                bonus = 0

            else:
                print("Hmmm it's tuesday, innit?")
        else:
            print("I only accept alphabetical characters... and cash, cash as well!")

hangman()

    