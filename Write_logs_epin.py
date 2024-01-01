import os
import datetime
from pathlib import Path

def write_logs_epin(PUSH_START_DATE,PUSH_END_DATE,PUSH_MESSAGE):

    # Creating the LOGS Folder if it does not exist
    Log_folder_name = "LOGS"
    if Path(Log_folder_name).is_dir():
        print("")
    else:
        os.makedirs(Log_folder_name)

        # Geting the date and time
    current_datetime = datetime.datetime.now()
    # Formatting the Date and Time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d")
    Date_and_Time = str(formatted_datetime)


    # passing the info to that was passed in from the function to PUSH_INFO
    PUSH_INFO = [f"Pushed from {PUSH_START_DATE} - {PUSH_END_DATE} \n",f"{PUSH_MESSAGE}"]

    # Creating the Automatic log folder if it does not exist
    folder_name = f"E_PIN_Automatic_Push_logs___{Date_and_Time}"
    folder_path = "./LOGS/" + folder_name

    if Path(folder_path).is_dir():
        print("")
    else:
        os.makedirs(folder_path)
    logs_path = f"./LOGS/E_PIN_Automatic_Push_logs___{Date_and_Time}"
    log_file = f"{PUSH_START_DATE} - {PUSH_END_DATE}.txt"
    log_file_path = logs_path + "/" + log_file

    #Writing files
    with open(log_file_path, "w") as logs:
        logs.write(f"Policy Details{PUSH_INFO[0]}\n")
        logs.write(f"Policy Details{PUSH_INFO[1]}\n")
        logs.write(f"Date Modified {current_datetime}\n\n\n")














