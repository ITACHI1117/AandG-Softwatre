import os
from pathlib import Path

def write_last_push_date_epin(S_date, E_date):
    # Creating the LOGS Folder if it does not exist
    Log_folder_name = "LOGS"
    if Path(Log_folder_name).is_dir():
        print("")
    else:
        os.makedirs(Log_folder_name)

        # passing the last push date as passed in from the function to LAST_PUSH_DATE
    LAST_PUSH_SDATE = S_date
    LAST_PUSH_EDATE = E_date

    # Creating the Automatic log folder if it does not exist
    folder_name = f"E_PIN_Last_push_date"
    folder_path = "./LOGS/" + folder_name

    #checking if the folder path is already created
    if Path(folder_path).is_dir():
        print("")
    else:
        os.makedirs(folder_path)
    logs_path = f"./LOGS/E_PIN_Last_push_date"
    log_file1 = f"last_push_Sdate.txt"
    log_file2 = f"last_push_Edate.txt"
    log_file_path1 = logs_path + "/" + log_file1
    log_file_path2 = logs_path + "/" + log_file2

    # Writing files
    with open(log_file_path1, "w") as logs:
        logs.write(f"{LAST_PUSH_SDATE}")
        # Writing files
    with open(log_file_path2, "w") as logs:
        logs.write(f"{LAST_PUSH_EDATE}")

