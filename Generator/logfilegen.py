# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:03:04 2020

@author: sebastian
"""
import random

import datetime


dbentry=[]
with open("book_name+isbn.txt","r") as database:
    for book in database:
        dbentry.append(book.rstrip("\n").split(','))
    #waste=dbentry.pop(0)   
        
def log_gen(ammount):
    
    logs=[]
    for n in range (0,ammount):
        try:
            random_int=random.randint(1,len(dbentry)-1)
            date_brought=str_to_datetime(dbentry[random_int][4])
        except:
            print(random_int)
            #HEREEEEEEEEEEEEEEEEEEEEEEEE
        dayrange=(datetime.datetime.now()-datetime.timedelta(150)-date_brought).days
        #HEREEEEEEEEEEEEEEE
        take_out_day=date_brought+datetime.timedelta(random.randint(0,dayrange+50))
        return_day=take_out_day+datetime.timedelta(random.randint(10,100))  
        if n==ammount/4:
            print("25%")
        if n==ammount/2:
            print("50%")
        if n == ammount*3/4:
            print("75%")
        if n==ammount-1:
            print("100%\n")
        logs.append([dbentry[random_int][0],take_out_day,return_day])
    return(logs)

'''



ICHANGED THIS SO IT CANT MAKE A BOOK BE TAKEN OUT AT CUTRRENT DATE BY ADDING
150 DAYS TO IT I NED TO CHA GE THIS SO THAT IT DOES ALLOW IT AND THEN ASSIGNS 
IT TO A RANDOM PERSON.

PEOPLE SHOULD USE 6 DIGIT ID


'''





'''  
        for i in logs:
            
            if i[0]==dbentry[random_int][0]:
                
                if (take_out_day<i[2] and take_out_day>i[1]) or (return_day<i[2] and return_day>i[1]):
                   take_out_day=date_brought+datetime.timedelta(random.randint(0,dayrange+50))
                   return_day=take_out_day+datetime.timedelta(random.randint(0,100))   
                   
                   
'''
def remove_dupe_fast(logs):

    #sorts the lsit
    for n in range(0,len(logs)):
        logs[n][0]=int(logs[n][0])
    logs.sort(key=lambda x:(x[0],x[1]))
    

    # initilises 
    removelist=[]
    
    ammount=len(logs)
    for n in range(0,len(logs)-1):
        count=n
        if n==ammount/4:
            print("25%")
        if n==ammount/2:
            print("50%")
        if n == ammount*3/4:
            print("75%")
        if n==ammount-1:
            print("100%\n")

   
        while logs[n][0]==logs[count][0] and n<ammount-2:
            #print(logs[n][0]==logs[count][0])
            
            if (logs[n][1]<logs[count][2] and logs[n][1]>logs[count][1]) or (logs[n][2]<logs[count][2] and logs[n][2]>logs[count][1]):
                    removelist.append(count)
            if count < len(logs)-1:
                count=count+1
            else:
        
                break
    
  
    ammount=len(removelist)
    for n in range (0,len(removelist)):
        
        if n==ammount/4:
            print("25%")
        if n==ammount/2:
            print("50%")
        if n == ammount*3/4:
            print("75%")
        if n==ammount-1:
            print("100%\n")
        #print(logs[removelist[n]],logs[removelist[n]-1],removelist[n])
        logs.pop(removelist[n]-n)
    print("writing")
    return(logs)



def remove_dupe(logs):
    ammount=len(logs)
    for n in range(1,len(logs)):
        
        if n==ammount/4:
            print("25%")
        if n==ammount/2:
            print("50%")
        if n == ammount*3/4:
            print("75%")
        if n==ammount-1:
            print("100%\n")
        
        

       # try:
           
           
        
        for m in range(n,len(logs)):
            removelist=[]
            if logs[n][0]==logs[m][0]:
                if (logs[n][1]<logs[m][2] and logs[n][1]>logs[m][1]) or (logs[n][2]<logs[m][2] and logs[n][2]>logs[m][1]):
                    removelist.append(m)
            
        for p in range(0,len(removelist)):            
            logs.remove(logs[removelist[p]-p])
       # except:
           # print(n,m)
    return(logs)

def str_to_datetime(string):
    p=datetime.datetime.strptime(string,"%d/%m/%Y")
    return(p)
def datetime_to_str(datetimeobj):
    p=datetimeobj.strftime('%d/%m/%Y')
    return p

logs=log_gen(400000)
logs=remove_dupe_fast(logs)

print(len(logs))
f=open("logfile.txt","w+") 
for n in range(1,len(logs)):
    for m in range(1,3):
        logs[n][m]=datetime_to_str(logs[n][m])
    f.write(str(logs[n][0])+","+logs[n][1]+","+logs[n][2]+"\n")
        

