# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:01:01 2020

@author: sebastian
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:03:04 2020

@author: sebastian
"""
import random
1234567891234567891234567891234567891234567891234567891234567891234567891234567891234567891234567891
import datetime


dbentry = []
with open("book_name+isbn.txt","r") as database:
    for book in database:
        dbentry.append(book.rstrip("\n").split(','))  
        
def log_gen(ammount):
    
    logs = []
    for n in range (0,ammount):
        try:
            random_int = random.randint(1,len(dbentry)-1)
            date_brought = str_to_datetime(dbentry[random_int][4])
        except:
            print(random_int)
            #HEREEEEEEEEEEEEEEEEEEEEEEEE
        dayrange=(datetime.datetime.now()-datetime.timedelta(150)-date_brought).days
        #HEREEEEEEEEEEEEEEE
        take_out_day = date_brought+datetime.timedelta(random.randint(0,dayrange+50))
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
I CHANGED THIS SO IT CANT MAKE A BOOK BE TAKEN OUT AT CUTRRENT DATE BY ADDING
150 DAYS TO IT I NED TO CHA GE THIS SO THAT IT DOES ALLOW IT AND THEN ASSIGNS 
IT TO A RANDOM PERSON. 20/11/2020

i can change this but then i ralised it wouldnt really change any of the
fucitoning of the program and i was kinda getting bored of this part of the 
program as it wasnt part of the original spec and was extra becuase i decided
to make life hard for myself. 

having this large of a data set has actually caused alot of issues that i
wouldnt ahve had to fix otherwise, alot of my initial algorithms were too 
slow on this large of a data set so i ahd to amek them better, ive only kept a 
few of the ones ive replaced. 25/11/2020

'''

def remove_dupe_fast(logs,mode):

    #sorts the lsit
    for n in range(0,len(logs)):
        logs[n][0]=int(logs[n][0])
    logs.sort(key=lambda x:(x[0],x[1]))
    

    # initilises 
    removelist=[]
    
    ammount=len(logs)
    for n in range(0,len(logs)-1):
        if n<ammount-1:
            count=n+1
        if n==ammount/4:
            print("25%")
        if n==ammount/2:
            print("50%")
        if n == ammount*3/4:
            print("75%")
        if n==ammount-10:
            print("100%\n")
        if mode==1:
            if (logs[n][1]<logs[count][2] and logs[n][1]>logs[count][1]) or (logs[n][2]<logs[count][2] and logs[n][2]>logs[count][1]):
                        removelist.append(count)
        if mode==0:
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
        logs.pop(removelist[n]-n)
    return(logs)



def remove_dupe_slow(logs):
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
        
        
        for m in range(n,len(logs)):
            removelist=[]
            if logs[n][0]==logs[m][0]:
                if (logs[n][1]<logs[m][2] and logs[n][1]>logs[m][1]) or (logs[n][2]<logs[m][2] and logs[n][2]>logs[m][1]):
                    removelist.append(m)
            
        for p in range(0,len(removelist)):            
            logs.remove(logs[removelist[p]-p])
    return(logs)




def str_to_datetime(string):
    p=datetime.datetime.strptime(string,"%Y/%m/%d")
    return(p)
def datetime_to_str(datetimeobj):
    p=datetimeobj.strftime('%Y/%m/%d')
    return p

#gens 400000 logs some being overalapping
logs=log_gen(400000)


#this is a updated version so it deletes less valid overlaping logs
for n in range(0,10):
    logs=remove_dupe_fast(logs,1)

#incase it misses some it we run the algorithm in the mode
#that is guarnedded to get them all
logs=remove_dupe_fast(logs,0)

'''
this part writes the finall array of logs into the log file, i could have made
this into a function but there was no point as it only gets called once and
this program is only used to generate datasets
'''
print(len(logs))
f=open("logfile.txt","w+") 
for n in range(1,len(logs)):
    for m in range(1,3):
        logs[n][m]=datetime_to_str(logs[n][m])
    f.write(str(logs[n][0])+","+logs[n][1]+","+logs[n][2]+"\n")
        
