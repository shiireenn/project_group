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
    with file_path.open(mode = 'r', encoding = 'UTF-8') as file:
        reader = csv.reader(file)
        previous_day = 0
        value_difference = 0
        next(reader)
        

        

