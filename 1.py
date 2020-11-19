from openpyxl import Workbook
wb = Workbook()
ws =wb.active

data = [
    ["fruit","quantity"],
    ["kiwi",3],
    ["grape",15],
    ["apple",3],
    ["pear",3],
    ["mango",3]
]
for r in data:
    ws.append(r)
ws.auto_filter.ref = "A1:B15"
ws.auto_filter.add_filter_column(0,["kawi","apple","mango"])
ws.auto_filter.add_sort_condition("B2:B15")
wb.save('1.xlsx')
