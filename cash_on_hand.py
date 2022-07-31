#zandra
import csv

full_list = []
with open(r"C:/Users/zan/Downloads/cash-on-hand-usd.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    
    for line in reader:
        full_list.append(line)

print(full_list)
