# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:55:11 2020

@author: sebastian
"""

'''
The main program which makes the GUI and put everyting together
'''
import tkinter as tk
import booksearch as bs
import bookcheckout as bc
import bookreturn as br
import bookweed
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
window = tk.Tk()
window.geometry("1000x1000")

''' places all textinputs and outputs as well as labels'''
label=tk.Label(window,text=("Input book name"))
label.place(x=190,y=0)

label=tk.Label(window,text=("Input inerquartile ranges above median to use as descriminate for book weeding"))
label.place(x=525,y=0)

book_entry = tk.Entry(width=75)
book_entry.place(x=10,y=30)

iqr_entry = tk.Entry(width=15)
iqr_entry.place(x=700,y=30)

book_info_box=tk.Text(window,height=56,width=56,state='disabled',wrap=tk.WORD)
book_info_box.place(x=10,y=90)


def clearbox():
    '''code to reset the textbox in the GUI'''
    cleartext()    
    str1="Input book name and press info to get all info on all book copies\n"    
    str1+="\nInput memberID, BookID and days to withdraw serpeated by commas "
    str1+="and then press Checkout to checkout a book e.g 1234,15515,100 "
    str1+="that would take out book 15515 for 100 days by member 1234\n"
    writetobox(str1)

def booksearch():
    '''searches for a book'''
    textinput=book_entry.get()
    info=bs.booksearch(textinput)
    outputtobook(info)


def outputtobook(info):
    '''manages the output to text box for book searching'''
    if len(info)==0:
        cleartext()
        writetobox("Book Not In DB\n")
    else:
        cleartext()
        string=("Book Title: "+info[0][0][2]+"\n")
        string+=("Author: "+info[0][0][3]+"\n")
        string+=("ISBN: "+info[0][0][1]+"\n"+"\n")
        writetobox(string)
        for n in info:
            
            id_info=("Book ID: "+n[0][0]+"\n")
            id_info+=("Date Brought: "+n[0][4]+"\n")
            id_info+=("Taken By: "+n[0][5]+"\n"+"\n")
            writetobox(id_info)
            
            if n[1]=="No log entries":
                writetobox("Not Taken Out Yet\n")
            else:
                writetobox("Taken Out      Returned\n")
                for p in n:        
                    if len(p[1])!=13:#doesnt print first line containg isbn and book info
                        writetobox(str(p[1])+" "*5+str(p[2])+"\n")
            writetobox("\n")


def bookcheckout():
    '''code for checking out a book and updating text box to show progress'''
    cleartext()
    writetobox("Updating Database...\n")
    window.update()
        
    textinput=book_entry.get()
    textinput=textinput.split(',')
    
    book_info_box['state']='normal'
    book_info_box.delete(("0.0"),tk.END)
    if len(textinput)==3:
       
        info=bc.checkout(textinput[0],textinput[1],textinput[2])
        book_info_box.insert(tk.END,info+"\n")
    else:
        book_info_box.insert(tk.END,"Not Correct Format\n")
        book_info_box['state']='disabled'
def bookreturn():
    """returns a book based on the id placed into the box"""
    textinput=book_entry.get() 
    cleartext()
    writetobox("Updating Database...\n")
    window.update()
    
    info=br.returnbook(textinput)
    cleartext()
    writetobox(info)
    
def writetobox(string):
    '''code to write to the text box'''
    book_info_box['state']='normal'   
    book_info_box.insert(tk.END,string)
    book_info_box['state']='disabled'

def cleartext():
    '''clears the text box'''
    book_info_box['state']='normal'
    book_info_box.delete(("0.0"),tk.END)
    book_info_box['state']='disabled'
    window.update()
    
    
def weedresult():
    '''runs the weeding algorithm then displays the graphs and books
    that were outputted by the algorithm
    '''
    cleartext()
    
    text_input=float(iqr_entry.get())
    books_to_weed,graph_data=bookweed.weeding(text_input)
    writetobox("Stats on Dataset:\n\n")
    writetobox("Inter-quartile range: "+str(graph_data[0][1])+"\n")
    writetobox("Median: %0.2f\n"%(graph_data[0][3]))
    writetobox("Removing books above: %0.2f days between takeout\n\n\n"%(graph_data[0][2]))
    writetobox("Books to Remove:\n\n")
    for n in range(0,len(books_to_weed)):
        writetobox(books_to_weed[n][0]+" "+ str(books_to_weed[n][6])+"\n")

    #plots the grpahs and adds them to the gui
    fig=Figure(figsize=(5,9),dpi=100)

    graph_1=fig.add_subplot(211)
    graph_1.plot(graph_data[1])
    graph_1.grid(True)
    graph_1.title.set_text('Cumulative times takenout, distribution')
    
    
    graph_2=fig.add_subplot(212)    
    graph_2.boxplot(graph_data[2],whis=text_input)##wis is wisker length mult
    graph_2.title.set_text('Days between takeout, distribution')
    graph_2.grid(True)
            
    canvas=FigureCanvasTkAgg(fig,master=window)   
    canvas.draw()
    canvas.get_tk_widget().place(x=490,y=90)

   
'''adds all the buttons and runs the main loop, didnt put in funciton because
it only needs ot be run once'''
clearbox()  
search = tk.Button(window, text="Info", width=12, command=booksearch)
search.place(x=10,y=60)

checkout= tk.Button(window, text="Checkout", width=12, command=bookcheckout)
checkout.place(x=250,y=60)

clear= tk.Button(window, text="Clear Box", width=12, command=clearbox)
clear.place(x=130,y=60)

returnn= tk.Button(window, text="Return", width=12, command=bookreturn)
returnn.place(x=370,y=60)

weed = tk.Button(window, text="Weed Dataset", width=12, command=weedresult)
weed.place(x=700,y=60)

tk.mainloop()

if __name__=="__main__":
    print("""cant really do test code for this as it would jsut test 
functions tested in the sub functions and nothing would run
without the tkinter initilisation""")
