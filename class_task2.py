# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:05:47 2020

@author: Admin
"""

import pandas as pd
import numpy as np
import os  
import time
os.chdir(r"E:\Python_practice\task_1")
class compare_excel():
    
    def __init__(self,reference,target):
        self.reference=reference
        self.target=target 

    def read(self,reference,target):
        sheet1=pd.read_excel(reference)
        sheet2=pd.read_excel(target)
        comparison_column1 = np.where(((sheet1[sheet1.columns[0]].str.lower() == sheet2[sheet2.columns[0]].str.lower())& (sheet1[sheet1.columns[1]].str.lower() == sheet2[sheet2.columns[1]].str.lower())), True, False)
    
        sheet2["column3"]=comparison_column1
        data=sheet2.loc[sheet2['column3'] == True]
        data.pop("column3")
        #data.to_csv("book3.csv",index=False)
        return sheet1,sheet2,data,comparison_column1
    
if __name__ == '__main__':
    start_time = time.time()
    reference=r"E:\Python_practice\task_1\Book1_case.xlsx"
    target=r"E:\Python_practice\task_1\Book2_case.xlsx"
    object_create=compare_excel(reference,target)
    data1,data2,data,compared_values=object_create.read(reference,target)
    end_time = time.time()
    print('total time ->', end_time - start_time)

#read(reference,target)
    #.str.lower()