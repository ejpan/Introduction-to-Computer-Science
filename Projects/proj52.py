#World Series Winners
#Author's Names:Eric Pan and Demili Pichay
#Last Date Modified: April 8, 2021

#opens file for the world series winners
filename=open('WorldSeriesWinners.txt','r')
original_list=filename.readlines()
winners_list=[]
#loop to get rid of the line spacing
for i in range(len(original_list)):
    addition=original_list[i].rstrip('\n')
    #adds each winning team to a new list called winners_list
    winners_list.append(addition)

years_list=[]
start=1903

#loop to create list of the years excluding 1904 and 1994
for e in range(len(winners_list)+3):
    if (start+e)!=1904 and (start+e)!=1994:
        years_list.append(start+e)
    else:
        print()

again="Y"
#loop for asking user for team
while again=="Y":    
    team=input("Enter the name of a team:")
    times=0
    winning_list=[]
    #loop for comparing the users team to the winning team list
    for k in range(len(winners_list)):
        if winners_list[k]==team:
            times+=1
            #winning team and year lists are ordered correspondingly
            #So, we can output the year based on the index of the winners list
            winning_list.append(years_list[k])
            
        else:
            pass
    #changes list to string to print out list without brackets
    str_winning_list=str(winning_list)[1:-1]
        
    print("The",team,"won the world series",times,"times between 1903 and 2009.")
    #team that has not won a world series will be printed out this string
    if winning_list==[]:
        print("The",team,"never won the world series.")
    else:
        print("The winning years are:",str_winning_list)
    #asks user if user wants to run program again
    again=input("Do you want to enter another team name? Y for yes and N for no:")



    

