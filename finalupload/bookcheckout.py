# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:08:22 2020

@author: sebastian

takes out books
the main function checkout is called by the menu 
or to check out a book the other function are to 
make the code more managable and easier to read
though some can be used for bespoke functions
"""

import database as db
import datetime as dt

memberid=0
bookid=0


def checkout(memberid,bookid,time):
    """the main function to take out books"""
    bookentry=db.readfrombook()
    logentry=db.readfromlog()
    found=False
    if memberid.isnumeric()==True and len(memberid)==4:
        for n in range(0,len( bookentry)):
            if bookentry[n][0]==bookid:
                if int(bookentry[n][5])==0:
                    changebook(memberid,bookid,bookentry)
                    changelog(bookid,logentry,time)
                    return "Book tanken out"
                else:
                    return "Already taken out"
        if found==False:
            return "Book not found"
    else:
        return "Not valid member id"

def changebook(memberid,bookid,bookentry):
    """ changes the id in the book file to have the member id 
    of the person taking it out"""
    for n in range(0,len(bookentry)):
        if bookentry[n][0]==bookid:
            bookentry[n][5]=memberid
            
    db.writetobook(bookentry)
            
            
def datetime_to_str(datetimeobj):
    p=datetimeobj.strftime('%Y/%m/%d')
    return p   

        
def changelog(bookid,logentry,time):
    """updats the logs based on the new array"""    
    p=datetime_to_str(dt.datetime.now())
    q=datetime_to_str(dt.datetime.now()+dt.timedelta(int(time)))
    logentry.append([bookid,p,q])
    db.writetolog(logentry)
if __name__ =="__main__":
    print("if already taken out run the return book test code")
    print(checkout("1234","15515","10"))#to member 1234 book id 15515 for 10 days
    print(checkout("1234","15515","10"))#to check if it wont let you take out a already checked out book
