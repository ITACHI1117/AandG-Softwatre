import os
import time

file_name = "Last_push_date"
folder_path = r"./LOGS/Last_push_date"

file_name_epin = "E_PIN_Last_push_date"
folder_path_epin = r"./LOGS/E_PIN_Last_push_date"

def check_last_push_file():
    if os.path.exists(folder_path):
        print(f"The file exists")
        return True
    else:
        print(f"The file '{file_name}' does not exists in the directory")
        return False

def check_last_push_file_epin():
    if os.path.exists(folder_path_epin):
        print(f"The file exists")
        return True
    else:
        print(f"The file '{file_name_epin}' does not exists in the directory")
        return False