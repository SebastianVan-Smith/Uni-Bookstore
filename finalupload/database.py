# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 00:13:48 2020

@author: sebastian

this program contains all functions to interface with the database
including reading and writing from it, i oculd ahve alkso use it for
datetime conversion but i found it easier to jsut copy paste into 
eachone as its jsut three lines.
"""


import datetime

def readfrombook():    
    '''opens the file and writes each line to a array then the 
    whole thing to a 2d array'''
    
    book_db_array=[]
    with open("database.txt","r") as book_database:
        for book in book_database:
            book_db_array.append(book.rstrip("\n").split(','))
            
    return book_db_array


def readfromlog():   
    '''opens the file and writes each line to a array then the 
    whole thing to a 2d array'''
    
    logdb=[]
    with open("logfile.txt","r") as logdatabase:
        for log in logdatabase:
            logdb.append(log.rstrip("\n").split(','))
            
    return logdb


def str_to_datetime(string):
    '''converts str to datetime objects'''
    output=datetime.datetime.strptime(string,"%Y/%m/%d")
    return(output)

def datetime_to_str(datetime_obj):
    '''converts datetime objects to srings'''
    output=datetime_obj.strftime('%Y/%m/%d')
    return output   


'''
i am a god, i can remove the hashed slow lines by using year month day as a
time format insted of day month year, as then in order to sort by date i dont 
need to convert each time to a datetime object first as it will natrually 
be sorted in string form.

this saves arround 10 seconds per book checkout and return now most of the 
time comes from writing to and from the file  
'''

def writetolog(logs):
    '''writes the log array back into the log file'''
    
    #converts first elemnt from str to int to sort
    for n in range(0,len(logs)):
        logs[n][0]=int(logs[n][0])
  
    #sorts on book id then date withdrawed
    logs.sort(key=lambda x:(x[0],x[1]))


    #little deubg code so i can see how many logs were writen    
    print("writing: "+str(len(logs)))
    
    #writes it back to the text file, this was the fastest way i could do it
    writestring=""
    f=open("logfile.txt","w+") 
    for n in range(0,len(logs)):
        writestring+=(str(logs[n][0])+","+logs[n][1]+","+logs[n][2]+"\n")
    
    f.write(writestring)


def writetobook(books):
    '''writes the book array back into the book file, updating it'''
    
    file= open("database.txt","w+")
    for n in range(0,len(books)):
        p=''
        for m in range(0,len(books[n])):
            p+=str(books[n][m])+','
        p=p[:-1]+"\n"#removes the last ,
        file.write(p)
        
if __name__=="__main__":
    #test code to check all functons
    print("reads everybook then writes it all back")
    #reads the books file then overwrites it with its self
    arrayofbooks=readfrombook()
    writetobook(arrayofbooks)
    print("reads everylog the writes them all back")
    #reads the logs file then overwrites it with its self
    arrayoflogs=readfromlog()
    writetolog(arrayoflogs)
    print("dont know how to visually show this in command line but if it doesnt error we good")


