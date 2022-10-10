# The data we need to retrieve
    #Assign a variable for the file and a path
file_to_load = 'Resources/election_results.csv'
    #Open the election results and read the file
with open(file_to_load) as election_data:
     #Data analysis print
     print(election_data)
# 1. Total number of votes cast
# 2. Complete list of condidates voted for
# 3. Percentage of voted each candidate won
# 4. Total number of voted each candidate won
# 5. Winner of the election (based on popular vote)