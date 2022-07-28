from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"

with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    read = csv.reader(file)
    
    for line in read:
        print(line)

