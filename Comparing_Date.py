
def comparing_date(startDate,endDate):
    # startDate = "01-03-2023"
    # endDate = "01-02-2023"


    start_list = []
    end_list = []
    # Appending the neww arrray by each character in the start and end date
    for char in startDate:
        start_list.append(char)
    for char in endDate:
        end_list.append(char)

    # print(start_list)
    # print(end_list)

    index1_to_remove = 2
    index2_to_remove = 4
    # deleting the "-" in the array
    del start_list[index1_to_remove]
    del start_list[index2_to_remove]

    del end_list[index1_to_remove]
    del end_list[index2_to_remove]

    # print(start_list)
    # print(end_list)

    # New converted date list
    converted_start_list = []
    converted_end_list = []

    # Converting the values in the arry to int
    for char in start_list:
        converted_start_list.append(int(char))

    for char in end_list:
        converted_end_list.append(int(char))

    # Joining the values in the index 4-7 in th array
    Start_Year = start_list[4] + start_list[5] + start_list[6] + start_list[7]
    # print(int(Start_Year))
    End_Year = end_list[4] + end_list[5] + end_list[6] + end_list[7]
    # print(int(End_Year))

    # Checking if the value in the index of 2 in the list is == 0 and deleting it if its true
    if start_list[2] == '0' or end_list[2] == '0':
        Start_Month = start_list[3]
        End_Month = end_list[3]
    else:
        Start_Month = start_list[2] + start_list[3]
        End_Month = end_list[2] + end_list[3]

    # print(Start_Month)
    # print(End_Month)

    # Checking if the date format is correct
    if End_Year < Start_Year or End_Month < Start_Month:
        Error_Message = "From Date cannot be greater than To Date."
    else:
        Error_Message =""

        print(Error_Message)

    # print(converted_start_list)
    # print(converted_end_list)
    return Error_Message