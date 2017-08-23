__author__ = 'eduardo.fano'
import re

f=open('file1.txt')

for line in f:
    line=line.strip()
    match=re.search(r'@\w\w\w',line)
    if match:
        print('found', match.group())
    else:
        print('Did not find')
f.close()