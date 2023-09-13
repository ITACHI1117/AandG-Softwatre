from pathlib import Path
import os

# downloads Path
downloads_path = Path.home() / "Downloads"
file_path = f"{downloads_path}/NIID Spool.xlsx"

#delete function
def delete():
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")