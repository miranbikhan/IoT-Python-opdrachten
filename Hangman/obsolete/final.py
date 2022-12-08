abc = ("abcdefghijklmnopqrstuvwxyz")
alphabet = list(abc)
word = "banaan"
word_list = list(word)
word_list2 = list(word)
guesses = []
wrongs = []
tries = 0

while len(word_list2) > 0:

    if tries == 6:
        print("Sorry, you ran out of ""life"".")
        print("The word we were looking for was:", word)
        exit("see you in the after life")

    toGuess = [ letter if letter in guesses else "_" for letter in word]
    print("".join(toGuess))

    guess = input("guess a letter: ")
    if guess in guesses:
        print("you already used that one chief")
        continue
    elif guess in alphabet:
        if guess in word_list:
            guesses.append(guess)
            for l in word_list:
                if l == guess:
                    word_list2.remove(guess)
                    continue
    
        elif guess not in word_list:
            if guess in wrongs:
                print("you already used that letter")
                continue
            else:
                wrongs.append(guess)
                tries += 1
    else:
        print("please use a letter")
        continue


        
    print("these are your tries: ", tries)
    print("these are wrong guesses: ", wrongs)
    print("these are right guesses: ", guesses)
    print(word_list2)

print(word)
print("you guessed it right")






 # if guess in word_list:
            #     for l in word_list:
            #         if guess == guess:
            #             word_list.remove(guess)
            #             continue