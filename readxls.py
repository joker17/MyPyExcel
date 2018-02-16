#!/usr/local/bin/python3
#-*-coding: utf-8-*-
import os
import pyexcel


def main(base_dir):
    spreadsheet = pyexcel.get_sheet(file_name=os.path.join(base_dir,"hisqs_ti_tbranchdeliver.csv"))
    sqls = rows2sqls(list(spreadsheet.rows() ))
    print("=========\n%s" % sqls)

    
#生成sql插入所有
def rows2sqls(rows):
    index = 0
    names = ""
    values = ""
    sql = ""
    sqls = ""
    cols = ""
    for row in rows:
        print(row)
        if (index == 0):
            head = "insert into hisqs_ti_tbranchdeliver ("
            for value in row:
                names += str(value) + ","
            names = names[:-1]
            names += ")\n"
            head += names
        else:
            col = " select "
            for value in row:
                col += "'" + str(value) + "'" + ","
            col = col[:-1]
            col += " from dual union"
            cols += col
        index += 1
    cols = cols[:cols.rfind("union")]
    sqls = head + cols
    print("-----------%s" % sqls)
    return sqls


if __name__ == '__main__':
    main(os.getcwd())
