# The data we need to retrieve.
# 1. The total number of votes
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
#Print the present time
print("The time right now is", now)

#Add our dependencies
import csv
import os
#Assign a variable for the file to load 
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

candidate_options = []

candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read and print each row in the CSV file
    headers = next(file_reader)

    #print each row in the CSV file.
    for row in file_reader:
        #total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any exisiting candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate's count
        #Putting this within the if statement will only render us 1 in the dictionary
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as election_data:
#Print the final vote count 
    election_results = (
        f"Election Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    election_data.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4. Print the candidate name and percentage of votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
        #Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        # print out the winning candidate,vote count and percentage 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage 
        print(candidate_results)
        election_data.write(candidate_results)

    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    print(winning_candidate_summary)
    election_data.write(winning_candidate_summary)