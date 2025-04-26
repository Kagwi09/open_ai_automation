from openpyxl import load_workbook
from datetime import datetime
import os

# Config
file_path = 'material_table_2.xlsx'  # Update this if your file has a different name
sheet_name = 'Received'
columns = [
    'Date', 'Material', 
    'Units', 'Quantity', 
    'Rate', 'Material Cost', 
    'Admin cost', 'Total cost', 
    'Admin cost purpose'
    ]

def is_sunday():
    return datetime.today().weekday() == 6  # Sunday = 6