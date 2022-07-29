from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"

full_list = []

with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        full_list.append(line)

print(full_list)

#for day in full_list:


