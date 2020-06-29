#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

# Path to collect data from the Resources folder
budget_csvpath = os.path.join('Resources_PyBank', 'budget_data.csv')


# In[2]:


total_months=1
total_profloss=0
changes=[]
months=[]

# Read the CSV file
with open(budget_csvpath) as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    first_row= next(csvreader)
    total_profloss += int(first_row[1])
    previous_revenue=int(first_row[1])
    
    
    # Loop through the data
    for row in csvreader:
            
        total_months += 1
        total_profloss += int(row[1])
        changes.append(int(row[1]) - previous_revenue)
        previous_revenue=int(row[1])
        months.append(row[0])


# In[3]:


# The greatest increase in profits & greatest decrease in losses
greatest_inc = max(changes)
greatest_dec = min(changes)

greatest_inc_months=months[changes.index(greatest_inc)]
greatest_dec_months=months[changes.index(greatest_dec)]


# In[4]:


# The average of the changes
monthly_average=sum(changes)/len(changes)


# In[5]:


# Write to new file
newFilePath=os.path.join('main_pybank.csv')

with open(newFilePath,'w') as newFile:
    
    newFile.write(f'Financial Analysis')
    newFile.write("\n")
    newFile.write(f'-------------------------------')
    newFile.write("\n")
    newFile.write(f'Total Months: {total_months}')
    newFile.write("\n")
    newFile.write(f'Total: ${total_profloss}')
    newFile.write("\n")
    newFile.write(f'Average Change: ${monthly_average:.2f}')
    newFile.write("\n")
    newFile.write(f'Greatest Increase in Profits: {greatest_inc_months} (${greatest_inc})')
    newFile.write("\n")
    newFile.write(f'Greatest Decrease in Profits: {greatest_dec_months} (${greatest_dec})')
    


# In[ ]:




