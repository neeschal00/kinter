from tkinter import *
root = Tk()

def myclck():
	mylabel = Label(root, text = entry1.get()) #the entry1.get() text is shown by taking entry and after clicked the button
	mylabel.grid(row = 4) #with the use of grid you were able to use the button just once

mylabel1 = Label(root, text ='Sex')
mylabel2 = Label(root, text ='Age')
mylabel1.grid(row = 0)
mylabel2.grid(row = 1)

entry1 = Entry(root, bg = '#48CCCD' , fg = 'black') #Entry() to input the data 
entry2 = Entry(root, width=40, borderwidth = 6) #boarderwidth and width size can be manipulated
entry1.insert(0, 'Enter your sex')
entry1.grid(row=0 , column = 1) #entry for placement
entry2.grid(row=1 , column = 1)

mybutton = Button(root, text = 'Click here!', bg = 'Red', fg = 'Black', padx = 40, command = myclck) #no need to have parenthesis() 
#padx = size in xaxis and pady = size in y axis
mybutton.grid(row = 3)

root.mainloop()