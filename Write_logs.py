import os
import datetime
from pathlib import Path

def write_logs(PUSH_START_DATE,PUSH_END_DATE,PUSH_MESSAGE):

    # Checking what type of update the user wants to make

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



    PUSH_INFO = [f"Pushed from {PUSH_START_DATE} - {PUSH_END_DATE} \n",f"{PUSH_MESSAGE}"]

    # Creating the RegCorrection log folder if it does not exist
    folder_name = "Automatic_Push_logs"
    folder_path = "./LOGS/" + folder_name

    if Path(folder_path).is_dir():
        print("")
    else:
        os.makedirs(folder_path)
    logs_path = "./LOGS/Automatic_Push_logs"
    log_file = f"{PUSH_START_DATE} - {PUSH_END_DATE}.txt"
    log_file_path = logs_path + "/" + log_file

    with open(log_file_path, "w") as logs:
        logs.write(f"Policy Details{PUSH_INFO[0]}\n")
        logs.write(f"Policy Details{PUSH_INFO[1]}\n")
        logs.write(f"Date Modified {current_datetime}\n\n\n")














