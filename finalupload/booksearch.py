# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 00:12:50 2020

@author: sebastian


this has the functionality to search for a book the main function will return
a list of book ids and thier respective logs/ lack of logs



"""

import database as db


def findbookpositions(search_string,bookentry):
    """find the book positions given a book id or name"""
    
    if search_string.isnumeric():
        bookpositions=[]
        for n in range(0,len(bookentry)):#can chage this as only looking for one book
            if bookentry[n][0]==search_string:
                bookpositions.append(n)
        
#finds all the positions in book array that has the same title
        
    else:
        bookpositions=[]
        for n in range(0,len(bookentry)):
            if bookentry[n][2].lower().replace(' ','')==search_string:
                bookpositions.append(n)
                
    return bookpositions
                
def findlogposiitons(bookpositions,bookentry,logentry):
    """finds the log entries of a list of books given their ids"""
    logpositions=[]
    for n in range(0,len(bookpositions)):
        temp=[]
        
        for m in range(0,len(logentry)):
            
            if bookentry[bookpositions[n]][0]==logentry[m][0]:
                #print(temp)
                temp.append([bookentry[bookpositions[n]][0],m])
        if len(temp)!=0:
            logpositions.append(temp)    
        else:
            logpositions.append([[bookentry[bookpositions[n]][0],"No log entries"]])
    return logpositions


def booksearch(search_string):
    """the main function that is called form other programs it gets the log 
    and book positions and then makes a array with all the info in a 
    easily machine read-able way"""
    
    bookentry=db.readfrombook()
    logentry=db.readfromlog()
    
    #incase you mess up a capital it puts it all
    # in lowwer case and removes all spaces
    search_string=(str(search_string).lower()).replace(' ', '')
    bookpositions = findbookpositions(search_string,bookentry)  


    logpositions=findlogposiitons(bookpositions,bookentry,logentry)
    
    
    #makes array of all previously collected data
    output=[]
    for n in range(0,len(logpositions)):
     
        temp=[]
        temp.append(bookentry[bookpositions[n]])
        
        
        for m in range(0,len(logpositions[n])):
            
            if str(logpositions[n][m][1]).isnumeric()==True:
                temp.append(logentry[logpositions[n][m][1]])
            else:
                 temp.append("No log entries")
        output.append(temp)

    return output
if __name__ =="__main__":
    print("takes out book by id then name then name mistyped then with error inputs")
    print(booksearch("15515"))
    print(booksearch("Opponent Without Hate"))
    print(booksearch("OpponentWithoutHate"))
    #incase someone really wants to mangle it
    print(booksearch("Op pO ne NtW iT hOu thAte"))
    print(booksearch(" "))
    print(booksearch(3))#it would never be passed a int by my program 
    #but incase it is reused i added a str conversion
    
    print(booksearch("if you wanna add something to test it"))
    print("takes out book by id then name then name mistyped then with error inputs")




