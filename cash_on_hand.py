#zandra
from pathlib import Path
import csv

full_list = []
with open(r"./csv_reports/cash_on_hand.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        full_list.append(line)

print(full_list)
