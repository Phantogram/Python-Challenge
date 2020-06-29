#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies
import os
import csv

# Path to collect data from the Resources folder
election_csvpath = os.path.join('Resources_PyPoll', 'election_data.csv')


# In[ ]:


total_votes=0
khan=0
correy=0
li=0
otooley=0
candidates={}
options = []

# Read in the CSV file
with open(election_csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        total_votes+=1
        name=row[2]

        if name not in options:
            options.append(name)
            candidates[name]=0
        
        candidates[name]+=1
    
# Total votes and percentage of votes for each candidate   
    khan = candidates.get("Khan")
    khan_percent=((khan/total_votes)*100)

    correy = candidates.get("Correy")
    correy_percent=((correy/total_votes)*100)

    li = candidates.get("Li")
    li_percent=((li/total_votes)*100)

    otooley = candidates.get("O'Tooley")
    otooley_percent=((otooley/total_votes)*100)


# In[ ]:


# The winner of the election based on popular vote
winning_votes = 0
winning_candidate = ''

for name, count in candidates.items():
  
   if count > winning_votes: 
       
       #Check results - print(name, ((count/total_votes)*100), count)
       
        if khan > correy and li and otooley:
       
            winning_candidate = "Khan"
            runner_up = "Correy"
            third_up = "Li"
            fourth_up = "O'Tooley"
            # Check results - print(winning_candidate)


# In[ ]:


# Write to new file
PyPollPath=os.path.join('main_pypoll.csv')

with open(PyPollPath,'w') as PyPollPath:
    
    PyPollPath.write(f'Election Results')
    PyPollPath.write("\n")
    PyPollPath.write(f'-------------------------')
    PyPollPath.write("\n")
    PyPollPath.write(f'Total Votes: {total_votes}')
    PyPollPath.write("\n")
    PyPollPath.write(f'-------------------------')
    PyPollPath.write("\n")
    PyPollPath.write(f'{winning_candidate}: {khan_percent:.3f}% ({khan})')
    PyPollPath.write("\n")
    PyPollPath.write(f'{runner_up}: {correy_percent:.3f}% ({correy})')
    PyPollPath.write("\n")
    PyPollPath.write(f'{third_up}: {li_percent:.3f}% ({li})')
    PyPollPath.write("\n")
    PyPollPath.write(f'{fourth_up}: {otooley_percent:.3f}% ({otooley})')
    PyPollPath.write("\n")
    PyPollPath.write(f'-------------------------')
    PyPollPath.write("\n")
    PyPollPath.write(f'Winner: {winning_candidate}')
    PyPollPath.write("\n")
    PyPollPath.write(f'-------------------------')


# In[ ]:




