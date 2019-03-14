'''
Created on 04-Mar-2019

@author: Admin
'''



correct_password="python123"
password=input("enter password")

while correct_password != password:
    password=input("incorrect password! enter again")
    
print("logedin")    


file = open("writetext.txt", "w")
list1=[10,20,100]
for temp in list1:
    
    print(temp)
    temp=str(temp)
    file.write(temp+"\n")
file.close()      



def converter2(c):
    return c*9/5+32
list1=[10,-20,100]
for temp in list1:
    print(converter2(temp))    


file = open("fruit.txt", "r")
content = file.read()
file.close()  
content=content.splitlines()
for content in content:
    print(len(content))
  


    
    

file = open("fruit.txt", "r")
content = file.read()
file.close()
print(content)


def str_length(data):
    if((type(data)==int) or (type(data)==float)):
        return "sry data is integer or float"
    else:
        return "length of data is ",len(data)
print(str_length("10"))    
print(str_length(10)) 
print(str_length(10.3)) 
    



def converter1(c):
    return c*9/5+32
print(converter1(10))    




def converter(kg,coef=2.20462):
    return kg*coef
print(converter(10))    


def power(no):
    return no*no
print(power(2))  


def power1(no):
    return pow(no,3)
print(power1(2))   


def hello_world():
    return "Hello World"
print(hello_world())    



a = 1.0
b = 2
print(int(a+b))

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-3:-1])

mylist = ["Marry", "Jack"]
print(mylist)
mylist.append("john")
print(mylist)

mylist = ["Marry", "Jack", "John"]
print(mylist)
mylist.remove("John")
print(mylist)


list1 = [1.2323442655, 1.4534345567, 1.023458894]

list2 = [1.9934332091]
print(list2)
list2.append(list1[-1])
print(list2)


mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c=mylist[0]+mylist[-1]
print(c)


mydict = {"name":'akshay',"study":'python'}
print(mydict.values() ,mydict.keys())



address=["flat no","WSS 2","5","pune"]
pins={"mike":1234,"joe":4569,"harry":987}

print(address[0:3])

pin=int(input("enter your pin"))
def Myfun(f):
    print("size of"+f+ " is ",len(f))
    myfile=open("sample.txt")
    fruits=myfile.read()
    #fruits=fruits.splitlines()
    if f in fruits:
        return "that fruit is in the list"
    else:
        myfile=open("sample.txt",'a+')
        myfile.write("\n")
        myfile.write(f)
        data=myfile.read()
        print("some data from file",data)
        return "that fruit not in the list so we will append to the list"
    myfile.close()
if pin in pins.values():
    fruit=input("fruit name:")
    print(Myfun(fruit))
else:
    print("incorrect pin")
    print("this info only accesible for")
    for key in pins.keys():
        print(key)  
        
exit()   