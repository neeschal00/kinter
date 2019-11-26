from tkinter import *
root = Tk()
root.title('Simple calculator') #for title of the program

e = Entry(root, width = 55, borderwidth=5)
e.grid(row = 0, column = 0, columnspan= 3, padx=10, pady=10)

def button_click(number): #function defined for buttons to add or accept more than 1 digits
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0,str(current) + str(number))
def button_clear(): #clears the data or operation executed or other anything
	e.delete(0,END)
def button_add():
	first_number = e.get() #gets the number number entered
	global fun_num #global variable to conduct operation
	global math
	math = 'addition' #conditional global variable
	fun_num = int(first_number)
	e.delete(0, END)

def button_subt():
	first_number = e.get()
	global fun_num
	global math #need to be mentioned in order to be accesed
	math = 'subtraction'
	fun_num = int(first_number)
	e.delete(0, END)

def button_mult():
	first_number = e.get()
	global fun_num
	global math
	math = 'multiplication'
	fun_num = int(first_number)
	e.delete(0, END)

def button_div():
	first_number = e.get()
	global fun_num
	global math
	math = 'division'
	fun_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	if math == 'addition': #checking the conditional variable the program is executed
		e.insert(0, fun_num + int(second_number))
	if math == 'subtraction':
		e.insert(0, fun_num - int(second_number))
	if math == 'multiplication':
		e.insert(0, fun_num * int(second_number))
	if math == 'division':
		e.insert(0, fun_num / int(second_number))


#buttons for evry numbers and operators
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda:button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda:button_click(2)) #lamda cause the function can't have parenthesis(functionname) in buttons
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda:button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda:button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda:button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda:button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command= lambda:button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command= lambda:button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command= lambda:button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command= lambda:button_click(0))


button_ad = Button(root, text='+', padx=39, pady=20, command=button_add) #no need to use the parameter as no function used
button_sub = Button(root, text='-', padx=39, pady=20, command=button_subt)
button_mul = Button(root, text='*', padx=39,pady=20,command=button_mult)
button_div = Button(root, text='/', padx=39, pady=20, command=button_div)
button_equal = Button(root, text='=', padx=39, pady=40, command=button_equal)
button_clear = Button(root, text='CLR', padx=93,pady=20 , command=button_clear)



#Arranging the calculator using grid
button_1.grid(row=3 , column=0 )
button_2.grid(row=3, column= 1)
button_3.grid(row=3 , column= 2)

button_4.grid(row=2 , column= 0)
button_5.grid(row=2, column= 1)
button_6.grid(row=2 , column= 2)

button_7.grid(row=1 , column= 0)
button_8.grid(row= 1, column= 1)
button_9.grid(row=1 , column= 2)

button_0.grid(row=4 , column=0 )
button_ad.grid(row=5 , column=0 )
button_sub.grid(row=5, column=1)
button_mul.grid(row=4, column=1)
button_div.grid(row=4, column=2)
button_equal.grid(row=5,column=2, rowspan=2) #rowspan to occupy two row space , need to have space mentioned to be equal to sixe of two rows
button_clear.grid(row=6, column=0, columnspan=2)#columnspan same as rowspan

root.mainloop()
