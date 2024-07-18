import datetime
import time

from pathlib import Path

# Get the current date
current_date = datetime.date.today()
date_to_string = [str(current_date).split("-")]

current_Year = int(date_to_string[0][0])
current_Month = int(date_to_string[0][1])
current_Day = int(date_to_string[0][2])

month = 0
addList = 0

months = 1
start = 1
end = 5


def run(push_start_date, push_end_month, SHOW_WINDOW, LINK):
    Month30 = [4, 6, 9, 11]

    # Checking if the user wants to continue push and values were passes in to the run function
    if push_start_date == "" and push_end_month == "":
        if current_Month == 12:
            Start_Date = [1, 1, current_Year]
            End_Date = [5, 1, current_Year]
        else:
            if current_Day <= 5:
                Start_Date = [current_Day, current_Month, current_Year - 1]
                End_Date = [5, current_Month, current_Year - 1]
            elif 6 <= current_Day <= 10:
                Start_Date = [current_Day, current_Month, current_Year - 1]
                End_Date = [10, current_Month, current_Year - 1]
            elif 11 <= current_Day <= 15:
                Start_Date = [current_Day, current_Month, current_Year - 1]
                End_Date = [15, current_Month, current_Year - 1]
            elif 16 <= current_Day <= 20:
                Start_Date = [current_Day, current_Month, current_Year - 1]
                End_Date = [20, current_Month, current_Year - 1]
            elif 21 <= current_Day <= 25:
                Start_Date = [current_Day, current_Month, current_Year - 1]
                End_Date = [25, current_Month, current_Year - 1]
            elif 26 <= current_Day <= 31 and int(current_Year - 1) % 4 != 0 and current_Month == 2:
                Start_Date = [current_Day, 2, current_Year - 1]
                End_Date = [28, 2, current_Year - 1]
            elif 26 <= current_Day <= 31 and int(current_Year - 1) % 4 == 0 and current_Month == 2:
                Start_Date = [current_Day, 2, current_Year - 1]
                End_Date = [29, 2, current_Year - 1]
            elif 26 <= current_Day <= 31:
                Start_Date = [current_Day, current_Month, current_Year - 1]
                End_Date = [31, current_Month, current_Year - 1]
            if 26 <= current_Day <= 31:
                for i in Month30:
                    if current_Month == i:
                        Start_Date = [current_Day, current_Month, current_Year - 1]
                        End_Date = [30, current_Month, current_Year - 1]

        # Start_Date = [1, current_Month+1, current_Year-1]
        # End_Date = [5, current_Month+1, current_Year-1]
    else:
        Start_Date = push_start_date
        End_Date = push_end_month
        # print(Start_Date[1])
        # print(End_Date)

    # running the function to get the first values
    Pussing_Dates = date_formater(Start_Date, End_Date, SHOW_WINDOW,LINK)

    passed = ""
    for Pushing_Date in Pussing_Dates:
        passed = Pushing_Date
    yield passed
    if current_Day <= 5:
        Start_Date[0] = 1
        End_Date[0] = 5
    elif 6 <= current_Day <= 10:
        Start_Date[0] = 6
        End_Date[0] = 10
    elif 11 <= current_Day <= 15:
        Start_Date[0] = 11
        End_Date[0] = 15
    elif 16 <= current_Day <= 20:
        Start_Date[0] = 16
        End_Date[0] = 20
    elif 21 <= current_Day <= 25:
        Start_Date[0] = 21
        End_Date[0] = 25
    elif 26 <= current_Day <= 31 and int(current_Year - 1) % 4 != 0 and Start_Date[1] == 2:
        Start_Date[0] = -4
        End_Date[0] = 0
        Start_Date[1] += 1
        End_Date[1] += 1
    elif 26 <= current_Day <= 31 and int(current_Year - 1) % 4 != 0 and Start_Date[1] == 2:
        Start_Date[0] = -4
        End_Date[0] = 0
        Start_Date[1] += 1
        End_Date[1] += 1
    elif 26 <= current_Day <= 31:
        Start_Date[0] = -4
        End_Date[0] = 0
        Start_Date[1] += 1
        End_Date[1] += 1

    while (Start_Date[1] != current_Month or End_Date[0] <
           current_Day or End_Date[2] != current_Year):
        Start_Date[0] += 5
        End_Date[0] += 5
        # Formatting the date depending on the specific months
        if End_Date[0] == 30 and End_Date[1] == 2 and int(current_Year) % 4 != 0:
            End_Date[0] = 28
        if End_Date[0] == 30 and End_Date[1] == 2 and int(current_Year) % 4 == 0:
            End_Date[0] = 29
        if Start_Date[0] == 26 and Start_Date[1] == 1:
            End_Date[0] = 31
        if Start_Date[0] == 26 and Start_Date[1] == 3:
            End_Date[0] = 31
        if Start_Date[0] == 26 and Start_Date[1] == 5:
            End_Date[0] = 31
        if Start_Date[0] == 26 and Start_Date[1] == 7:
            End_Date[0] = 31
        if Start_Date[0] == 26 and Start_Date[1] == 8:
            End_Date[0] = 31
        if Start_Date[0] == 26 and Start_Date[1] == 10:
            End_Date[0] = 31
        if Start_Date[0] == 26 and Start_Date[1] == 12:
            End_Date[0] = 31
        # changing end dates for april, jun sep and nov
        if Start_Date[0] == 26 and Start_Date[1] == 4:
            End_Date[0] = 30
        if Start_Date[0] == 26 and Start_Date[1] == 6:
            End_Date[0] = 30
        if Start_Date[0] == 26 and Start_Date[1] == 9:
            End_Date[0] = 30
        if Start_Date[0] == 26 and Start_Date[1] == 11:
            End_Date[0] = 30
        # if End_Date[0] >= current_Day and Start_Date[1] == current_Month and current_Day % 5 != 0:
        #     End_Date[0] = current_Day
        if End_Date[0] >= current_Day and Start_Date[1] == current_Month and Start_Date[2] == current_Year:
            End_Date[0] = current_Day
        if Start_Date[0] == 31 and Start_Date[1] == 12 and Start_Date[2] != current_Year:
            Start_Date[1] = 1
            End_Date[1] = 1
            Start_Date[0] = 1
            End_Date[0] = 5
            Start_Date[2] += 1
            End_Date[2] += 1
        if Start_Date[0] == 31:
            Start_Date[1] += 1
            End_Date[1] += 1
            Start_Date[0] = 1
            End_Date[0] = 5
        # if Start_Date[0] == 31:
        #     Start_Date[1] += 1
        #     End_Date[1] += 1
        #     Start_Date[0] =1
        #     End_Date[0] =5
        #     Start_Date[1] =1
        #     End_Date[1] =1

        # print(f"start {Start_Date}")
        # print(f"end {End_Date[0]}")
        # Geting the data from the date formatte
        Pussing_Dates = date_formater(Start_Date, End_Date, SHOW_WINDOW,LINK)
        passed = ""
        for Pushing_Date in Pussing_Dates:
            passed = Pushing_Date
        yield passed


# This function formats the date and runs the push functions
def date_formater(S_date, E_date, SHOW_WINDOW, LINK):
    downloads_path = Path.home() / "Downloads"
    file_path = f"{downloads_path}/NIID Spool.xlsx"

    new_value = ""
    # Formating the date
    if S_date[1] == 1 or S_date[1] == "Jan":
        new_value = "Jan"
    if S_date[1] == 2 or S_date[1] == "Feb":
        new_value = "Feb"
    if S_date[1] == 3 or S_date[1] == "Mar":
        new_value = "Mar"
    if S_date[1] == 4 or S_date[1] == "Apr":
        new_value = "Apr"
    if S_date[1] == 5 or S_date[1] == "May":
        new_value = "May"
    if S_date[1] == 6 or S_date[1] == "Jun":
        new_value = "Jun"
    if S_date[1] == 7 or S_date[1] == "Jul":
        new_value = "Jul"
    if S_date[1] == 8 or S_date[1] == "Aug":
        new_value = "Aug"
    if S_date[1] == 9 or S_date[1] == "Sep":
        new_value = "Sep"
    if S_date[1] == 10 or S_date[1] == "Oct":
        new_value = "Oct"
    if S_date[1] == 11 or S_date[1] == "Nov":
        new_value = "Nov"
    if S_date[1] == 12 or S_date[1] == "Dec":
        new_value = "Dec"

    S_date[1] = new_value
    E_date[1] = new_value

    Formted_Sdate = "-".join(map(str, S_date))
    Formted_Edate = "-".join(map(str, E_date))

    print(Formted_Sdate)
    print(Formted_Edate)

    time.sleep(0.4)

    #running the functions
    # try:
    #     get_niid_spool(Formted_Sdate,Formted_Edate,SHOW_WINDOW,LINK)
    #     change_sheet_name()
    # except Exception as e:
    #     delete()
    #     print(e)
    #     time.sleep(3)
    #     return
    #
    # print("gotten Data")
    # try:
    #     errmessage = Push_to_Niid(SHOW_WINDOW)
    # except Exception as e:
    #     delete()
    #     print(e)
    #     time.sleep(3)
    #     return errmessage
    #
    # delete()

    errmessage = "hi"

    yield [Formted_Sdate, Formted_Edate, errmessage, S_date, E_date]


    # Reformating the date so the run function can undersand the date format
    if S_date[1] == "Jan":
        new_value = 1
    if S_date[1] == "Feb":
        new_value = 2
    if S_date[1] == "Mar":
        new_value = 3
    if S_date[1] == "Apr":
        new_value = 4
    if S_date[1] == "May":
        new_value = 5
    if S_date[1] == "Jun":
        new_value = 6
    if S_date[1] == "Jul":
        new_value = 7
    if S_date[1] == "Aug":
        new_value = 8
    if S_date[1] == "Sep":
        new_value = 9
    if S_date[1] == "Oct":
        new_value = 10
    if S_date[1] == "Nov":
        new_value = 11
    if S_date[1] == "Dec":
        new_value = 12

    S_date[1] = new_value
    E_date[1] = new_value

    print(S_date)
    print(E_date)

    print(Formted_Sdate)
    print(Formted_Edate)

    # storing the data so it can be passed when the function is called
