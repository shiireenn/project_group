#theo
#import Path function from pathlib
from pathlib import Path
#import csv module
import csv

file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
#current working directory of summary_report.txt will be csv_report
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"

#create a function 'overheads_category' that returns the highest category of overheads
def overheads_function(forex):
    """
    This function returns the category with the highest overheads in percentage.
    """
    if file_path.exists():
        with file_path.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as files:
            reader = csv.reader(files)
            overheads = {}
            next(reader)
            for category in reader:
                overheads[category[0]] = float(category[1]) * forex
    highest_value = 0
    for key in overheads:
        if overheads[key] > highest_value:
            highest_value = overheads[key]
    for key, value in overheads.items():
        if value == highest_value:
            if summary_path.exists():
                with summary_path.open(mode = 'a', encoding = "UTF-8", errors = 'ignore') as file:
                    message = file.write(f'\n[HIGHEST OVERHEADS] {key.upper()}: SGD{value:.2f}')
                return message    
