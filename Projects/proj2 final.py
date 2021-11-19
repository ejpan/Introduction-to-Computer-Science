#Date Validity Checker
#Author's Names: Demili Pichay and Eric Pan
#Last Date Modified: February 23, 2021


#Variables used throughout program.
InputDate=(input("Enter a date with the format \"mm dd yyyy\" :"))
Month,Day,Year=InputDate.split()
Month=int(Month)                            
Day=int(Day)
Year=int(Year)


#Displays valid date.
print("Your date: ",Month,"/",Day,"/",Year,sep='')



#If statement if month and day is valid for all months, excluding February.
if (1<= Month <=12):
    if (Month==9 or Month==4 or Month ==6 or Month==11) and Day<=30:            
        print("It is a valid date.")                                                
    elif (Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or \
            Month==10 or Month==12) and Day<=31:                      
        print("It is a valid date.")
#If the month was valid, but not the day.
    elif (Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or \
            Month==10 or Month==12) and Day>31:
        print("It is not a valid date.")
        print("The reason it is invalid: the day value should not be less "\
                    "than 1 or greater than 31.")
#Statement for February.
    elif (Month==2):
            if ((Year%100==0 and Year%4==0) or (Year%4==0)) and Day<=29:
                print("It is a valid date")
            elif Year%100==0 and Day<=29:
                print("It is a valid date")
            elif Day<=28:
                print("It is a valid date")
#If there are more days than there should be during a leap year.
            elif ((Year%100==0 and Year%4==0) or (Year%4==0)) and Day>=28:
                print("It is not a valid date.")
                print("The reason it is invalid: the day value " \
                          "is greater than 29 in February in a leap year.")
#If there are more than 28 days on a non-leap year.
            elif Day>=29:    
                print("It is not a valid date.")
                print("The reason it is invalid: the day is greater than 28 "\
                      "in February in a non-leap year.")
#If there are more than 29 days in February during a leap year.
            elif Day>=30:
                print("It is not a valid date.")
                print("The reason it is invalid: the day value" \
                          "is greater than 29 in February in a leap year.")
#If the date is not valid because there are more than 30 days.
            else:
                pass

#If the date is not valid because the amount of days didn't match the month.
    else:
        print("It is not a valid date.")
        print("The reason it is invalid: the day value is greater than "\
            "30 in a month with just 30 days.")
                    

    
#If the date is not valid because the month does not fall within the range.
elif Month>12:
    print("It is not a valid date")
    print("The reason it is invalid: the month value should be in the range from 1 to 12.")
else:
    pass
