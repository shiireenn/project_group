from pathlib import Path
import api, cash_on_hand, overheads, profit_loss
import csv
import json,re
import requests

path = Path.cwd()
# Set current working directory to csv_reports
cwd_path = Path.cwd()/"csv_reports"
# Current working directory of summary_report.txt will be csv_report
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
# Touch summary_path to csv_reports
summary_path.touch()


cwd_path = Path.cwd()/"PROJECT_GROUP"
# # cwd_path.exists()
summary_path = Path.cwd()/"PROJECT_GROUP"/"csv_reports"/"summary_report.txt"
# # #creating csv file using .touch() method
summary_path.exists()
# summary_path.touch()



# def main():

#     forex = api.api_function()
#     overheads.overheads_function(forex)
#     cash_on_hand.cash_on_hand(forex)
#     profit_loss.profitloss_function(forex)

# #    with summary_path.open(mode = "w", encoding = "UTF-8", newline = ""):

# main()
