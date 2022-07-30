#theo
#import Path function from pathlib
from pathlib import Path
#import csv module
import csv

file_path = Path.cwd()/"csv_reports"/"overheads.csv"

#create empty list
empty_list = []

#create 'reader' pbject and print line if file path exists
with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    #instantiate a read object
    reader = csv.reader(file)
    #use 'next()' to skip Header
    next(reader)

# Create nested loop to access each value in the list
# and append the value to the empty_list.
# Header is skipped due to `next()` before for loop
    for line in reader:
        for value in line:
            empty_list.append(value)
            
            #check value in empty_list
            print (empty_list)