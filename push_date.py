import datetime
import time

from pathlib import Path

from Change_Sheet_Name import change_sheet_name
from Delete_file_when_done import delete
from Get_Niid_Spool import get_niid_spool
from Push_to_Niid import Push_to_Niid
from write_last_date import write_last_push_date

# Get the current date
current_date = datetime.date.today()
date_to_string = [str(current_date).split("-")]

current_Year = int(date_to_string[0][0])
# Setting current month to june beacuse of the update made at A&G
# Policy push will start from June 2024
# This will be changed later on
current_Month = int(date_to_string[0][1])
# current_Month = 7 # June
current_Day = int(date_to_string[0][2])

month = 0
addList = 0

months = 1
start = 1
end = 5


def run(push_start_date, push_end_date, SHOW_WINDOW, LINK):
    print(push_start_date)
    print(current_Month)
    Month30 = [4, 6, 9, 11]

    # Checking if the user wants to continue push and values were passes in to the run function
    if push_start_date == "" and push_end_date == "":
        Start_Date = [1, current_Month, current_Year]
        End_Date = [5, current_Month, current_Year]

        if current_Month == 12:
            Start_Date = [1, 1, current_Year + 1]
            End_Date = [5, 1, current_Year + 1]
        else:
            if current_Day <= 5:
                Start_Date = [1, 6, current_Year]
                End_Date = [5, 6, current_Year]
            elif 6 <= current_Day <= 10:
                Start_Date = [6, 6, current_Year]
                End_Date = [10, 6, current_Year]
            elif 11 <= current_Day <= 15:
                Start_Date = [11, 6, current_Year]
                End_Date = [15, 6, current_Year]
            elif 16 <= current_Day <= 20:
                Start_Date = [16, 6, current_Year]
                End_Date = [20, 6, current_Year]
            elif 21 <= current_Day <= 25:
                Start_Date = [21, 6, current_Year]
                End_Date = [25, 6, current_Year]
            elif current_Day >= 26:
                if current_Month == 2:
                    if int(current_Year) % 4 == 0:
                        End_Date = [29, 2, current_Year]
                    else:
                        End_Date = [28, 2, current_Year]
                elif current_Month in Month30:
                    End_Date = [30, current_Month, current_Year]
                else:
                    End_Date = [31, current_Month, current_Year]
    else:
        Start_Date = push_start_date
        End_Date = push_end_date
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
    global errmessage
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

    # running the functions
    try:
        # Deleting the NIIID File If it exists
        delete()
        errmessage = get_niid_spool(Formted_Sdate,Formted_Edate,SHOW_WINDOW,LINK)
        print(f"Error message from the function {errmessage}")
        if errmessage:
            print(errmessage)
            yield [Formted_Sdate, Formted_Edate, errmessage, S_date, E_date]
        else:
            print("Executing next task")
            print(errmessage)
            print("changing sheet name")
            change_sheet_name()
            print("gotten Data")
            errmessage = Push_to_Niid(SHOW_WINDOW)
            yield [Formted_Sdate, Formted_Edate, errmessage, S_date, E_date]
            write_last_push_date(S_date, E_date)
            delete()
    except Exception as e:
        delete()
        write_last_push_date(S_date, E_date)
        print(f" this is  the error {e}")
        time.sleep(3)
        # return errmessage

    #
    # try:
    #     errmessage = Push_to_Niid(SHOW_WINDOW)
    # except Exception as e:
    #     delete()
    #     print(e)
    #     time.sleep(3)
    #     return errmessage,

    # delete()
    # errmessage = "hi"


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
