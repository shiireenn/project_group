from pathlib import Path
import csv

# trial 1

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"

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

empty_list = []

with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader)
    
    for line in reader:
        empty_list.append(line[4])

#empty_list[1].pop(-2)
#empty_list.pop(-3)
#empty_list.pop(-4)

print(empty_list)

#for day in range(empty_list):
#
#    if day < day - 1:
#        print("fail")
#
#    else:
#        print("success")

