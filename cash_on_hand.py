from pathlib import Path
import csv
#flag day 43,45,46,48 & 49
full_list = []
def cash_on_hand_function():
    with open(r"./csv_reports/cash_on_hand.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            full_list.append(line)
        previous_day = 0
        value_difference = 0