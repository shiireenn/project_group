# Import path
from pathlib import Path
# Import api.py,overheads.py, cash_on_hand.py and profit_loss.py
import api, overheads, cash_on_hand, profit_loss

# Instantiate summary_path to summary_report.txt
summary_path = Path.cwd()/"summary_report.txt"
# Use .touch() to create summary_report.txt project_group
summary_path.touch()

# Create a function named main
def main():
    """
    - This function will import api_function(), overheads_function(forex), cash_on_hand_function(forex) and profitloss_function(forex)
    - This function will write all the data into a summary report
    """
    # Use variable forex for api.api_function()
    forex = api.api_function()
    # overheads_function(forex) from overheads.py
    overheads.overheads_function(forex)
    # cash_on_hand_function(forex) from cash_on_hand.py
    cash_on_hand.cash_on_hand_function(forex)
    # profitloss_function(forex) from profit_loss.py
    profit_loss.profitloss_function(forex)

# Calling main() function
main()


        

