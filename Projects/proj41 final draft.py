#Four-Digit Arabic Numeral to Roman Numeral Converter Program
#Author's Names: Demili Pichay and Eric Pan
#Last Date Modified: March 24, 2021

#function definition for RomanDigitConverter()
def RomanDigitConverter(digit, firstChar, secondChar, thirdChar):
    #for loop for each Roman Numeral possibility for each place value
    #composed of integer division and subtraction
    for M in range(digit//1):
        print("M",end="")
    for CM in range(firstChar//9):
        firstChar=firstChar-9
        print("CM",end="")
    for D in range(firstChar//5):
        firstChar=firstChar-5
        print("D",end="")
    for CD in range(firstChar//4):
        firstChar=firstChar-4
        print("CD",end="")
    for C in range(firstChar//1):
        firstChar=firstChar-1
        print("C",end="")
    for XC in range(secondChar//9):
        secondChar=secondChar-9
        print("XC",end="")
    for L in range(secondChar//5):
        secondChar=secondChar-5
        print("L",end="")
    for XL in range(secondChar//4):
        secondChar=secondChar-4
        print("XL",end="")
    for X in range(secondChar//1):
        secondChar=secondChar-1
        print("X",end="")
    for IX in range(thirdChar//9):
        thirdChar=thirdChar-9
        print("IX",end="")
    for V in range(thirdChar//5):
        thirdChar=thirdChar-5
        print("V",end="")
    for IV in range(thirdChar//4):
        thirdChar=thirdChar-4
        print("IV",end="")
    for I in range(thirdChar//1):
        thirdChar=thirdChar-1
        print("I",end="")
    print()

#function definition of main function
def main():
    #while loop allows rerun of program
    again='y'
    while(again=="y" or again=="Y"):

        #input request for arabic number
        arabNum=int(input("Please enter a year (positive integer between 1000 " \
                          "and 3999):"))

        #assignment of variables
        digit=arabNum//1000
        arabNum=arabNum-(digit*1000)

        firstChar=arabNum//100
        arabNum=arabNum-(firstChar*100)

        secondChar=arabNum//10
        arabNum=arabNum-(secondChar*10)

        thirdChar=arabNum//1
        arabNum=arabNum-(thirdChar*1)
        
        RomanDigitConverter(digit, firstChar, secondChar, thirdChar)

        again=input("Do you want to run the program again? y or Y for yes and n or N for no:")

main()
