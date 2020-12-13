from openpyxl import Workbook
wb = Workbook()
ws = wb.active
data = [['aooles',1000,5000,8000,6000],
        ['perars',2000,3000,4000,5000],
        ['bana',3,2,1,0],
        ]
ws.append(['fruit','2011','2012','2013','2014'])
for row in data:
    ws.append(row)
