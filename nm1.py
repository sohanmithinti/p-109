import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv 
import statistics

count = []
sum1 = []
for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum1.append(dice1 + dice2)
    count.append(i)

mean = sum(sum1)/len(sum1)
median = statistics.median(sum1)
mode = statistics.mode(sum1)
std = statistics.stdev(sum1)

print(mean)
print(median)
print(mode)
print(std)

std1_start = mean - std 
std1_end = mean + std 
std2_start = mean - (2* std)
std2_end = mean + (2* std)
std3_start = mean - (3* std)
std3_end = mean + (3* std)

array1 = []
array2 = []
array3 = []

for x in sum1:
    if(std1_start < x < std1_end):
        array1.append(x)
    if(std2_start < x < std2_end):
        array2.append(x)    
    if(std3_start < x < std3_end):
        array3.append(x)    

percentage1 = len(array1)*100/len(sum1)
percentage2 = len(array2)*100/len(sum1) 
percentage3 = len(array3)*100/len(sum1)

print(std1_start)
print(std1_end)
print(percentage1)
print(percentage2)
print(percentage3)

graph = ff.create_distplot([sum1], ["result"], show_hist = False)
graph.show()