#Flashcard Application - CS50p Final Project - Anna Zwolińska

import sys
import random
import json


mydict = "mydictionary.json"

def main():
    legend = "\nSelect one of the following commands:\nadd - to add a new word or a phrase to the existing set\nrem - to remove a word or a phrase from the existing set\ntest - to test your knowledge\nexitf - to exit the flashcards\n\nCommand: "
    command = "0"
    commands = ["add", "rem", "test", "exitf"]
    diction = loaddiction()

#if no arg command, show the instructions "legend", continue doing so as long as no command from the list chosen
    if  len(sys.argv) == 1:
        command = input(legend)
        while command not in commands:
            print("\nUnknown command.")
            command = input(legend)
#if an arg command, check if it's one of the existing commands + if not existing, ask to select:
    elif len(sys.argv) > 1 and sys.argv[1] not in commands:
        print(sys.argv[1])
        command = input(legend)
        print(command)

#if an arg command and it's one of the existing commands:
    if len(sys.argv) > 1 and sys.argv[1] == commands[0] or command == commands[0]:
        addaword(diction) #if command "add" was chosen
    if len(sys.argv) > 1 and sys.argv[1] == commands[1] or command == commands[1]:
        remaword(diction) #if command "rem" was chosen
    if len(sys.argv) > 1 and sys.argv[1] == commands[2] or command == commands[2]:
        n = int(input("How many words do you want to test? Number: "))
        takeatest(diction, n) #if command "test" was chosen + number of words in the test
    if len(sys.argv) > 1 and sys.argv[1] == commands[3] or command == commands[3]:
        exit() #exit the program

#load the json file
def loaddiction():
    try:
        with open(mydict, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Dictionary file not found. Creating a new one.")
        return {}

#add a word to the library DONEEE!
def addaword(diction):
    #loop to request a word to be added: 1) if 'exitf' - stop 2) if exists - ask again
    while True:
        word = input("Enter a word or type 'exitf' to stop: ")
        if word == "exitf":
            break
        if word in diction:
            print(f"{word} already exists in the dictionary.")
            continue
        #3) if none of those - ask for the definition and save it to the json file
        else:
            definition = input("Definition: ")
            diction[word] = definition
            with open(mydict, 'w') as file:
                json.dump(diction, file, indent=4)
            print(f"OK, '{word} = {definition}' has been added.")
            break

#remove a word from the library DONEEE!
def remaword(diction):
    while True:
        toremove = input("Insert a word to be removed or type 'exitf' to stop: ")
        if toremove in diction:
            removeddef = diction[toremove]
            del diction[toremove]
            with open(mydict, 'w') as file:
                json.dump(diction, file, indent=4)
                print(f"OK, '{toremove} = {removeddef}' has been removed.")
                break
        elif toremove == "exitf":
            break
        else:
            print("The word has not been found.")
            continue


#take a test with n numbers of user's input
def takeatest(diction, n):
    o = 0
    #c = number of correct answers
    c = 0
    #create a dictionnary list
    dictionlist = list(diction)

    troublelist = []
    welldone = ["neat", "cool", "nice job", "you're doing well", "good", "bravo", "felicitation", "super", "sharp"]
    while o < n:
        #choose a random definition of a word from dictionlist
        #if diction[random.choice(dictionlist)] != "definition":
        #guesses must be unique
        correctan = random.choice(dictionlist)
        toguess = diction[correctan]

        guess = input(str(o+1) + ") " + toguess + " = ")
        o += 1
        if guess == correctan:
            c += 1
            print(random.choice(welldone)+"!")
        else:
            #add the incorrect word to the troublelist
            troublelist.append(correctan)
            print(f"Incorrect. Correct answer: '{correctan}'")
        #delete the tested words from the list, so that they don't reoccur
        dictionlist.remove(correctan)

    while o == n:
        if c == n:
            print("Excellent! All answers correct")
            break
        else:
            print(f"Test completed. Correct answers: {c}/{n}")
            adtest = input("Do you want to train the words you didn't guess? Y/N: ").lower()
            #additional test
            if adtest == "y":
                print("Sure! Let's review the troublemaking words: ")
                training(diction, troublelist)
                break
            if adtest == "n":
                print("Session ended.")
                break
#re-test
def training(diction, troublelist):
    #zrob test, gdy w liscie bledow znajduja sie jakies pozycje. Po skonczeniu podaj wynik i spytaj znow
    #czy chce ten test czy nie

    while True:
        newtroublelist = []
        tc = 0
        o = 1
        welldone = ["neat", "cool", "nice job", "you're doing well", "good", "bravo", "felicitation", "super", "sharp"]
        tn = len(troublelist)
        while len(troublelist) > 0:
            #random word to guess
            correctan = random.choice(troublelist)
            toguess = diction[correctan]
            guess = input(str(o) + ") " + toguess + " = ")
            troublelist.remove(correctan)
            if guess == correctan:
                tc += 1
                print(random.choice(welldone)+"!")
            else:
                newtroublelist.append(correctan)
                print(f"Incorrect. Correct answer: '{correctan}'")
            o += 1
        if len(troublelist) == 0:
            if tc == tn:
                print("Excellent! All answers correct.")
                break

            else:
                print(f"Re-test completed. Correct answers: {tc}/{tn}")
                # Update troublelist with remaining trouble words
                troublelist = newtroublelist
                adtest = input("Do you want to train the words you didn't guess? Y/N: ").lower()
                #yet another additional test
                if adtest == "y":
                    print("Sure! Let's review the troublemaking words: ")
                    continue
                if adtest == "n":
                    print("Session ended.")
                    break


if __name__ == "__main__":
    main()

