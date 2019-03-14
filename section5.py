import json
from difflib import get_close_matches
import pandas
import xlrd

data = json.load(open("data.json"))
'''
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn=yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    '''
#read csv
df=pandas.read_csv("f:/CodeRepo/demo.csv")
print(df)

#read json
df=pandas.read_json("f:/CodeRepo/demo.json")
print(df)

#read excel
df=pandas.read_excel("f:/CodeRepo/titanic3.xls","titanic3",index_col=None,na_values=['na'])
print(df)

#read txt with ,seperator
df=pandas.read_csv("f:/CodeRepo/demo_c.txt")
print(df)

#read with semicolan 
df=pandas.read_csv("f:/CodeRepo/demo_sc.txt",delimiter=';')
print(df)

#read without header
df=pandas.read_csv("f:/CodeRepo/demo_c.txt",header=None)
print(df)

#add header to tables when display
df=pandas.read_csv("f:/CodeRepo/demo_c.txt")
print(df)

#adding columns
df.columns=["ID","Address","City","Zip","Country","Name","Employees"]
print(df)





print(df.set_index("ID",inplace=True,drop=False))


print(df.loc[1:3,"ID"])


print(df.loc[2:5])



print(df.loc[: ,"Country"])


list1=list(df.loc[: ,"Country"])
print(list1)

df1=df.iloc[1:4 ,[1,2]]
print(df1)

# 0 in second argument specify to delete the column from dataframe and you have to pass row number
df1=df.drop(1,0)
print(df1)

#1 in second argument specify to delete the column from dataframe and you have to pass column name
df1=df.drop("Country",1)
print(df1)
