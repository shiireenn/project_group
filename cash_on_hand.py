from pathlib import Path
import csv
import re
#flag day 43,45,46,48 & 49

file_path = Path.cwd()/"csv_reports"/"cash_on_hand.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"


def cash_on_hand_function(forex):
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline='') as file:
        

        

