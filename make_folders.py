import os, calendar
from datetime import datetime, timedelta

def make_dir(first_date):
    first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
    year = first_date.year
    last_date=datetime(year,12,31).date()
    total=(last_date-first_date).days
    try:
        for i in range(total):
            first_date+=timedelta(days=1)
            os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{first_date}")
            folder_path = os.path.join("C:/Users/beerva.joshi/PycharmProjects/Date_folders", str(first_date))
            total_day = calendar.monthrange(first_date.year, first_date.month)[1]
            # print(last_day)
            reversed_day = total_day - first_date.day + 1
            reversed_date = f"{reversed_day}-{first_date.month}-{first_date.year}"
            extensions = ["txt", "py", "json", "html"]

            for ext in extensions:
                file_path = os.path.join(folder_path, f"{reversed_date}.{ext}")
                with open(file_path, "w") as f:
                    f.write(f"This is {reversed_date}.{ext}")

        print("folders formed sucessfully")
    except FileExistsError:
        print("Folders already exist")


start_date_input=input("Enter starting date in yyyy-mm-dd format:")
make_dir(start_date_input)