# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:29:12 2020

@author: sebastian

the code requireed to return a book
it has the main function returnbook which is used
by other funcitons to return a book and then sub 
functions to make the code more readable/managable
"""

import database as db
import datetime as dt


bookid=0

def returnbook(bookid):
    """the main function called by """
    bookentry=db.readfrombook()
    logentry=db.readfromlog()
    found=False
    for n in range(0,len( bookentry)):
        if bookentry[n][0]==bookid:
            if int(bookentry[n][5])!=0:
                changebook(bookid,bookentry)
                changelog(bookid,logentry)
                found=True
                return "Book returned"
            else:
                return "Not Taken Out"
    if found==False:
        return "Book not found"
    else:
        return "Book Returned"

def changebook(bookid,bookentry):  
    """changes the memeber associated with the book to 0 for none"""
    for n in range(0,len(bookentry)):
        if bookentry[n][0]==bookid:
            bookentry[n][5]=0
           
    db.writetobook(bookentry)
            
            
def datetime_to_str(datetimeobj):
    """changes satetime objects to srings"""
    p=datetimeobj.strftime('%Y/%m/%d')
    return p           
def changelog(bookid,logs):    
    """changes the logs so that it was taken out on this day"""
    templist=[]   
    for n in range(0,len(logs)):
        if logs[n][0]==bookid:
            templist.append(n)
    logs[templist[-1]][2]=datetime_to_str(dt.datetime.now())
    db.writetolog(logs)

if __name__=="__main__":
    print("if it prints not taken out twice run the takeout book test code")
    print("it tries to take the same book out twice to check it taking it ")
    print("taking out a book then trying to take out a book that already is")
    
    print(returnbook("15515"))#returns book 15515
    print(returnbook("15515"))#to show error if you try to return a returned book

