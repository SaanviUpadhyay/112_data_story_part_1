# Importing required files 

from distutils.spawn import spawn

import pandas as pd
import statistics
import csv

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

#  Reading the data file
df   = pd.read_csv('data.csv')
data = df['quant_saved']

# Figure
fig = px.scatter(df , y = "quant_saved" ,  color = "female")
fig.show()

#  Processing the data
mean    = statistics.mean(data)
mode    = statistics.mode(data)
median  = statistics.median(data)
std_dev = statistics.stdev(data)

# Printing the data
print('Mean of the money saved is ' , mean)
print('Mode of the money saved is ' , mode)
print('Median of the money saved is ' , median)
print('Standard deviation of the money saved is ' , std_dev)

# Standard Deviation
std_dev_1_start , std_dev_1_end  =  mean-std_dev     , mean+std_dev
std_dev_2_start , std_dev_2_end  =  mean-(2*std_dev) , mean+(2*std_dev)
std_dev_3_start , std_dev_3_end  =  mean-(3*std_dev) , mean+(3*std_dev)

# Checking if studies and money are related

with open("data.csv" , newline='') as f :
    reader       = csv.reader(f)
    savings_data = list(reader)

savings_data.pop(0)

# Finding total no of people who completed the high school

total_entries         = len(savings_data)
completed_high_school = 0

for data in savings_data :
    if(int(data[3]) == 1) :
        completed_high_school += 1

fig = go.Figure(
    go.Bar(x = ["Completed high school" , "Not completed high school"] , 
    y = [completed_high_school , 
    (total_entries-completed_high_school)]
    ))
fig.show()

gender = []
savings =[]

for data in savings_data :
    if(float(data[2]) != 0):
        gender.append(float(data[2]))
        savings.append(float(data[0]))

correlation = np.corrcoef(gender , savings)
print("Correlation between gender and savings is " , correlation[0,1])











