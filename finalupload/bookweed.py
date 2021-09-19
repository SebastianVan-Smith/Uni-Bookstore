# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:29:56 2020

@author: sebastian


this program compiles relevent staticstics of the database and then uses 
them to weed out books based on interquartile ranges above the median
it then provides the data to plot this onto a box plot and a line graph

"""
from copy import deepcopy
import matplotlib.pyplot as plt
import database as db
import datetime
import statistics as st


1234567891234567891234567891234567891234567891234567891234567891234567891234567891234567891234567891

def bookarrayinitilastion(bookentry):
    """initilises a array containing the books title and all book ids
    associated with it in a 3D array as this makes it easier to do
    things later e.g[[book_1,[id1,id2]],[book_2,[id3,id4]]]"""
    
    bookarray = []
    bookdatabase = deepcopy(bookentry)
    bookdatabase.sort(key=lambda x:(x[2]))
    
    #converts all indexs to ints from strs
    for n in range(0,len(bookdatabase)):
        bookdatabase[n][0]=int(bookdatabase[n][0])
        
    #this adds the book title and id then keeps adding ids till the book names dont match 
    for n in range(0,len(bookdatabase)):
        temp=[]
        end=False
        if n < len(bookdatabase)-1:        
            count=n+1
        else:
            break
        
        temp.append(bookdatabase[n][0])
        while bookdatabase[count][2]==bookdatabase[n][2] and end==False:      
            temp.append(bookdatabase[count][0])
                 
            if count <len(bookdatabase)-1:            
                count+=1
            
            else:
                end=True
               
        bookarray.append([bookdatabase[n][2],temp])   
        #deletes the dupes
    bookarray=removeconcecutivedupes(bookarray)

    return bookarray
    
def removeconcecutivedupes(array):
    '''will delete duplicate logs from bookarrayintiliastion by delteing all 
    logs with matching names above the first'''
    count=0
    while count <len(array)-1:   
        if array[count][0]==array[count+1][0]:
            array.pop(count+1)
        else:      
            count+=1
    return array
        
        

def slowtotal(bookarray,logentry):
    '''finds total each book id was taken out by itterating every book then 
    everylog, this is really slow though for 22000books and 300000logs'''
    for n in range(0,len(bookarray)):#8000
        bookarray[n].append(0)
        for m in range(0,len(bookarray[n][1])):#3
            
            for p in range(int(bookarray[n][1][m]),len(logentry)):#290000
                if bookarray[n][1][m]==logentry[p][0]:
                   bookarray[n][2]+=1
                 
def str_to_datetime(string):
    p=datetime.datetime.strptime(string,"%Y/%m/%d")
    return(p)

def fasttotal(bookentry,logentry):
    """as all logs have the book id in them, i insted looped through the 
    logarray and used the book id as the index of the total variable in a 
    seperate array it also find time since it was brought in days"""
    
    ammountoftakeout = []
    ammountoftime = []

    for n in range(0,len(bookentry)):#creates list of 0 of length bookentry
        ammountoftakeout.append(0)
        ammountoftime.append((datetime.datetime.today()-str_to_datetime(bookentry[n][4])).days)
   
    for n in range(0,len(logentry)):#goes through every log then incriments 

        ammountoftakeout[int(logentry[n][0])]+=1#the value to the id of that log by 1
  

    return(ammountoftakeout,ammountoftime)


def appenddatatobookentry(bookentry,bookarray,booktimecount,booklogcount):
    """appends the data calcuated from total to the main 3D array """
    
    for n in range(0,len(bookentry)):
        bookentry[n].append(booklogcount[n])
        bookentry[n].append(booktimecount[n])

    for n in range(0,len(bookarray)):
        bookarray[n].append([])
        bookarray[n].append([])
        
        for m in range(0,len(bookarray[n][1])):
            bookarray[n][2].append(bookentry[bookarray[n][1][m]][6])
            bookarray[n][3].append(bookentry[bookarray[n][1][m]][7])

def addsums(bookarray):
    """appends the total of the previously two calcualted lists to the main array"""

    for n in range(0,len(bookarray)):
        bookarray[n].append(sum(bookarray[n][2]))
        bookarray[n].append(sum(bookarray[n][3]))
        bookarray[n].append(int(bookarray[n][5]/bookarray[n][4]))
        
        

def datacollection():    
    """jsut does every previous function in the correct order to make the 
    main array with all the data in"""
    
    bookentry=db.readfrombook()
    logentry=db.readfromlog()
    booklogcount,booktimecount=fasttotal(bookentry,logentry)
    bookarray=bookarrayinitilastion(bookentry)
    appenddatatobookentry(bookentry,bookarray,booktimecount,booklogcount)
    addsums(bookarray)
    
    return bookarray


#sorts the list based on how much each book was taken out
#print(bookarray)


def weeding(iqcutoff):
    """uses the data form the main array to create two smaller arrays of data
    so it is eaier to pass and graph in the main program, it also generates
    the list of books to weedout based on the input"""
    
    
    bookarray=datacollection()
    #print(bookarray)
    bookarray.sort(key=lambda x:(x[4]))
    
    takeoutdist=[]
    for n in range(0,len(bookarray)):
        takeoutdist.append(bookarray[n][4])

    
    bookarray.sort(key=lambda x:(x[6]))
    
    timedist=[]
    for n in range(0,len(bookarray)):
        timedist.append(bookarray[n][6])
    quartiles=st.quantiles(timedist,n=4,method='exclusive')
    interquartile_range=quartiles[2]-quartiles[0]


    data=[]
    data.append(quartiles)
    data.append(interquartile_range)
    data.append(st.median(timedist)+(iqcutoff+0.5)*interquartile_range)
    data.append(st.median(timedist))#becuase we using rates

    
    alldata=[data,takeoutdist,timedist]
    
    books_to_weed=[]
    for n in range(0,len(bookarray)):
        if bookarray[n][6]>=data[2]:
           
            books_to_weed.append(bookarray[n])
    return(books_to_weed,alldata)


if __name__=="__main__":
    print("if this runs your all good it outsputs all info needed from weeding")
    print(weeding(3)) 
#if this doesnt have a error you all good as it needs all functions
#to work'''



