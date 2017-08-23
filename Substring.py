__author__ = 'eduardo.fano'

fileList= ['file1.txt', 'myprogram.exe', 'file2.txt']

for fileName in fileList:
	if '.txt' in fileName:
	   print (fileName)