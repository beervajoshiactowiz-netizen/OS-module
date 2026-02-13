import os
from datetime import datetime,timedelta

print("Create folder from first date to last date")

def make_dir(end_date,start_date):

    total_days_from_now=(end_date-start_date).days

    for i in range(total_days_from_now):
        start_date+=timedelta(days=1)
        os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{start_date}")
    print("Folders created successfully")


last_date_input=input("enter last date in yyyy-mm-dd format: ")
last_date=datetime.strptime(last_date_input,"%Y-%m-%d").date()
first_date_input=input("enter starting date in yyyy-mm-dd format: ")
first_date=datetime.strptime(first_date_input,"%Y-%m-%d").date()


make_dir(last_date,first_date)
