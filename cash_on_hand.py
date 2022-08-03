#import path method from pathlib
from pathlib import Path
#import csv module
import csv
#import module for regex
import re

#instantiate file path object to Cash_on_Hand.csv file under csv_reports folder 
file_path = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
#instantiate file patch object to summary_report.txt file under csv_reports folder
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"

#creating a function called cash_on_hand_function
def cash_on_hand_function(forex):
   """
   -This function highlights the days where cash on hand was lower than the previous day and also shows the value difference as a deficit
   """
   #open file and read the file
   #newline parameter prevents extra line in csv file
   #file is a variable assigned to file after opening and reading
   with file_path.open(mode = 'r', encoding = 'UTF-8', newline = '') as file:
        #to skip the header
        next(file)
        #assigning value of 0 to previous_day and value_difference
        previous_day = 0
        value_difference = 0
        #created nested loop to access all values in the file
        for line in file.readlines():
            line = re.findall(pattern=r'[0-9][0-9]+', string=line)
            #subtract values from the current day with previous day to find the difference of cash in hand 
            value_difference = float(line[1]) - previous_day
            #cash on hand for previous day
            previous_day = float(line[1])
            #if statement runs code when difference is a negative value
            if value_difference < 0:
                #used abs() to always return a positive number
                #value_difference is multiplied by the forex for current price  
                value_difference = round(abs(value_difference)*forex)
                #to open summary_path and append data to file
                with summary_path.open(mode = "a", encoding = "UTF-8", newline = "" ) as file:
                    #writelines() to write data into summary_path
                    file.writelines("\n[CASH DEFICIT]"+"DAY: "+str(round(float(line[0]),1))+", AMOUNT: SGD"+str(value_difference))
        #close files
        file.close()

        

        

