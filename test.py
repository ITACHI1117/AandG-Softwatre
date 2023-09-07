# import pandas as pd
# import numpy as np
# import glob
#
# files = glob.glob('*.xlsx')
#
# excel_file_path ="Chassis Cover.xlsx"
#
#
# for f in files:
#     sales = pd.read_excel('NIID Spool.xlsx')
#
#     print(sales)
#     df = pd.DataFrame(sales)
#     df.to_excel(excel_file_path, index=False)
# #
# #     def_list.append(csv)
# #
# # sales = pd.concat(def_list)
#
# # print(sales)
import os
import time

directory_path = "C:/Users/ICT001/PycharmProjects/A&G Software"
file_name = "NIID Spool.xlsx"

file_path = os.path.join(directory_path, file_name)

while not os.path.isfile(file_path):
    time.sleep(2)
    print(f"The file '{file_name}' exists in the directory '{directory_path}'.")
else:
    print(f"The file '{file_name}'  exist in the directory '{directory_path}'.")