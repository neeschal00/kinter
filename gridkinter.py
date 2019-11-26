from tkinter import*  # import * to import everything 
root = Tk()
root.title('Shailesh bitch')


mylabel = Label(root , text = 'Hwllo bitcges').grid(row = 1 , column = 1) 
#creating a label widget

#mylabel.grid(row = 1 , column = 1)
#packs it into the window of gui
mylabel1 = Label(root , text = 'I am shailesh giri and i am a fucking ass hole').grid(row = 0 , column = 5)
#mylabel1.grid(row = 0 , column = 5) 

#python ignores the command here as there is no elements between so it doesn't show column 5 because there's no elements between

mybutton = Button(root ,bg = 'Blue', text = 25 , width = 28, command = root.destroy) #bg for background preferance
#creates a button on the window with appropriate text , width and command 
#Button(root, padx = 'size in x axis', pady='size in yaxis',state= 'Enable/Disable')
mybutton.grid(row = 2 , column = 2)
# .pack()puts everything in middel so in order to have freedom of postioning .grid(row = , cloumn = ) is used
# .pack() and .grid() can't be used at the same time 
root.mainloop()


