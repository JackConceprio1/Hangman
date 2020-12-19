# imported moudels
import random

# these are the words that the user can try and guess
listOfWords = ["Apples","Citrus","Stone fruit","Tropical","Berries","Melons"]

# this is the main game loop
while True:
    # as the user if they want to play
    isPlaying = input("do you want to play? (y/n) ")
    # if the user types y
    if isPlaying.lower() == "y":
        # set the users lives to 5
        lives = 5
        # pick a roundom word from selectedWord
        selectedWord = random.choice(listOfWords)
        # when the user guess a letter it will be stored here
        lettersGuess = []
        # this will track the user word
        guessingWord = ""
        # this will loop over the length of selectedWord and add - to guessingWord
        for i in range(len(selectedWord)):
            guessingWord += "-"
        while True:
            print("------------------------------------------------------")
            # check to see how meny lives the user has
            if lives == 0:
                break
            # check to see if there are any - in the string
            if guessingWord.find("-") == -1:
                break
            
            print("lives: " + str(lives))
            print("guessing word: "+guessingWord)
            # this is asking the user to guess the letter
            letterGuessed = input("Guess a letter: ")
            # check to see if the given number is not equl to 1
            if len(letterGuessed) != 1:
                print("you must enter in a one letter")
            # check to see if the user has entered a string
            elif(letterGuessed.isnumeric()):
                print("you must enter in a letter")
            else:
                # if the user has entered a uppercase letter then convert it to lowercase
                letterGuessed = letterGuessed.lower()
                found = False
                # this will check to see if the user has entered the letter all ready
                for i in lettersGuess:
                    if letterGuessed == i:
                        found = True
                # check to see it the user had enterd the letter
                if found == True:
                    print("you have all ready geussed that letter try again")
                else:
                    # split the guessing word in to a list
                    guessingWordList = list(guessingWord)
                    found = False
                    # check to see if the users input letter is in the string
                    for i in range(len(list(selectedWord))):
                        j = list(selectedWord)[i]
                        if j.lower() == letterGuessed:
                            guessingWordList[i] = j
                            found = True
                    # if the letter had been found
                    if found == True:
                        # convert the list to a string
                        guessingWord = ''.join(guessingWordList)
                        print("found a letter")
                        print(guessingWord)
                        # add to the letters guessed
                        lettersGuess.append(letterGuessed)
                    # if the letter has not been found
                    else:
                        # add to the letters guessed
                        lettersGuess.append(letterGuessed)
                        # remove a life
                        lives -= 1
        # if the user had run out of lives show message
        if lives == 0:
            print("you have ran out of lives")
        # if the user has no more letters to guess then show message
        elif letterGuessed.find("-") == -1 :
            print("you win well done")
    
    # if the user types n then exit the game
    elif isPlaying.lower() == "n":
        exit()
    # if the user types anything else it will show an error
    else:
        print("you must type y or n")