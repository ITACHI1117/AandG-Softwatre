
# Formatting the date for A and G Platform
def format_date(Date):
    string = Date
    string_list = []
    for char in string:
        string_list.append(char)

    new_value = ""
    index_to_remove = 3
    index_to_replace = 4
    if string_list[3] == '0' and string_list[4] == '1':
        new_value = "Jan"
    if string_list[3] == '0' and string_list[4] == '2':
        new_value = "Feb"
    if string_list[3] == '0' and string_list[4] == '3':
        new_value = "Mar"
    if string_list[3] == '0' and string_list[4] == '4':
        new_value = "Apr"
    if string_list[3] == '0' and string_list[4] == '5':
        new_value = "May"
    if string_list[3] == '0' and string_list[4] == '6':
        new_value = "Jun"
    if string_list[3] == '0' and string_list[4] == '7':
        new_value = "Jul"
    if string_list[3] == '0' and string_list[4] == '8':
        new_value = "Aug"
    if string_list[3] == '0' and string_list[4] == '9':
        new_value = "Sep"
    if string_list[3] == '1' and string_list[4] == '0':
        new_value = "Oct"
    if string_list[3] == '1' and string_list[4] == '1':
        new_value = "Nov"
    if string_list[3] == '1' and string_list[4] == '2':
        new_value = "Dec"

    string_list[index_to_replace] = new_value
    del string_list[index_to_remove]

    return string_list


