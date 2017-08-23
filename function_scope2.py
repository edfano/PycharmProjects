__author__ = 'eduardo.fano'

def f1():
    var1='var local to f1'
    print(var1)

def f2():
    var1='var local to f2'
    print(var1)
    f1():

