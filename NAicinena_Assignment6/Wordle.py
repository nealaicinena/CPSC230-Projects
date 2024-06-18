import random
totalWords = "/Users/nealdabananapeel/Desktop/NAicinena_Assignment6/words.txt" #string of file path to list of words

def getRandomWord(afile): #random word generator
    line = open(afile).read().splitlines() #grabs the file and splits each line into a list
    return random.choice(line) #grabs a random line from the list
    

def printInstructions(): #tells the user to input a 5 letter word
    return "Enter a five-letter word: "

def readInput(word, afile): #sees if the word follows criteria and is in the list of words
    for i in word: #goes thru each letter
        if (97 > ord(i) or ord(i) > 122 or len(word) > 5 or len(word) < 5 or word not in open(afile).read()): #checking ascii index of each letter to see if the letters are only lowercase letters and that the word is in the text file of words
            print("Invalid input\nWords cannot contain any punctuation, spaces, digits, must be all lowercase, and must be a real word")
            return False #returns false if criteria is not met
    else:
        return True #returns true if the word fits criteria and is a word in the list

print("Welcome to wordle!")
print("Wordle is a guessing game where a random 5 letter word is chosen and you must guess it.")
print("You are given 6 attempts and each guess, I will tell you which letters you got right and which ones were in the right place.")
#introduces the user to how wordle works

word = input(printInstructions()) # gets user guess
while (readInput(word, totalWords) == False): #while the guess does not fit criteria...
    word = input(printInstructions()) #keep asking for a new word

wordle = getRandomWord(totalWords) #generates the wordle
tries = 1 #starts at the first try
usedLetters = [] #total used letters set to empty

while word != wordle and tries < 6: #while the user still has more tries and has not guessed the wordle
    correct = [] #correct letters set to 0
    placement = {} #correct letters in the right spot set to 0
    wordle1 = wordle #creates a second wordle to mutilate in code without losing the wordle
    incorrect = [] #incorrect letters set to 0
    letterRepeat = 1 #index for repeated letter set to 0

    for i in word: #itterates through each letter in the guess
        if(i == wordle[word.index(i)]): #if the letter is in the same spot as in the wordle...
            if i in placement.keys(): #if the letter is already in the right spot...
                letterRepeat += 1 #add to the letter repeat
                placement[i + str(letterRepeat)] = word.index(i) + 2 #adds to correct letters in the right spot and the same letter is already in the list, add it again with the index so that theres 2 of the letter for when letters have 2 repeating letters ex) aaron
            else:
                placement[i] = word.index(i) + 1 #just add to the list of correct letters in the right spot
        if (i in wordle1): #if the letter is in the wordle without already guessed correct letters...
            correct.append(i) #adds the correct letter to the list
            wordle1 = wordle1.replace(i, "", 1) #removes the letter from the mutilatable wordle string
        if i not in usedLetters: #if the letter is not in used letters...
            usedLetters.append(i) #add the letter to the list of used letters
        if i not in correct: #if the letter is not in the list of correct letters...
            incorrect.append(i) #add it to the list of incorrect letters

    print("Incorrect guess\nCorrect letters:",correct) #tells the user all the correct letters
    print("Incorrect letters: ", incorrect) #tells the user all the incorrect letters
    print(placement, "These letters are the letters you guessed correctly in the right position") #tells the user the list of all correct letters that are in the right position and tells the user their indexes
    print("You have", 6 - tries, "tries left") #tells the user how many tries they have left
    print("The letters you have already used are", usedLetters) #tells the user all the letters they have already used

    word = input(printInstructions()) #gets the new user guess
    while (readInput(word, totalWords) == False): #while the guess does not fit the criteria...
        word = input(printInstructions()) #ask the user for a new guess
    tries += 1 #add 1 to the number of tries

if(word == wordle): #if the user guesses the wordle...
    print("Congrats! You solved the wordle!\nThe wordle was", wordle, "\nAnd it took you", tries, "tries to guess it") #tell the user they guessed it and how many tries it took
else: #if the user could not guess the wordle...
    print("Sorry! You did not solve the wordle\nThe wordle was", wordle, "\nBetter luck next time") #tell the user what the wordle was