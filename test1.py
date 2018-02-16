import pyexcel as pe

#sheet = pe.get_sheet(file_name="./test_xlsx.xlsx")
#sheet = pe.get_sheet(file_name="./data1.xls", name_columns_by_row = 0)
sheet = pe.get_sheet(file_name="./test_xlsx.xlsx", name_rows_by_column = 1, name_columns_by_row = 0)
print(sheet.column[0])
print(sheet.row[0])
print(sheet.column["AGE"])
print(sheet.row["A1"])
print(sheet.row[1])