
def get_last_push_dates_epin():
    start_date = ""
    end_date = ""
    # Open a file in read mode ('r')
    file_path1 = './LOGS/E_PIN_Last_push_date/last_push_Sdate.txt'  # Replace with the path to your file
    file_path2 = './LOGS/E_PIN_Last_push_date/last_push_Edate.txt'
    try:
        with open(file_path1, 'r') as file:
            start_date = file.read()
            original_string = f"{start_date}"
            letters_to_remove = "[]',"
            for letter in letters_to_remove:
                original_string = original_string.replace(letter, "")
            start_date_list = original_string.split()
            START_DATE = [int(start_date_list[0]),int(start_date_list[1]),int(start_date_list[2])]
            print(START_DATE)
        with open(file_path2, 'r') as file:
            end_date = file.read()
            original_string2 = f"{end_date}"
            letters_to_remove2 = "[]',"
            for letter2 in letters_to_remove2:
                original_string2 = original_string2.replace(letter2, "")
            end_date_list = original_string2.split()
            END_DATE = [int(end_date_list[0]), int(end_date_list[1]), int(end_date_list[2])]
            print(END_DATE)
    except FileNotFoundError:
        print(f"The file '{file_path1} or {file_path2}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return START_DATE,END_DATE

