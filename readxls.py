#!/usr/local/bin/python3
#import pyexcel_io
import pyexcel as pe

#records = pe.iget_records(file_name="./data1.xls")
records = pe.iget_records(file_name="./test_xlsx.xlsx")
print("[%s]", records[0][1])
for record in records:
    print("%s is aged at %d" % (record['NAME'], record['AGE']))