# election-analysis

# Overview of the Election Audit
Tom and Seth, Colorado board of elections employees, asked for assistance in an election audit of a US congressional precinct in Colorado.  The goal was to utilize the programming language Python to return the total number of votes for each candidate, the percentage of votes for each candidate and the winner of the election based on the popular vote.  The election results data was provided in a csv file, which is what we used for the analysis. 

After the candidate results were provided, the election commission requested voter turnout for each county, the percentage of votes from each county of the total counts and the county that had the highest turnout.  This was achieved by adding new lines of code to our existing code that returned the candidate results.  I then had the candidate and county results saved to a text file for the election commission’s review.  

# Election Audit Results
* Total number of votes cast in this congressional election?
 - There was a total of 369,711 votes cast in this congressional election.
* Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
 - Jefferson county casted a total of 38,855 votes which made up 10.5% of the total votes cast in this congressional election.
 - Denver county casted a total of 306,055 votes which made up 82.8% of the total votes cast in this congressional election.
 - Arapahoe county casted a total of 24,801 votes which made up 6.7% of the total votes cast in this congressional election.
* County with the largest number of votes?
 - The county of Denver had the largest number of votes cast (306,055) in this congressional election.
* Breakdown of the number of votes and the percentage of the total votes each candidate received.
 - Candidate Charles Casper DeGette received 85,213 votes which made up 23.0% of total votes cast in this congressional election.
 - Candidate Diana DeGette received 272,892 votes which made up 73.8% of total votes cast in this congressional election.
 - Candidate Raymon Anthony Doane received 11,606 votes which made up 3.1% of total votes cast in this congressional election.
* Winning candidate of the election, with their vote count, and their percentage of the total votes?
 - Candidate Diana DeGette won the election with a total of 272,892 votes which made up 73.8% of total votes cast in this congressional election.

# Election Audit Summary
The election commission can use this Python script for any future elections with minor modifications to the script.  This would allow the election commission to receive future election results in a more efficient and accurate manor. 

As long as future election data is provided the same way (Ballot ID, County, Candidate) we can modify the exciting script by changing the file_to_load path to a new csv file and execute the script to return results based on the new data file.  In this example file_to_load = os.path.join(“Resources”, “NEW_election_results.csv”)

If the future election data is provided but in a different order (Ballot ID, Candidate, County) we can simply modify lines of code that get the correct candidate and county name from each row.  In this example candidate_name = row[1] and county_name = row [2]. 

Lastly, we can always modify how the election results are printed to our results file.  We could modify the print to terminal sections to only see the winner’s results, only results from a specific county or to include a message by simply adding or removing sections of the print code.
