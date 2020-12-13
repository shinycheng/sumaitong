from openpyxl import load_workbook
wb = load_workbook(filename='empty_book.xlsx')
sheet_ranges = wb['range']
print(sheet_ranges['D18'].value)