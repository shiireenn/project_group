# Import Path from pathlib
from pathlib import Path
# Import re
import re

# Instantiate file_path to csv_reports folder, Profit and loss.csv file
file_path = Path.cwd()/"csv_reports"/"Profits and Loss.csv"
# Instantiate summary_path to summary_report.txt file
summary_path = Path.cwd()/"summary_report.txt"

# Create a function named profitloss_function
def profitloss_function(forex):
    """
    - This function will check for the net profit of each day
    - This function will return "PROFIT DEFICIT" if the net profit of the day after is lower than the day before
    - This function will find the difference in the net profit and exchange it from USD to SGD
    - This function will return "PROFIT SURPLUS" if the net profit of each day is consecutively higher
    """
    # Open file_path and read file
    with file_path.open(mode = "r", encoding = "UTF-8", newline= "") as file:
        
        # Skip headers in file_path
        next(file)
        # Value of previous_day and difference will be 0
        previous_day = 0
        difference = 0
        
        # Use a for loop to iterate through the file
        for line in file.readlines():
            
            # Use re.findall to find patterns with only numbers
            line = re.findall(pattern = r"[0-9][0-9]+", string = line)
            # Use minus to find the net profit difference between the current day and the previous_day
            difference = float(line[4]) - previous_day
            # Find previous_day net profit
            previous_day = float(line[4])
            
            # Use if to only execute the code when the difference is less than 0
            if difference < 0:
                
                # Use abs() to change the difference into a positive number, and then multiply it by forex
                difference = round(abs(difference) * forex, 1)
                
                # Open summary_path and append
                with summary_path.open(mode = "a", encoding="UTF-8", newline = "") as file:
                    # Use .writelines() to write the data into summary_path
                    file.writelines("\n[PROFIT DEFICIT] "+"DAY: "+str(round(float(line[0]),1))+", AMOUNT: SGD"+str(difference))

            # Use elif to only execute the code the difference is 0 or more
            elif difference == 0:
                # Open summary_path and append
                with summary_path.open(mode = "a", encoding="UTF-8", newline = "") as file:
                    # Use .writelines() to write the data into summary_path
                    file.writelines("\n[PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")        
        
        # Close both files
        file.close()
