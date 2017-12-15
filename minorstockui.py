

# from sharedetail import code
# from bollingerband import fun 
# from linear import linereg
# from svm import svmalgo
from Tkinter import *
import time
import random
from sharedetail import code
from linear import linereg
from svm import svmalgo
from sharedetail import nws
from bollingerband import fun
from pa import assistant
from recom import recommendation

root = Tk()

root.geometry("1920x1080+0+0")   
root.title("STOCK PREDICTION MODEL")
text_Input=StringVar()
operator=""
Tops= Frame(root, width = 2600, height = 50, bg= "powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 700, height = 1000,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width =300,height=400,bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)



#==================================#========================================#


localtime=time.asctime(time.localtime(time.time()))

lb1Info = Label(Tops, font=('arial',50,'bold'), text="STOCK PREDICTION MODEL",fg="steel blue",bd=10,anchor='w')
lb1Info.grid(row=0,column=0)
lb1Info=Label(Tops, font=('arial',20,'bold'),text=localtime,fg="steel Blue",bd=10, anchor='w')
lb1Info.grid(row=1,column=0)




#=============== calculator=================================#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
	global operator
	operator=""
	text_Input.set("")


def btnEqualsInput():
	global operator
	sumup =str(eval(operator))
	text_Input.set(sumup)
	operator=""

def ref():
		a = str(sharename.get())
		sharename.set(a)
		print a 
		b=code(a)
		print b
		c=str(time.get())
		time.set(c)
		print c
		l = linereg(a,c)
		lr.set(l[0])
		lrerr.set(l[1])
		cp.set(b)

		svm_1 = svmalgo(a,c)
		svm.set(svm_1[0])
		svmerr.set(svm_1[1])


		status = nws(a)
		na.set(status)
def bolli():
    	a = str(sharename.get())
    	fun(a)

def assis():
    	a = str(sharename.get())
    	assistant(a)
    	

def recomm():
    	recommendation()
    	


		
    # a=str(sharename.get())
    # sharename.set(a)
    # print a
    # b = code(a)
    # print b
	# l = linereg(a)
	# line2= linereg(a)
	# lr.set(line[0])
    # cp.set(b)

   

    
txtDisplay = Entry(f2,font=('arial',20,'bold'), textvariable = text_Input ,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)

#===================================================================================#


btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=2,column=2)
Adittion=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=2,column=3)


#=======================================================================================#


btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)
Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=3,column=3)


#=======================================================================================#


btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=4,column=2)
Multiplication=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)


#======================================================================================#


btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),
	text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)




#======================================form===========================================#

sharename=StringVar()
time=StringVar()
user=StringVar()
lts=StringVar()
pp=StringVar()
svmerr=StringVar()
lrerr=StringVar()
na=StringVar()
cp=StringVar()
lr=StringVar()
svm=StringVar()





lb1Stockname = Label(f1,font=('arial',16,'bold'), text="Enter User Name", bd=16 , anchor='w')
lb1Stockname.grid(row=0,column=0)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=user,bd=10,
	insertwidth=4,bg='powder blue',justify='right')
txtStockname.grid(row=0,column=1)

lb1Time = Label(f1,font=('arial',16,'bold'), text="Last Traded Stock", bd=16 , anchor='w')
lb1Time.grid(row=1,column=0)
txtTime = Entry(f1,font=('arial', 16 ,'bold'), textvariable=lts,bd=10,
	insertwidth=10,bg='powder blue',justify='right')
txtTime.grid(row=1,column=1)

lb1Stockname = Label(f1,font=('arial',16,'bold'), text="Enter Stock Name", bd=16 , anchor='w')
lb1Stockname.grid(row=2,column=0)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=sharename,bd=10,
	insertwidth=10,bg='powder blue',justify='right')
txtStockname.grid(row=2,column=1)


lb1Stockname = Label(f1,padx=5,pady=5,font=('arial',16,'bold'), text="Enter Stock Time", bd=16 , anchor='w')
lb1Stockname.grid(row=3,column=0)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=time,bd=10,
	insertwidth=10,bg='powder blue',justify='right')
txtStockname.grid(row=3,column=1)


lb1Stockname = Label(f1,font=('arial',16,'bold'), text="Current Price", bd=16 , anchor='w')
lb1Stockname.grid(row=4,column=0)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=cp,bd=10,
	insertwidth=10,bg='white',justify='right')
txtStockname.grid(row=4,column=1)



lb1Stockname = Label(f1,padx=10,pady=10,font=('arial',16,'bold'), text="News Analysis", bd=16 , anchor='w')
lb1Stockname.grid(row=0,column=8)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=na,bd=10,
	insertwidth=10,bg='white',justify='right')
txtStockname.grid(row=0,column=9)


lb1Stockname = Label(f1,font=('arial',16,'bold'), text="L.R Prediction price", bd=16 , anchor='w')
lb1Stockname.grid(row=1,column=8)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=lr,bd=10,
	insertwidth=10,bg='white',justify='right')
txtStockname.grid(row=1,column=9)

lb1Stockname = Label(f1,font=('arial',16,'bold'), text="Error In L.R Price", bd=16 , anchor='w')
lb1Stockname.grid(row=2,column=8)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=lrerr,bd=10,
	insertwidth=10,bg='white',justify='right')
txtStockname.grid(row=2,column=9)

lb1Stockname = Label(f1,font=('arial',16,'bold'), text="S.V.M Prediction Price", bd=16 , anchor='w')
lb1Stockname.grid(row=3,column=8)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=svm,bd=10,
	insertwidth=10,bg='white',justify='right')
txtStockname.grid(row=3,column=9)


lb1Stockname = Label(f1,font=('arial',16,'bold'), text="Error In S.V.M Price", bd=16 , anchor='w')
lb1Stockname.grid(row=4,column=8)
txtStockname = Entry(f1,font=('arial', 16 ,'bold'), textvariable=svmerr,bd=10,
	insertwidth=10,bg='white',justify='right')
txtStockname.grid(row=4,column=9)



btnTotal=Button(f1,padx=5,pady=5,bd=5,fg="black",font=('arial',10,'bold'),
	text="PREDICT",bg="powder blue",command=ref).grid(row=900,column=1)
btnTotal=Button(f1,padx=5,pady=5,bd=5,fg="red",font=('arial',10,'bold'),
	text="BOLLINGER . BANDS",bg="black",command=bolli).grid(row=900,column=2)
btnTotal=Button(f1,padx=5,pady=5,bd=5,fg="black",font=('arial',10,'bold'),
	text="ASSISTANT",bg="powder blue",command=assis).grid(row=900,column=3)
btnTotal=Button(f1,padx=5,pady=5,bd=5,fg="black",font=('arial',10,'bold'),
	text="RECOMMENDATION",bg="powder blue",command=recomm).grid(row=900,column=4)





root.mainloop()