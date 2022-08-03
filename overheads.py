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



    #create and assign an empty list to 'percentage'
    #percentage = []
   #overheads = {}

    #create 'reader' object and print line if file path exists
    #with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    #instantiate a read object
        #reader = csv.reader(file)
    #use 'next()' to skip Header
    #next(reader)

    # Create nested loop to access each value in the list
    # and append the value to 'percentage'.
    # Header is skipped due to `next()` before for loop
        #for line in reader:
            #data = float(line)
            #category = line[0]
            #percentage.append()
            #highest = max(data)
            #highest_category = category
            #message = f"([HIGHEST_OVERHEADS]) {highest_category.upper()} = {highest} %"
            #return message

#print(overheads_function())
