from pathlib import Path
import csv
import requests
import json, re

# trial 1

#file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"

#profit_list = []
#day_list = []
#
#with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
#    reader = csv.reader(file)
#    next(reader)
#    for line in reader:
#        day_list.append(int(line[0]))
#        profit_list.append(int(line[4]))
#
#print(day_list)
#print(profit_list)

# trial 2

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"
#summary_path = Path.cwd/"csv_reports"/"summary_report.txt"

empty_list = []

def profitloss_function():
    with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        # Skip the headers
        next(reader)
    
#        for line in reader:
#            line.pop(1)
#            line.pop(1)
#            line.pop(1)
#            float_lst = [float(item) for item in line]
#            empty_list.append(float_lst)
        
    

