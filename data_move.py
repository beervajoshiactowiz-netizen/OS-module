import os,calendar
from datetime import datetime, timedelta

def make_dir(first_date):
    first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
    year_c = first_date.year
    last_date=datetime(year_c,12,31).date()
    total=(last_date-first_date).days
    try:
        for i in range(total):
            first_date+=timedelta(days=1)
            os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/Date_folders/{first_date}")
            folder_path = os.path.join("C:/Users/beerva.joshi/PycharmProjects/Date_folders", str(first_date))
            total_day = calendar.monthrange(first_date.year, first_date.month)[1]
            # print(last_day)
            reversed_day = total_day - first_date.day + 1
            reversed_date = f"{first_date.year}-{first_date.month}-{reversed_day}"
            extensions = ["txt", "py", "json", "html"]

            for ext in extensions:
                file_path = os.path.join(folder_path, f"{reversed_date}.{ext}")
                with open(file_path, "w") as f:
                    f.write(f"This is {reversed_date}.{ext}")

        print("folders formed sucessfully")
    except FileExistsError:
        print("Folders already exist")

def next_year(input_date):
    input_date = datetime.strptime(input_date, "%Y-%m-%d").date()
    year_n=input_date.year+1
    month=input_date.month
    day=input_date.day
    next_year_date=datetime(year_n,month,day).date()
    last_date = datetime(year_n, 12, 31).date()
    total = (last_date - next_year_date).days
    try:
        for i in range(total):
            next_year_date+=timedelta(days=1)
            os.mkdir(f"C:/Users/beerva.joshi/PycharmProjects/data_copy/{next_year_date}")
        print("next year folder formed")
    except FileExistsError:
        print("Folders already exist")


def move_file(source_path,destination_path):
    for i in os.listdir(source_path):
        source_folder=os.path.join(source_path,i)
        year_change=i.replace("2026","2027")
        dest_folder=os.path.join(destination_path,year_change)
        for j in os.listdir(source_folder):
            source_file=os.path.join(source_folder,j)
            dest_file=os.path.join(dest_folder,j)
            os.rename(source_file,dest_file)

def remove_file(destination_):
    for i in os.listdir(destination_):
        folder=os.path.join(destination_,i)
        for j in os.listdir(folder):
            file=os.path.join(folder,j)

            if file.endswith(".py") or file.endswith((".json")):
                os.remove(file)


source="C:/Users/beerva.joshi/PycharmProjects/Date_folders"
destination="C:/Users/beerva.joshi/PycharmProjects/data_copy"
start_date_input=input("Enter starting date in yyyy-mm-dd format:")
# copy_folder_date=input("enter date from which we have to move: ")
make_dir(start_date_input)
next_year(start_date_input)
move_file(source,destination)
remove_file(destination)