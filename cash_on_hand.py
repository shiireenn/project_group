from pathlib import Path
import csv
import re
#flag day 43,45,46,48 & 49

file_path = Path.cwd()/"csv_reports"/"cash_on_hand.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"


def cash_on_hand_function(forex):
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline='') as file:
    '''
    This function highlights the days where cash on hand was lower than the previous day and also shows the value difference
    '''
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline = '') as file:
        next(file)
        previous_day = 0
        value_difference = 0
        for line in file.readlines():
            line = re.findall(pattern=r'[0-9][0-9]+', string=line)
            value_difference = float(line[1]) - previous_day
            previous_day = float(line[1])
            if value_difference < 0:
                value_difference = round(abs(value_difference)*forex)
                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "" ) as file:
                    file.writelines("\n[CASH DEFICIT]"+"DAY: "+str(round(float(line[0]),1))+", AMOUNT: SGD"+str(value_difference))
        file.close()

        

        

