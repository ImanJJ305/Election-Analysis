# The data we need to retrieve
    #Import dependencies
import csv
import os 

    #Assign a variable for the file and a path
file_to_load = 'Documents/Election_Analysis/Resources/election_results.csv'
   
    # Write to another file
     # Create a filename variable to a direct or indirect path to the file.
file_to_save = 'Documents/Election_Analysis/Analysis/election_analysis.txt'

#1. (total number of votes cast) Initializing the accumulator variable that will incrament by 1
total_votes = 0

#2. (candidates voted for) declaring new list and dictionary of candidates for names and votes print
candidate_options = []
candidate_votes = {}

#Winning candidate, count, and percentage variables
winning_cadidate = ("")
winning_count = 0
winning_percentage = 0

    #Open the election results and read the file
with open(file_to_load) as election_data:

    #Read file object with reader function
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in file
    for row in file_reader:

        #Add to the total vote count
        total_votes += 1

        #Print candidate name from each row
        candidate_name = row[2]

        #Avoid candidate name repitition
        if candidate_name not in candidate_options:
            #Add candidate name to list
            candidate_options.append(candidate_name)
            #Tracking candidates vote count
            candidate_votes[candidate_name] = 0

        #Add count to candidate count (out of if statement to increase for each row from the loop)
        candidate_votes[candidate_name] += 1

#Save results to text file
with open(file_to_save, "w") as txt_file:

#Print final count to terminal
        election_results = (f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
#Save final count to text file
        txt_file.write(election_results)

    #3. Percentage for each candidate
        #3.1 Iterate through the candidate list
        for candidate_name in candidate_votes:
         #3.2 Get candidate vote count
            votes = candidate_votes[candidate_name]
            #3.3 Calculate percentage of votes
            vote_percentage = (float(votes) / float(total_votes)) * 100
            #Print name and vote percentage
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% {votes:,})\n") 

            #print candidate, thier voter count, and percentage to terminal
            print(candidate_results)

            #Save it to txt file
            txt_file.write(candidate_results)
        
            #Determing if votes are greater than winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                #True = set winning count equal to votes and winning percentage equal to vote percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #winning candedate
                winning_candidate = candidate_name

             #5. Winner of election winning candidate sumaary
            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                 f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary)
            #Save winning candidate's name to text file
            txt_file.write(winning_candidate_summary)
