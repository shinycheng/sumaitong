import datetime
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws['A1'] = datetime.datetime(2010,7,21)
print(ws['A1'].number_format)
ws['A2'] = "SUM(1,1)"
wb.save('formula.xlsx')