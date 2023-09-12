import time
from tkinter import *
import ttkbootstrap as tb
import customtkinter
import threading

from Error_messges import openNewWindow
from Get_Niid_Spool import get_niid_spool
from Push_to_Niid import Push_to_Niid
import os
from pathlib import Path

from Format_date import format_date
from  Comparing_Date import comparing_date
from push_date import run
from test import change_sheet_name

LightTheme = ["pulse","default","default","white"]
DarkTheme = ["cyborg","dark","default","black"]
Theme = DarkTheme

root = tb.Window(themename=Theme[0])
# root = Tk()
root.title("A&G Policy Updater")
root.iconbitmap("./A&GICON.ico")
root.geometry('600x500')


# Done = ""

def run_program():

    def run_program_auto():
        run()


    def update():
        # my_progress.start()
        error_message.config(text="Working on it👩‍💻", bootstyle="success")
        Reg_update_button.config(state="disabled")
        downloads_path = Path.home() / "Downloads"
        file_path = f"{downloads_path}/NIID Spool.xlsx"

        #Getting the date from the input
        input_start_date = start_date.entry.get()
        input_end_date = end_date.entry.get()

        #replacing the "/" string with "-"
        edited_start_date = input_start_date.replace("/","-")
        edited_end_date = input_end_date.replace("/", "-")

        #Getting error message if the date format is wrong
        ErrorMessage = comparing_date(edited_start_date,edited_end_date)
        if ErrorMessage == "From Date cannot be greater than To Date.":
            error_message.config(text=ErrorMessage, bootstyle="danger")
            time.sleep(3)
            error_message.config(text="")
        else:
            # Getting the formmated date
            formated_start_date = format_date(edited_start_date)
            formated_end_date = format_date(edited_end_date)


            try:
                error_message.config(text="Geting the file👩‍💻", bootstyle="success")
                get_niid_spool(formated_start_date, formated_end_date)
                error_message.config(text="Edditing Sheet‍💻", bootstyle="success")
                change_sheet_name()
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    time.sleep(3)
                    error_message.config(text="",)
                    return


            print("gotten Data")
            try:
                error_message.config(text="Pushing to NIID👩‍💻", bootstyle="success")
                errmessage = Push_to_Niid()
                openNewWindow(root,errmessage)
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    time.sleep(3)
                    error_message.config(text="",)
                    return


            # global Done
            # Done = "Done"
            error_message.config(text="Done✅", bootstyle="success")
            time.sleep(3)
            error_message.config(text="")
            print("Done")
            try:
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            Reg_update_button.config(state="enabled")



    def run_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update)
        thread.start()
        # thread1 = threading.Thread(target=loading)
        # thread1.start()


    my_frame = customtkinter.CTkFrame(root, fg_color=Theme[3],  border_width=2, width=800, height=550)
    my_frame.pack(fill="both", expand=True,pady=70, padx=100)
    root.rowconfigure(4, weight=1)

    my_label = tb.Label(my_frame, text="Fill In the required details", bootstyle="default", font=("Inter", 18))
    my_label.pack(pady=30, padx=(20, 20))

    start_date = tb.DateEntry(my_frame, bootstyle="dark", )
    start_date.pack(pady=5)

    end_date = tb.DateEntry(my_frame, bootstyle="dark",)
    end_date.pack(pady=5)

    Reg_update_button = tb.Button(my_frame, bootstyle="danger", text="Push", width=30, command=run_function_in_background)
    Reg_update_button.pack( padx=0, pady=10, )

    auto_push = tb.Button(my_frame, bootstyle="danger", text="Push Automatically", width=30, command=run_program_auto)
    auto_push.pack(padx=0, pady=10, )

    # if Done == "":
    #     my_progress = tb.Progressbar(root, bootstyle="success", maximum=100, mode="determinate", length=300, value=0)
    #     my_progress.pack(fill=X, pady=5, padx=20)
    # else:
    #     print("non")

    error_message = tb.Label(my_frame, text="", bootstyle="danger", font=("Inter", 9))
    error_message.pack(pady=2, padx=(10, 20))



    root.mainloop()

if __name__ == '__main__':
    run_program()

# //span[@id="MainContent_lblErrorMessage"]