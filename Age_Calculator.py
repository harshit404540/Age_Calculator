from datetime import date

try:
    today = date.today()
    resolved_date = str(today).split("-")

    user_year = int(input("Enter Year: "))
    user_month = int(input("Enter Month: "))
    user_date = int(input("Enter Date: "))

    current_year = resolved_date[0]
    current_month = resolved_date[1]
    current_date = resolved_date[2]

    if  int(user_year) > int(current_year):
        print("Wrong Year")
    else:
        year = int(current_year)-int(user_year)
    if   int(user_month) > int(current_month):
        month = int(user_month)-int(current_month)
    else:
        month = int(current_month)-int(user_month)
    if    int(user_date) > int(current_date):
        day = int(user_date)-int(current_date)
    else:
        day = int(current_date)-int(user_date)


    print(f"Your Age is: {year}yrs {month}months {day}days")

except Exception as e:
    print(str(e))