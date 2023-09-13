from pathlib import Path
import openpyxl

def change_sheet_name():
    downloads_path = Path.home() / "Downloads"
    # Load the Excel workbook
    file_path = f"{downloads_path}/NIID Spool.xlsx"  # Replace with the path to your Excel file
    workbook = openpyxl.load_workbook(file_path)

    # Get the sheet whose name you want to change
    old_sheet_name = "3rdParty"  # Replace with the current sheet name
    sheet = workbook[old_sheet_name]

    # Set the new sheet name
    new_sheet_name = "Sheet1"  # Replace with the desired new sheet name
    sheet.title = new_sheet_name

    # Save the workbook with the updated sheet name
    workbook.save(file_path)

    # Close the workbook
    workbook.close()


