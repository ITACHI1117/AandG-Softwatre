from tkinter import *
import ttkbootstrap as tb
import customtkinter
import threading
from Get_Niid_Spool import get_niid_spool
from Push_to_Niid import Push_to_Niid
import os



LightTheme = ["pulse","default","default","white"]
DarkTheme = ["cyborg","dark","default","black"]
Theme = DarkTheme

root = tb.Window(themename=Theme[0])
# root = Tk()
root.title("A&G Policy Updater")
root.iconbitmap("./A&GICON.ico")
root.geometry('600x400')


def run_program():
    def update():
        file_path = "NIID Spool.xlsx"
        input_start_date = start_date.entry.get()
        input_end_date = end_date.entry.get()

        edited_start_date = input_start_date.replace("/","-")
        edited_end_date = input_end_date.replace("/", "-")

        get_niid_spool(edited_start_date,edited_end_date)
        print("gotten Data")

        Push_to_Niid()
        print("Done")
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def run_function_in_background():
        # Create a thread to run the long_running_function
        thread = threading.Thread(target=update)
        thread.start()

    my_frame = customtkinter.CTkFrame(root, fg_color=Theme[3],  border_width=2, width=800, height=550)
    my_frame.pack(fill="both", expand=True,pady=70, padx=100)
    root.rowconfigure(4, weight=1)

    my_label = tb.Label(my_frame, text="Fill In the required details", bootstyle="default", font=("Inter", 18))
    my_label.pack(pady=30, padx=(20, 20))

    start_date = tb.DateEntry(my_frame, bootstyle="dark", )
    start_date.pack(pady=5)

    end_date = tb.DateEntry(my_frame, bootstyle="dark",)
    end_date.pack(pady=5)

    Reg_update_button = tb.Button(my_frame, bootstyle="danger", text="Spool", width=30, command=run_function_in_background)
    Reg_update_button.pack( padx=0, pady=10, )



    root.mainloop()

if __name__ == '__main__':
    run_program()

