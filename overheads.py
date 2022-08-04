# Import Path function from pathlib
from pathlib import Path
# Import csv module
import csv

# Instantiate file_path to csv_reports folder, Overheads csv file
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"
# Instantiate summary_path to summary_report.txt file
summary_path = Path.cwd()/"summary_report.txt"

#create a function 'overheads_function(forex)' that returns the highest overheads after the foreign exchange rate.
def overheads_function(forex):
    """
    This function returns the category and highest overheads after the foreign exchange rate.
# Create a function named overheads_fucntion
def overheads_function(forex):
    """
    - This function returns the category with the highest overheads in percentage terms
    - This function will convert the highest overheads from USD to SGD
    """
    # Check if file_path exists
    if file_path.exists():

        # Open file_path
        with file_path.open(mode = 'r', encoding = 'UTF-8', errors = 'ignore') as files:
            
            # Use .reader() to read the file
            reader = csv.reader(files)
            # Set overheads as dictionary
            overheads = {}
            # Use next to skip the headers
            next(reader)

            # Use for loop to iterate through reader
            for category in reader:
                
                # Convert the overhead from USD to SGD
                overheads[category[0]] = float(category[1]) * forex

    # Value of highest_value will be 0            
    highest_value = 0

    # Use for loop to iterathe through overheads
    for key in overheads:

        # Use if to only execute the code when highest_value is less than overheads[key]
        if overheads[key] > highest_value:

            # Use varibale highest_value
            highest_value = overheads[key]

    # Use for loop to iterate through key and value        
    for key, value in overheads.items():

        # Use if to only execute the code when value equals to highest_value
        if value == highest_value:

            # Check if summary_path exists
            if summary_path.exists():

                # Open summary_path and append
                with summary_path.open(mode = 'a', encoding = "UTF-8", errors = 'ignore') as file:
                    
                    # Use .write() to write into summary_path
                    message = file.write(f'\n[HIGHEST OVERHEADS] {key.upper()}: SGD{value:.2f}')
                
                # Return the data in message
                return message    
