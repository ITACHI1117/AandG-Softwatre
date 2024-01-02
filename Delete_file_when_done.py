import shutil
from pathlib import Path
import os

# downloads Path
downloads_path = Path.home() / "Downloads"
file_path = f"{downloads_path}/NIID Spool.xlsx"

#Last push date folder path
file_name = "Last_push_date"
folder_path = r"./LOGS/Last_push_date"

#Last push date epin folder path
file_name_epin = "E_PIN_Last_push_date"
folder_path_epin = r"./LOGS/E_PIN_Last_push_date"

#delete function
def delete():
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_last_push_date():
    try:
        shutil.rmtree(folder_path)
        print(f"File '{folder_path}' has been deleted.")
    except FileNotFoundError:
        print(f"File '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_last_push_date_epin():
    try:
        shutil.rmtree(folder_path_epin)
        print(f"File '{folder_path_epin}' has been deleted.")
    except FileNotFoundError:
        print(f"File '{folder_path_epin}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")