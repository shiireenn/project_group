import api
from pathlib import Path
import csv
import re

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
forex = api.api_function()

def profitloss_function(forex):
    with file_path.open(mode = "r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        previous_day = 0
        difference = 0
        for line in file:
            line = re.findall(pattern = r"[0-9][0-9]+", string = line)
            previous_day = float(line[4])
            difference = float(line[4]) - previous_day
            if difference < 0:
                difference = abs(difference) * forex
                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    file.writelines("\n[PROFIT DEFICIT] "+"DAY: "+line[0]+", AMOUNT: SGD "+difference)
            else:
                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    file.writelines("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")

