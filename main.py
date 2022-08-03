from pathlib import Path
import api, overheads, cash_on_hand, profit_loss


# Set current working directory to csv_reports
cwd_path = Path.cwd()/"csv_reports"
# Current working directory of summary_report.txt will be csv_report
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
# creating summary_report.txt using .touch() from summary_path to csv_reports
summary_path.touch()


def main():
    forex = api.api_function()
    #overheads.overhead_function(forex)
    cash_on_hand.cash_on_hand_function(forex)
    profit_loss.profitloss_function(forex)

main()
            

        

