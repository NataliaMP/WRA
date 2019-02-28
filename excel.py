import xlrd

workbook = xlrd.open_workbook("190219_serviciosWRAmanualV5.xls")
worksheet = workbook.sheet_by_name("ServiciosDWDM")

workbook2 = xlrd.open_workbook("Transponders.xlsx")
worksheet2 = workbook2.sheet_by_name("Hoja1")

filas = worksheet.nrows
filas2 = worksheet2.nrows

my_dict = {}

for i in range(2, filas):
    Equipo_A = worksheet.cell(i, 12).value
    Client = worksheet.cell(i, 13).value
    Line = worksheet.cell(i, 14).value

    for i in range(0, filas2):
        NEname = worksheet2.cell(x, 1).value
        Transponder = worksheet.cell(x,2).value

 if Equipo_A == NEname:
 if Client == Transponder:
 worksheet.cell(i,19).value = worksheet2.cell(x,8).value)

