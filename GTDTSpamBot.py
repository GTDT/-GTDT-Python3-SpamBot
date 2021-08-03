"""

                                      By GTDT

        I jus coded a simple spam bot. It might be useful for some of you :D

            You need to open your terminal and install pynput with command:
                                pip install pynput

                                	11/17/2020
"""

## Inporting the libraryes.
from pynput.keyboard import Controller
import time

## Setting some variables to make code more clean.
keyboard = Controller()

## Definition to Spam Selected Text.
def SpamSelectedText():

    ## Spam Delay in seconds.
    global SpamDelay, TypedSpamText, SpamTimes

    ## Variable T for SpamTimes loop.
    T = 0

    ## While loop.
    while T < SpamTimes:
        ## Types the text.
        keyboard.type(f"{TypedSpamText}\n")

        ## Prints spam info in to the console.
        print(f"\nSpammed {T + 1}, Spam delay is {SpamDelay}\nSpam text: {TypedSpamText}\n")

        ## Waits selected time.
        time.sleep(SpamDelay)

        T += 1


## Finction to spam from text file.
def SpamFromSelectedTextFile():

    ## Setting variables to global.
    global FilePath, SpamDelay, SpamTimes

    ## Setting other variables
    TextFile = open(FilePath, "r", encoding='utf8')
    TextFileRead = TextFile.readlines()

    ## Variable T for SpamTimes loop.
    T = 0

    ## For loop to spam all the lines separately.
    for SText in TextFileRead:
        ## Types the text
        keyboard.type(SText)

        ## Prints spam info in to the console.
        print(f"\nSpammed {T + 1}, Spam delay is {SpamDelay}\nSpam text: {SText}\n")

        ## Waits selected time.
        time.sleep(SpamDelay)

        T += 1



        ## Finction to spam selected text.
    def SpamSelectedText():

        ## Spam Delay in seconds.
        global SpamDelay, TypedSpamText, SpamTimes, T

        ## Variable T for SpamTimes loop.
        T = 0

        ## While loop.
        while T < SpamTimes:

            ## Types the text.
            keyboard.type(f"{TypedSpamText}\n")

            ## Prints spam info in to the console.
            print(f"\nSpammed {T + 1}, Spam delay is {SpamDelay}\nSpam text: {TypedSpamText}\n")

            ## Waits selected time.
            time.sleep(SpamDelay)

            T += 1


## Finction to start everything.
def StartEverything():
    global SpamDelay

    ## Asking to select spam mode.
    SpamMode = input("\nPlease select Numbers 1 = Spam Selected Text, are 2 = Spam From Txt File:\n >> ")

    ## If user selects number 2 then running def SpamSelectedText() Finction.
    ## And setting some other variables.
    if SpamMode == "1":

        ## Setting variables to global.
        global TypedSpamText, SpamTimes, StartAfter
        TypedSpamText = str(input("Please type the text that you want to spam:\n >> "))
        SpamDelay = float(input("\nDefault = 1. Please select Spam delay in seconds:\n >> "))
        SpamTimes = int(input("\nPlease type the number how many times do you want to spam the text:\n >> "))
        StartAfter = int(input("\nPlease set after how many seconds do you want to spam the text:\n >> "))
        print(f'\nOk running spam selected text.\n Spam will start after {StartAfter} seconds.')
        time.sleep(StartAfter)
        SpamSelectedText()

    ## If user selects number 2 then running def def SpamFromSelectedTextFile() Finction.
    ## And setting some other variables.
    elif SpamMode == "2":

        ## Setting variables to global.
        global FilePath
        FilePath = str(input("\nPlease type the path of the text file:\n >> "))
        SpamDelay = float(input("\nDefault = 1. Please select Spam delay in seconds:\n >> "))
        StartAfter = int(input("\nPlease set after how many seconds do you want to spam the text:\n >> "))
        print(f'\nOk running spam from selected file.\n Spam will start {StartAfter} seconds.')
        time.sleep(StartAfter)
        SpamFromSelectedTextFile()

    ## If user selects not existing spam mode then printing an error and letting user to choose again.
    else:

        # prints error message to try again.
        print("\nError: You did not select number 1 are 2 please select again:")
        StartEverything()


##Starts the the program.
StartEverything()

## Exit inputs & messages.
OnExit = input("Do you want to spam again? Y/N\n >> ")

if OnExit == "Y" or "y" or "Yes" or "yes":
    StartEverything()
else: exit()
 
