from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"

profit_list = []
day_list = []

with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        day_list.append(int(line[0]))
        profit_list.append(int(line[4]))

print(day_list)
print(profit_list)





