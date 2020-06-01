#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os 
flag= True
if flag == True:
	print ("Test1 is Passed")
	FPrint(os.environ["TestRunFolder"] + r'/REPORT.txt','Test1','PASSED')
else:
	print ("BOM_ModelEdit_Export_Import_Modelcompare  is Failed")
	FPrint(os.environ["TestRunFolder"] + r'/REPORT.txt','Test1','FAILED')

