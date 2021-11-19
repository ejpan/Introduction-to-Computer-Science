#Guessing Game
#Eric Pan and Demili Pichay
#March 24, 2021

#imports the random module for the random integer
import random

#function for the guessing game that uses the random number as the argument
def playGuessingGame(number):
        retry=False
        tries=0
        #loop for incorrect guess
        while(retry==False):
            guess=int(input("Enter a number between 1 and 100, or 0 to quit:"))
                #Adds 1 for each try (loop)
            tries+=1
            if guess>number:
                print("Too high, try again")
                retry=False
            elif guess<number and guess>0:
                print("Too low, try again")
                retry=False
                #Ends loop for user to quit
            elif guess==0:
                retry=False
                return guess
                #Ends loop when user guesses correctly
            elif guess==number:
                retry=True
                print("Congratulations! After ",tries,"times, you guessed the right number!")
                return guess
def main():
    
    again=True
    #loop for playing the guessing game
    while again==True:
        #random number
        number=random.randint(1,101)
        #runs the function for the guessing game and takes number as arguement
        guess=playGuessingGame(number)
        #asks if user wants to play guessing game again
        if guess==0 or guess==number:
            again=input("Do you want to play the game again? Enter y or Y for yes," \
                        " n or N for no:")
            if again=="y" or again=="Y":
                again=True
            else:
                #using putting anything but y or Y will end program
                again=False
                print("Thanks for playing!")
main()        
