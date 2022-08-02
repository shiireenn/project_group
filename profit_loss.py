from pathlib import Path
import csv
import re

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"

def profit_loss_function(forex):
    with file_path.open(mode = "r", encoding = "UTF-8") as file:
        next(file)
        previous_day = 0
        difference = 0
        for line in file.readlines():
            line = re.findall(pattern = r"[0-9][0-9]+", string = line)
            difference = line[4] - previous_day
            if difference < 0:
                difference = abs(difference)*forex
                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    file.writelines("[PROFIT DEFICIT] "+"DAY: "+line[0]", AMOUNT: SGD"+difference)
        file.close()

