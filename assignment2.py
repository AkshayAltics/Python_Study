'''
Created on 05-Mar-2019

@author: Admin
'''
import os 
import datetime as dt
import datetime
from datetime import timedelta, date

currdate=datetime.datetime.today()

print('Current Date Time in =',(currdate.year, currdate.month, currdate.day))

BSEFolder=currdate.strftime('%y')  #get year ex 19,20
NSEFolder = currdate.strftime('%Y')  #get year ex 2019,2020

print(NSEFolder,BSEFolder)
if os.path.isdir("f:/StockAnalysis/BSE/Staging/"+BSEFolder):
    print("directory exist") 
    print(os.path.getctime("f:/StockAnalysis/BSE/Staging/"+BSEFolder)) 
else:
    os.mkdir("f:/StockAnalysis/BSE/Staging/"+BSEFolder)   
    
    
if os.path.isdir("f:/StockAnalysis/NSE/Staging/"+NSEFolder):
    print("directory exist") 
    print(os.path.getctime("f:/StockAnalysis/NSE/Staging/"+NSEFolder)) 
else:
    os.mkdir("f:/StockAnalysis/NSE/Staging/"+NSEFolder)          

a=1
b='2'
print(int(2.5))
print(a+int(b))

''''''''''''''''''''''''''''''''''''
correct_password="123"
name=input("enter your name")
password=input("enter password")
message="hi %s you loged in"%(name)


while correct_password != password:
    password=input("incorrect password! enter again")
    
print(message)

''''''''''''''''''''''''''''''''
myfile=open("sample.txt",'w')
myfile.write("something")
myfile.close()

with open("sample.txt",'w') as myfile:
    myfile.write("something")
    
myfile.close()
    
with open("sample.txt",'r') as myfile: 
    n=myfile.read() 
    print(n)
myfile.close()      