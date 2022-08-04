# Import path method from pathlib
from pathlib import Path
# Import csv module
import csv
# Import module for regex
import re

# Instantiate file path object to Cash_on_Hand.csv file under csv_reports folder 
file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
# Instantiate file patch object to summary_report.txt 
summary_path = Path.cwd()/"summary_report.txt"

# Creating a function called cash_on_hand_function
def cash_on_hand_function(forex):
   """
   - This function highlights the days where cash on hand was lower than the previous day and also shows the value difference as a deficit
   """
   # Open file and read the file
   # Newline parameter prevents extra line in csv file
   # File is a variable assigned to file after opening and reading
   with file_path.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        
        # To skip the header
        next(file)
        # Assigning value of 0 to previous_day and value_difference
        previous_day = 0
        value_difference = 0
        
        # Created nested loop to access all values in the file
        for line in file.readlines():
            
            line = re.findall(pattern = r"[0-9][0-9]+", string = line)
            # Subtract values from the current day with previous day to find the difference of cash in hand 
            value_difference = float(line[1]) - previous_day
            # Cash on hand for previous day
            previous_day = float(line[1])
            # If statement runs code when difference is a negative value
            
            if value_difference < 0:
                
                # Used abs() to always return a positive number
                # Value_difference is multiplied by the forex for current price  
                value_difference = round(abs(value_difference) * forex, 1)
                
                # To open summary_path and append data to file
                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "" ) as file:
                    
                    # .writelines() to write data into summary_path
                    file.writelines("\n[CASH DEFICIT]"+" DAY: "+str(round(float(line[0]),1))+", AMOUNT: SGD"+str(value_difference))
        

            # Use elif to only execute the code the difference is 0 or more
            elif value_difference == 0:
                # Open summary_path and append
                with summary_path.open(mode = "a", encoding="UTF-8", newline = "") as file:
                    # Use .writelines() to write the data into summary_path
                    file.writelines("\n[CASH SURPLUS] CASH ON HAND ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")   
        
        # Close files
        file.close()

        

        

