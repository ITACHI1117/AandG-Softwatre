import datetime
import os
import time

from Delete_file_when_done import delete
from Error_messges import openNewWindow
from Get_Niid_Spool import get_niid_spool
from Push_to_Niid import Push_to_Niid
from Change_Sheet_Name import change_sheet_name


from pathlib import Path

# Get the current date
current_date = datetime.date.today()
date_to_string = [str(current_date).split("-")]

current_Year = date_to_string[0][0]
current_Month = int(date_to_string[0][1])
current_Day = int(date_to_string[0][2])


# Print the current date in the default format (YYYY-MM-DD)


#
# Start_date = ""
# End_date = ""
#
# Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#
# Days = ""
# for Month in Months:
#     if Month == "Apr" or Month == "Jun" or Month == "Sep" or Month == "Nov":
#         Days = 30
#     elif int(current_Year) % 4 == 0 and Month == "Feb":
#         Days = 28
#     elif int(current_Year) % 4 != 0 and Month == "Feb":
#         Days = 29
#     else:
#         Days = 31
#
#     calendar = [[Month],[Days]]
#     print(calendar[1][0])
#
#     i = 0
#     start = 0
#     end = 5
#
#     print(f"{start + 1}-{end}")
#     while i <= calendar[1][0] - 1:
#         if i == 0:
#             pass
#         start += 5
#         end += 5
#         if end >= calendar[1][0]:
#             break
#         print(calendar[0][0])
#         print(f"{start}-{end}")
#
#     print(f"{Months[0]} has  {i}")
#
#
#
# # def passing_date():
# #     i = 0
# #     start = 0
# #     end = 5
# #
# #     print(f"{start + 1}-{end}")
# #     while i <= 31 - 1:
# #         if i == 0:
# #             pass
# #         start += 5
# #         end += 5
# #         if end >= 31:
# #             break
# #         print(f"{start}-{end}")
# #
# #     print(f"{Months[0]} has  {i}")


month = 0
Start_Date = [21, 7, current_Year]
End_Date = [25,7,current_Year]

addList = 0

months = 1
start = 1
end = 5
def run():
    Pussing_Dates = date_formater(Start_Date, End_Date)
    passed = ""
    for Pushing_Date in Pussing_Dates:
        passed = Pushing_Date
    yield passed
    while (Start_Date[1] != current_Month or End_Date[0] <
           current_Day):
        Start_Date[0] += 5
        End_Date[0] += 5

        if End_Date[0] == 30 and End_Date[1] == 2 and int(current_Year)%4 !=0:
            End_Date[0] = 28
        if End_Date[0] == 30 and End_Date[1] == 2 and int(current_Year)%4 ==0:
            End_Date[0] = 29
        if Start_Date[0] == 26 and  Start_Date[1] == 1:
            End_Date[0] = 31
        if Start_Date[0] == 26 and  Start_Date[1] == 3:
            End_Date[0] = 31
        if Start_Date[0] == 26 and  Start_Date[1] ==5:
            End_Date[0] = 31
        if Start_Date[0] == 26 and  Start_Date[1] == 7:
            End_Date[0] = 31
        if Start_Date[0] == 26 and  Start_Date[1] == 8 :
            End_Date[0] = 31
        if Start_Date[0] == 26 and  Start_Date[1] == 10 :
            End_Date[0] = 31
        if Start_Date[0] == 26 and  Start_Date[1] == 12 :
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
        if  End_Date[0] <= current_Day and Start_Date[1] == current_Month and current_Day %5 !=0:
            End_Date[0] = current_Day
        if Start_Date[0] == 31:
            Start_Date[1] += 1
            End_Date[1] += 1
            Start_Date[0] =1
            End_Date[0] =5

        # print(f"start {Start_Date}")
        # print(f"end {End_Date}")
        Pussing_Dates =date_formater(Start_Date,End_Date)
        passed = ""
        for Pushing_Date in Pussing_Dates:
            passed = Pushing_Date
        yield passed



def date_formater(S_date,E_date):
    downloads_path = Path.home() / "Downloads"
    file_path = f"{downloads_path}/NIID Spool.xlsx"

    new_value = ""
    if  S_date[1] == 1:
        new_value = "Jan"
    if  S_date[1] == 2:
        new_value = "Feb"
    if  S_date[1] == 3:
        new_value = "Mar"
    if S_date[1] == 4:
        new_value = "Apr"
    if  S_date[1] == 5:
        new_value = "May"
    if  S_date[1] == 6:
        new_value = "Jun"
    if S_date[1] == 7:
        new_value = "Jul"
    if S_date[1] == 8:
        new_value = "Aug"
    if  S_date[1] == 9:
        new_value = "Sep"
    if  S_date[1] == 10:
        new_value = "Oct"
    if  S_date[1] == 11:
        new_value = "Nov"
    if S_date[1] == 12:
        new_value = "Dec"

    S_date[1] = new_value
    E_date[1] = new_value




    Formted_Sdate = "-".join(map(str,S_date))
    Formted_Edate = "-".join(map(str, E_date))

    try:

        get_niid_spool(Formted_Sdate,Formted_Edate)
        change_sheet_name()
    except Exception as e:
        if e:
            print(e)

            time.sleep(3)

            return

    print("gotten Data")
    try:
        errmessage = Push_to_Niid()
    except Exception as e:
        if e:
            print(e)
            time.sleep(3)
            return errmessage

    delete()


    yield [Formted_Sdate, Formted_Edate,errmessage]
    time.sleep(5)





    if  S_date[1] == "Jan":
        new_value = 1
    if  S_date[1] == "Feb":
        new_value = 2
    if  S_date[1] == "Mar":
        new_value = 3
    if S_date[1] == "Apr":
        new_value = 4
    if  S_date[1] == "May":
        new_value = 5
    if  S_date[1] == "Jun":
        new_value = 6
    if S_date[1] == "Jul":
        new_value = 7
    if S_date[1] == "Aug":
        new_value = 8
    if  S_date[1] == "Sep":
        new_value = 9
    if  S_date[1] == "Oct":
        new_value = 10
    if  S_date[1] == "Nov":
        new_value = 11
    if S_date[1] == "Dec":
        new_value = 12

    S_date[1] = new_value
    E_date[1] = new_value



# num = 31
# i=0
# for i in range(num):
#     if i % 5 == 0:
#         print(i)
#     print(i+1)

