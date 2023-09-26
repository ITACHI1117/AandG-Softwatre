import time
from tkinter import *
import ttkbootstrap as tb
import customtkinter
import threading

from Delete_file_when_done import delete
from Error_messges import openNewWindow
from Get_Niid_Spool import get_niid_spool
from Push_to_Niid import Push_to_Niid
import os
from pathlib import Path

from Format_date import format_date
from Comparing_Date import comparing_date
from Write_logs import write_logs
from push_date import run
from Change_Sheet_Name import change_sheet_name

LightTheme = ["pulse", "default", "default", "white"]
DarkTheme = ["cyborg", "dark", "default", "black"]
Theme = DarkTheme

root = tb.Window(themename=Theme[0])
# root = Tk()
root.title("A&G Policy Updater")
root.iconbitmap("./A&GICON.ico")
root.geometry('1000x700')

# Done = ""
push_Sdate = ""
push_Edate = ""


def run_program():
    #Automatic Push Function
    def run_auto_update():
        global push_Sdate
        global push_Edate
        error_message.config(text=f"Starting👩‍💻...", bootstyle="success")
        Reg_update_button.config(state="disabled")
        auto_push.config(state="disabled")
        try:
            error_message.config(text=f"Pushing👩‍💻...", bootstyle="success")
            # running push
            Pushing_dates = run("", "")
            for Pushing_date in Pushing_dates:
                error_message.config(text=f"Pushed {Pushing_date[0]} to {Pushing_date[1]}", bootstyle="success")
                print(f"pushed {Pushing_date[0]} to {Pushing_date[1]}")
                write_logs(Pushing_date[0], Pushing_date[1], Pushing_date[2])
                push_Sdate = Pushing_date[3]
                push_Edate = Pushing_date[4]
                print(push_Sdate, push_Edate)
            error_message.config(text=f"Done✅", bootstyle="success")
            time.sleep(10)
            error_message.config(text=f"", bootstyle="success")
            continue_push.config(state="disabled")
            return push_Sdate,push_Edate
        except Exception as e:
            print(e)
            # print(push_Sdate, push_Edate)
            delete()
            continue_push.config(state="enabled")
            error_message.config(text=f"There was an error", bootstyle="danger")
            Reg_update_button.config(state="enabled")
            auto_push.config(state="enabled")
            time.sleep(10)
            error_message.config(text=f"", bootstyle="danger")
            return push_Sdate,push_Edate
        finally:
            Reg_update_button.config(state="enabled")
            auto_push.config(state="enabled")


    # Continue Pusshing if an error occurs
    def continue_run_program_auto():
        print(f"push dates {push_Sdate},{push_Edate}")
        time.sleep(4)
        error_message.config(text=f"Starting👩‍💻...", bootstyle="success")
        Reg_update_button.config(state="disabled")
        auto_push.config(state="disabled")
        continue_push.config(state="disabled")
        try:
            error_message.config(text=f"Pushing👩‍💻...", bootstyle="success")
            # Continuing push form last date
            Pushing_dates = run(push_Sdate, push_Edate)
            for Pushing_date in Pushing_dates:
                error_message.config(text=f"Pushed {Pushing_date[0]} to {Pushing_date[1]}", bootstyle="success")
                print(f"pushed {Pushing_date[0]} to {Pushing_date[1]}")
                write_logs(Pushing_date[0], Pushing_date[1], Pushing_date[2])
            error_message.config(text=f"Done✅", bootstyle="success")
            Reg_update_button.config(state="enabled")
            auto_push.config(state="enabled")
            time.sleep(10)
            error_message.config(text=f"", bootstyle="success")
        except Exception as e:
            print(e)
            continue_push.config(state="enabled")
            error_message.config(text=f"There was an error", bootstyle="danger")
            Reg_update_button.config(state="enabled")
            auto_push.config(state="enabled")
            time.sleep(10)
            error_message.config(text=f"", bootstyle="danger")

    #Manual update function
    def update():
        # my_progress.start()
        error_message.config(text="Working on it👩‍💻", bootstyle="success")
        Reg_update_button.config(state="disabled")
        downloads_path = Path.home() / "Downloads"
        file_path = f"{downloads_path}/NIID Spool.xlsx"

        # Getting the date from the input
        input_start_date = start_date.entry.get()
        input_end_date = end_date.entry.get()

        # replacing the "/" string with "-"
        edited_start_date = input_start_date.replace("/", "-")
        edited_end_date = input_end_date.replace("/", "-")

        # Getting error message if the date format is wrong
        ErrorMessage = comparing_date(edited_start_date, edited_end_date)
        if ErrorMessage == "From Date cannot be greater than To Date.":
            error_message.config(text=ErrorMessage, bootstyle="danger")
            time.sleep(3)
            error_message.config(text="")
        else:
            # Getting the formated date
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
                    error_message.config(text="", )
                    return

            print("gotten Data")
            try:
                error_message.config(text="Pushing to NIID👩‍💻", bootstyle="success")
                errmessage = Push_to_Niid()
                openNewWindow(root, errmessage)
            except Exception as e:
                if e:
                    print(e)
                    error_message.config(text="There was an error", bootstyle="danger")
                    time.sleep(3)
                    error_message.config(text="", )
                    return


            error_message.config(text="Done✅", bootstyle="success")
            time.sleep(3)
            error_message.config(text="")
            print("Done")
            #deleting file when done
            try:
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            Reg_update_button.config(state="enabled")

    # Push Manally run in background thread
    def run_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update)
        thread.start()

    # Push Automatically run in background thread
    def run_program_auto():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=run_auto_update)
        thread.start()

    # Continuing Push Automatically run in background thread
    def continue_run_program_auto_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=continue_run_program_auto)
        thread.start()

    #User Interface GUI
    my_frame = customtkinter.CTkFrame(root, fg_color=Theme[3], border_width=2, width=800, height=550)
    my_frame.pack(fill="both", expand=True, pady=70, padx=100)
    root.rowconfigure(4, weight=1)

    my_label = tb.Label(my_frame, text="Push Manually", bootstyle="default", font=("Inter", 18))
    my_label.pack(pady=(50, 1), padx=(20, 20))

    start_date = tb.DateEntry(my_frame, bootstyle="dark", )
    start_date.pack(pady=5)

    end_date = tb.DateEntry(my_frame, bootstyle="dark", )
    end_date.pack(pady=5)

    Reg_update_button = tb.Button(my_frame, bootstyle="danger", text="Push", width=30,
                                  command=run_function_in_background)
    Reg_update_button.pack(padx=0, pady=10, )

    my_label = tb.Label(my_frame, text="Push Policy Automatically ", bootstyle="default", font=("Inter", 18))
    my_label.pack(pady=(20, 1), padx=(20, 20))

    info = tb.Label(my_frame, text="If an error occurs while pushing the continue push button will be enabled",
                    bootstyle="default", font=("Inter", 9))
    info.pack(pady=0, padx=(20, 20))

    info = tb.Label(my_frame, text="Check the README.md file for more info", bootstyle="default", font=("Inter", 9))
    info.pack(pady=5, padx=(20, 20))

    auto_push = tb.Button(my_frame, bootstyle="danger", text="Push Automatically", width=30, command=run_program_auto)
    auto_push.pack(padx=(0, 0), pady=10, )

    continue_push = tb.Button(my_frame, bootstyle="success", text="Continue Push?", width=25, state="disabled",
                              command=continue_run_program_auto_background)
    continue_push.pack(padx=(0, 0), pady=10, )

    error_message = tb.Label(my_frame, text="", bootstyle="danger", font=("Inter", 9))
    error_message.pack(pady=2, padx=(10, 20))

    root.mainloop()


if __name__ == '__main__':
    run_program()


