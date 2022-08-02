#theo
#import Path function from pathlib
from pathlib import Path
#import csv module
import csv

file_path = Path.cwd()/"csv_reports"/"overheads.csv"
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"

#create a function 'overheads_category' that returns the highest category of overheads
def overheads_function():
    """
    This function returns the category with the highest overheads in percentage.
    """

#create and assign an empty list to 'percentage'
percentage = []
overheads = {}

#create 'reader' object and print line if file path exists
with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    #instantiate a read object
    reader = csv.reader(file)
    #use 'next()' to skip Header
    #next(reader)

# Create nested loop to access each value in the list
# and append the value to the empty_list.
# Header is skipped due to `next()` before for loop
    for line in reader:
        data = float(file[1])
        category = data[0]
        percentage.append[data]
        highest = max(data)
        highest_category = max{category}
        f"([HIGHEST_OVERHEADS] {highest_category.upper()} = {highest} %"
return message

print(overheads_function())
