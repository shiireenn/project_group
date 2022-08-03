import api
from pathlib import Path
import csv
import re

file_path = Path.cwd()/"csv_reports"/"profit_loss.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
forex = api.api_function

def profitloss_function(forex):
    with file_path.open(mode = "r", encoding = "UTF-8") as file:
        next(file)
        previous_day = 0
        difference = 0
        for line in file.readlines():
            line = re.findall(pattern = r"[0-9][0-9]+", string = line)
            previous_day = float(line[4])
            difference = float(line[4]) - previous_day
            if difference < 0:
                difference = round(abs(difference)) * forex
                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
                    file.writelines("[PROFIT DEFICIT] "+"DAY: "+ str(round(float(line[0],1)))+", AMOUNT: SGD" + str(difference))
        file.close()
#            else:
#                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
#                    file.writelines("\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")

print(profitloss_function(forex))