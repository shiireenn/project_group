from pathlib import Path
import api, cash_on_hand, overheads, profit_loss
import csv
import json,re
import requests

# Set current working directory to csv_reports
cwd_path = Path.cwd()/"csv_reports"
# Current working directory of summary_report.txt will be csv_report
summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"
# Touch summary_path to csv_reports
summary_path.touch()

def main():
    forex = api.api_function()
    overheads.overheads_function(forex)
    cash_on_hand.cash_on_hand(forex)
    profit_loss.profitloss_function(forex)


