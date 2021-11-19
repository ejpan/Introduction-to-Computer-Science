#Four-Digit Arabic Numeral to Roman Numeral Converter Program
#Author's Names: Demili Pichay and Eric Pan
#Last Date Modified: March 6, 2021

again="y"
#while loop for rerun of program
while(again=="y" or again=="Y"):
    #input request for arabic numeral
    arabNum=int(input("Please enter a year (positive integer between 1000 " \
                         "and 3999):"))
    print("The corresponding Roman number is:")
    #Finds the range of M (1000) by using integer division. 
    for M in range(arabNum//1000):
        #Numeral is subtracted by the value of Roman Numeral for each loop.
        arabNum=arabNum-1000
        #M will be printed for each 1000 dictated by range while continuing string.
        print("M", end="")
    #for loop for each unique Roman Numeral.
    for CM in range(arabNum//900):
        arabNum=arabNum-900
        print("CM",end="")
    for D in range(arabNum//500):
        arabNum=arabNum-500
        print("D",end="")
    for CD in range(arabNum//400):
        arabNum=arabNum-400
        print("CD",end="")
    for C in range(arabNum//100):
        arabNum=arabNum-100
        print("C",end="")
    for XC in range(arabNum//90):
        arabNum=arabNum-90
        print("XC",end="")
    for L in range(arabNum//50):
        arabNum=arabNum-50
        print("L",end="")
    for XL in range(arabNum//40):
        arabNum=arabNum-40
        print("XL",end="")
    for X in range(arabNum//10):
        arabNum=arabNum-10
        print("X",end="")
    for I in range(arabNum//9):
        arabNum=arabNum-9
        print("IX",end="")
    for V in range(arabNum//5):
        arabNum=arabNum-5
        print("V",end="")
    for IV in range(arabNum//4):
        arabNum=arabNum-4
        print("IV", end="")
    for I in range(arabNum//1):
        arabNum=arabNum-1
        print("I", end="")
    #Ends continuous string.
    print()
    #Input for rerun of program using a while loop.
    again=input("Do you want to run the program again? " \
      "y or Y for yes and n or N for no:")
        
