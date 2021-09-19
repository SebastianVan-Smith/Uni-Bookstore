# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:28:27 2020

@author: sebastian
"""
'''
import random
p=[]
def date():
    return (str(random.randint(0,28))+"\\"+str(random.randint(0,12))+"\\"+str(random.randint(2000,2020)))
with open ("test.txt",'r') as file:
    for i in file:
        p.append(i.rstrip("\n"))
for n in range (0,len(p)) :
    p[n]=str(random.randint(0,999))+","+p[n]+","+date()+","+str(random.randint(0,999))
print(p)'''
from calendar import monthrange
import random
import time

#used for a web scraper
import keyboard
import win32api, win32con


def isbngen():
    if random.randint(1,2)%2==0:
        
        isbn=[9,7,8]
    else:
        isbn=[9,7,9]
    total=0
    finalisbn=''
    for n in range(0,9):
        isbn.append(random.randint(0,9))
    for n in range(0,12):
        if n%2==0:
            total +=isbn[n]*1
        else:
            total +=isbn[n]*3     
    isbn.append((10-(total%10))%10)
    for n in range (0,13):
        finalisbn+=str(isbn[n])
    return(finalisbn)


booknames=[]
with open ("book_names.txt","r") as file:
    for i in file:
        if i.rstrip("\n") not in booknames:
            booknames.append(i.rstrip("\n"))
file.close()


def check():
    for n in range (0,len(booknames)):
        count=0
        marker=0        
        for m in range(0,len(booknames[n])):            
            if booknames[n][m].isupper():
                count=count+1              
                if count>1:
                    marker=m
            elif booknames[n][m]==' ':
                count=0           
        if marker>0:
            l,r=booknames[n][:marker], booknames[n][marker:]
            booknames[n]=l
            booknames.append(r)
                
#check()  
'''            
 used for a webscraper to get book names as i thought it would be easier to 
 do this than make my own book name generator as much as i would have loved to              
'''
def copypaste():
    #https://www.fantasynamegenerators.com/book-title-generator.php#.VvKbtrl96Rs
    
  
    bob=True
    while bob==True:
       
        win32api.SetCursorPos((1700,1150))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1700,1150)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,1700,1150)
        #time.sleep(0.1)
        win32api.SetCursorPos((2000,1130))
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,2000,1130)
        win32api.SetCursorPos((1300,830))
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,1300,830)
        keyboard.press_and_release('ctrl+c') 
        time.sleep(0.1)
        win32api.SetCursorPos((1000,1350))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1000,1300)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,1000,1300)
        keyboard.press_and_release('ctrl+v') 
        keyboard.press_and_release('enter') 
        time.sleep(0.1)
        if keyboard.is_pressed('p'):
            bob=False

def datemake():    
    year=random.randint(2000,2019)
    month=random.randint(1,12)
    p=monthrange(year,month)
    day=random.randint(p[0]+1,p[1])
    return(str(year)+"/"+str(month)+"/"+str(day))
          
isbnlist=[]
count=0
while count<len(booknames):
    p=isbngen()
    if p not in isbnlist:        
        isbnlist.append(p)
        count+=1



import names
authorlist=[]
count=0
while count<3000:
    p=names.get_full_name()
    if p not in authorlist:        
        authorlist.append(p)
        count+=1 
           
dbentry=[[]]
for n in range(0,len(booknames)):
    pp=[]
    pp.append(str(n))     
    pp.append(isbnlist[n])    
    pp.append(booknames[n])    
    pp.append(authorlist[random.randint(0,len(authorlist)-1)])    
    pp.append(datemake())
    dbentry.append(pp)


indexadder=len(dbentry)-1

for n in range(0,12000):
    randnum=random.randint(1,indexadder-1)
    pp=[str(n+indexadder),dbentry[randnum][1],dbentry[randnum][2],dbentry[randnum][3],datemake()]
    dbentry.append(pp)


with open("book_name+isbn.txt","w+") as file:
    for n in range(0,len(dbentry)):
        p=''
        for m in range(0,len(dbentry[n])):
            p+=dbentry[n][m]+','
        p+="0\n"
        file.write(p)

#str(n)+","+isbnlist[n]+","+booknames[n]+","+authorlist[random.randint(0,len(authorlist)-1)]+","+datemake()+",0"+"\n"


