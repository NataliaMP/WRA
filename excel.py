import xlrd

workbook = xlrd.open_workbook("190219_serviciosWRAmanualV5.xls")
worksheet = workbook.sheet_by_name("ServiciosDWDM")

workbook2 = xlrd.open_workbook("Potencia2.xlsx")
worksheet2 = workbook2.sheet_by_name("Hoja1")

filas = worksheet.nrows
filas2 = worksheet2.nrows

my_dict = {}

for i in range(2, filas):
    Equipo_A = worksheet.cell(i, 12).value
    Cliente_Shelf_Slot_A = worksheet.cell(i, 13).value
    Linea_Shelf_Slot_A = worksheet.cell(i, 14).value

    row = worksheet.row_values(i)
    my_dict[Equipo_A] = row


    # if Equipo_A == NEname:
    #     if Cliente_Shelf_Slot_A == Transponder:
    #     worksheet.cell(i,19).value = worksheet2.cell(x,8).value)

