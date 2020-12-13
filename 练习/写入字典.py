from openpyxl import Workbook
wb = Workbook()
ws = wb.active
a_dict = {'country': 'NL', 'company': 'AliExpress Standard Shipping', 'price': 0.0}
b_dict = {'country': 'NL', 'company': 'AliExpress Standard Shipping', 'price': 1}

values = []
for value in a_dict.values():
    values.append(value)
for value in b_dict.values():
    values.append(value)
ws.append(values)






wb.save('字典.xlsx')