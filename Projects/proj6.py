#Average Score for Review Program
#Eric Pan and Demili Pichay
#April 21, 2021

#average_score function that takes the a word and file name as the parameter
def average_score(word,file_name):
        #open and reads the file
        files=open(file_name,'r')
        #creates a list for the reviews
        file=files.readlines()
        keepscore=0
        loopcount=0
        estimated_score=0
        #for loop to iterate each review in the file
        for line in file:
            #removies \t\n and splits each word into individual elements
            rating_line=line.rstrip('\t\n').split(" ")
            #assigns the rating to a variable
            rating=rating_line[0]
            #changes the rating to an integer
            rating=int(rating)
            #removes the rating from the review
            rating_line.remove(rating_line[0])
            
            #compares the word to the list
            if word in rating_line:
                #if the word is in the list, the rating will be added to keepscore 
                keepscore=keepscore+rating
                #keeps track of how many review lines the word is in
                loopcount+=1
        #if the word is in no reviews, returns 2 as the rating 2 is neutral
        if loopcount==0:
                return 2
        else:
                #total of the rating divded by count will output the average
                estimated_score=(keepscore/loopcount)
                return estimated_score

def main():
        
        again="y"
        #while loop if user wants to run again
        while again=="y":
                #asks user for review
                user_review=input("Enter a movie review: ")
                #splits user's review into a list with elements consisting of individual words
                split_user_review=user_review.split(" ")
                #asks user for a file
                file_name=input("Enter the name of the file containing reviews: ")
                loopcount=0
                average_total=0
                #iteration for each word in user's review
                for word in split_user_review:
                    #lower cases each word
                    word=word.lower()
                    #the function average_score outputs the average score rating
                    average_rating=average_score(word,file_name)
                    #totals the average rating for all the words
                    average_total=average_total+average_rating
                    #keeps count of how many words are in the user's review
                    loopcount+=1
                #average rating for all the words in user's review    
                estimated_score=format((average_total/loopcount),'.2f')
                #converts average rating for user's review into int for comparison
                int_score=int(average_total/loopcount)
                #if statement to output the rating's review in words

                if int_score==0:
                        score="(negative)"
                elif int_score<1:
                        score="(somewhat negative)"
                elif int_score<2:
                        score="(neutral)"
                elif int_score<3:
                        score="(somewhat positive)"
                elif int_score<=4:
                        score="(positive)"
                        
                print("Estimated score:",estimated_score,score)
                #asks user if user wants to run program again
                again=input("Do you want to run the program again? (y for yes and n for no) ")

main()

    


            
            

            


