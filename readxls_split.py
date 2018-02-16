#!/usr/local/bin/python3
#-*-coding: utf-8-*-
import os
import pyexcel


def businno2businflag(base_dir):
    records = pyexcel.iget_records(file_name=os.path.join(base_dir,"busin2businflag.xlsx"))
    sqls = " "
    for record in records:
        splitstr = record["busin_flags"]
        if len(splitstr) <= 0: 
            continue
        sql = "insert into qs_tbusinflagtolic(busin_no, busin_flag) values(" + str(record["busin_no"]) + ","
        for businflag in record["busin_flags"].split(","):
            if businflag.isdigit() == False: 
                continue
            sqls += sql + businflag + ");\ncommit;\n"

    print("=========\n%s" % sqls)

def businnolist(base_dir):
    records = pyexcel.iget_records(file_name=os.path.join(base_dir,"busin2businflag.xlsx"))
    sqls = " "
    for record in records:
        sql = ("insert into qs_tlicense (busin_no, busin_name) values(" + str(record["busin_no"]) + 
               ", '" + str(record["desc"]) + "');\ncommit;\n"
        )
        sqls += sql

    print("=========\n%s" % sqls)

if __name__ == '__main__':
    #businno2businflag(os.getcwd())
    businnolist(os.getcwd())