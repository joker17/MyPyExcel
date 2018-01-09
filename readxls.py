#!/usr/local/bin/python3
#import pyexcel_io
import pyexcel as pe

records = pe.iget_records(file_name="./data1.xls")
for record in records:
    print("%s is aged at %d" % (record['NAME'], record['AGE']))