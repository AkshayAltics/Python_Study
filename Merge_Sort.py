'''
Created on Mar 3, 2019

@author: nishad
'''

import pandas as pd
import glob
import datetime
import traceback
from datetime import timedelta, date
import datetime as dt
import os


def BSE_NSE_MERGE_SORT(msg):
    msg=msg.upper()
    print(msg)
    print("im from "+msg+" sort and merge method")
    interesting_files = glob.glob("f:/StockAnalysis/"+msg+"/Staging/*/*.csv") 
    df = pd.concat((pd.read_csv(f, header = 0) for f in interesting_files))
    df_deduplicated = df.drop_duplicates()
    df_deduplicated.to_csv(msg+"MergedFile.csv",index=False)
    #open for sort
    demo_df=pd.read_csv(msg+"MergedFile.csv")           
    #print(demo_df)
    #Sort file by high and low with descending and ascending order reps.
    if msg=="NSE":
        ls=demo_df.sort_values(['HIGH','LOW'], ascending=(False,True))
        print("nse data is sorting")
        print(ls.iloc[0:10,[3,4]])
    else:
        ls=demo_df.sort_values(['HIGH','LOW'], ascending=(False,True)) 
        print("bse data is sorting")
        print(ls.iloc[0:10,[5,6]])
    df1=pd.DataFrame(ls)
    # write to csv file
    
    df1.to_csv(msg+'SortedFile.csv',index=False)
    print(msg+"done")



#function for single file

def NSE_BSE_OneFile_Operation(msg,filname,year):
    msg=msg.upper()    
    print("NSE FILE data on single file")
    if os.path.isfile("f:/StockAnalysis/"+msg+"/Staging/"+year+"/"+filename):
    
        NSE_df=pd.read_csv("f:/StockAnalysis/"+msg+"/Staging/"+year+"/"+filename)
        NSE_df['Diff'] = (NSE_df.OPEN - NSE_df.CLOSE)
    
        ls1=NSE_df.sort_values(['Diff'], ascending=(False)) 
        print("Max increases data on single file")   
        print("MAX INCREASE",ls1.iloc[0:5])
        max_increas=pd.DataFrame(ls1.iloc[0:5])
        # write to csv file
        
        max_increas.to_csv(msg+'_max_increase_'+filname,index=False)
        print(msg+"done")
    
        ls1=NSE_df.sort_values(['Diff'], ascending=(True)) 
        print("MAX DECREASE",ls1.iloc[0:5,[14]])
        max_decrease=pd.DataFrame(ls1.iloc[0:5])    
        
        max_decrease.to_csv(msg+'_max_decrease_'+filname,index=False)
        print(msg+"done")     
    else:
        print("file not found")

def NSE_BSE_MergedFile_Operation(msg):
    msg=msg.upper()
    print(msg+" FILE data")
    if os.path.isfile(msg+"MergedFile.csv"):    
        filedata=pd.read_csv(msg+"MergedFile.csv")
        filedata['Diff'] = (filedata.OPEN - filedata.CLOSE)
    
        ls1=filedata.sort_values(['Diff'], ascending=(False)) 
        print("MAX INCREASE",ls1.iloc[0:5])
        max_increas=pd.DataFrame(ls1.iloc[0:5])
        # write to csv file
        
        max_increas.to_csv(msg+'_Mergedfile_max_increase_.csv',index=False)
        print(msg+"done")
        
        ls1=filedata.sort_values(['Diff'], ascending=(True)) 
        print("MAX DECREASE",ls1.iloc[0:5]) 
        max_decreas=pd.DataFrame(ls1.iloc[0:5])
        # write to csv file
        
        max_decreas.to_csv(msg+'_Mergedfile_max_decrease_.csv',index=False)
        print(msg+"done")
    else:
        print("file not found")                
    
'''
    print("BSE FILE data")
    BSE_df=pd.read_csv("BSEMergedFile.csv")  
    BSE_df['Diff'] = (BSE_df.OPEN - BSE_df.CLOSE)
    ls1=BSE_df.sort_values(['Diff'], ascending=(False)) 
    print("MAX INCREASE",ls1.iloc[0:5]) 
    ls1=BSE_df.sort_values(['Diff'], ascending=(True)) 
    print("MAX DECREASE",ls1.iloc[0:5,[14]])
'''

'''
merge and sort from nse and bse stocks
'''
foldername=input("enter type of stocks")
if "NSE"==foldername.upper() or "BSE"==foldername.upper() :
    BSE_NSE_MERGE_SORT(foldername)
else:
    foldername=input("\nwrong input. Please enter folder name again")    
        
'''
max increase and decrease from nse and bse stocks date wise
'''
foldername1=input("enter type of stocks for date wise operation")
filenamepartdate = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime('%d')#get date

if "NSE"==foldername1.upper(): 

    filenamepartmonth = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime('%b')  #get month in short format like Jan Aug Sep
    filenamepartyear = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime('%Y')  #get year ex 2019,2020
    filename="cm"+filenamepartdate+filenamepartmonth+filenamepartyear+"bhav.csv"
    NSE_BSE_OneFile_Operation("NSE",filename,filenamepartyear)
elif "BSE"==foldername1.upper() :  

    filenamepartmonth = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime('%m')  #get month in short format like Jan Aug Sep
    filenamepartyear = datetime.date.fromordinal(datetime.date.today().toordinal()-1).strftime('%y')  #get year ex 2019,2020
    filename="EQ"+filenamepartdate+filenamepartmonth+filenamepartyear+".csv"
    NSE_BSE_OneFile_Operation("BSE",filename,filenamepartyear)   
else:
    foldername1=input("\nwrong input. Please enter type of stocks for date wise operation again")        


'''
max increase and decrease from nse and bse stocks merged file
'''
foldername=input("enter type of stocks for max increase and decrease from nse and bse stocks merged file")
if "NSE"==foldername.upper() or "BSE"==foldername.upper() :
    NSE_BSE_MergedFile_Operation(foldername)
else:
    foldername=input("\nwrong input. Please enter type of stocks for max increase and decrease from nse and bse stocks merged file")  

