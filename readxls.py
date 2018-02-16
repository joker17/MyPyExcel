#!/usr/local/bin/python3
#import pyexcel_io
import sys
import json
import collections
#sys.path.append("/usr/local/lib/python3.6/site-packages")
print("test[%s]" % sys.path)
print("test[%s]" % sys.version)
import pyexcel as pe

records = pe.iget_records(file_name="./data1.xls")
t1 = collections.OrderedDict(records)
#records = pe.iget_records(file_name="./test_xlsx.xlsx")
#print("[%s]", records[0][1])
for record in records:
    print("%s is aged at %d" % (record['NAME'], record['AGE']))

for key, item in t1.items():
    print(json.dumps({key: item}))