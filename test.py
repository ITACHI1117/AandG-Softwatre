# this is a test code
from datetime import datetime

# Get the current date
current_date = datetime.now()
print(current_date)

# Format the date as DD/MM/YY
formatted_date = current_date.strftime('%d/%m/%y')

print(formatted_date)  # Output: 04/05/17 (or the current date in this format)
