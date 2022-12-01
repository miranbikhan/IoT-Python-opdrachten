import random
from collections import Counter

underline = "_"

with open ("c:/Users/mrnbkhn/IoT-python/IoT-Python-opdrachten/Hangman/woordenlijst.txt", "r") as wordlist:
    alleTekst = wordlist.read()
    words = list(alleTekst.split())

    the_word = (random.choice(words))
    print(the_word)
    print (underline * len(the_word))

word_counter = Counter(the_word)

print (word_counter)

gokken = []

gok = input("Gok een letter: ")

gokken.append(gok)

print(gokken)
