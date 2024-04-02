from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
from PIL import Image
from PIL import Image, ImageTk


gui =  Tk()
gui.title("ARTICULATED Design Calculator")
gui.resizable(False,False)
gui.config(bg="grey")

image = PhotoImage(file="C:/Users/Dan/Documents/ArticulatedImage.png")
image_label = Label(gui, image=image)
image_label.grid(row=3, column=0, columnspan=5, padx=10, pady=10)









def reset():
    a1_E.delete(0, END)
    a2_E.delete(0, END)
    a3_E.delete(0, END)

    th1_E.delete(0, END)
    th2_E.delete(0, END)
    th3_E.delete(0, END)

    X_E.delete(0, END)
    Y_E.delete(0, END)
    Z_E.delete(0, END)

def f_k():

    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())
    
    def mm_to_meter(a):
        m = 1000
        return a/m

    a1 = mm_to_meter(a1)
    a2 = mm_to_meter(a2) 
    a3 = mm_to_meter(a3)  

    T1 = float(th1_E.get()) 
    T2 = float(th2_E.get()) 
    T3 = float(th3_E.get()) 

    T1 = (T1/180.0)*np.pi
    T2 = (T2/180.0)*np.pi
    T3 = (T3/180.0)*np.pi

    PT = [[T1,(90.0/180.0)*np.pi,0,a1],
          [T2,(0.0/180.0)*np.pi,a2,0],
          [T3,(0.0/180.0)*np.pi,a3,0]]

    i = 0
    H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]

    i = 1
    H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]

    i = 2
    H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
            [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
            [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
            [0,0,0,1]]
    
    H0_1= np.array(H0_1)
    H1_2= np.array(H1_2)
    H2_3= np.array(H2_3)

    H0_2 = np.dot(H0_1,H1_2)
    H0_3 = np.dot(H0_2,H2_3)

    X0_3 = H0_3[0,3]
    X_E.delete(0,END)
    X_E.insert(0,np.around(X0_3,3))
    Y0_3 = H0_3[1,3]
    Y_E.delete(0,END)
    Y_E.insert(0,np.around(Y0_3,3))
    Z0_3 = H0_3[2,3]
    Z_E.delete(0,END)
    Z_E.insert(0,np.around(Z0_3,3))
   
    ARTICULATED = DHRobot([
        RevoluteDH(a1,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a2,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a3,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2])
        ], name="ARTICULATED")
    
    print(ARTICULATED)
    ARTICULATED.teach(q=[T1, T2, T3])


def i_k():
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())

    def mm_to_meter(a):
        m = 1000
        return a/m

    a1 = mm_to_meter(a1)
    a2 = mm_to_meter(a2) 
    a3 = mm_to_meter(a3)  

    xe = float(X_E.get())
    ye = float(Y_E.get())
    ze = float(Z_E.get())

    if xe == 0:
        Th1 = (np.pi/2) * 180/np.pi if ye > 0 else (-np.pi/2) * 180/np.pi
    else:
        Th1 = np.arctan(ye/xe) * 180/np.pi #1

    r1 = np.sqrt(ye**2 + xe**2) #2
    r2 = ze - a1 #3

    if r1 == 0:
        phi1 = np.pi/2 if r2 > 0 else - np.pi/2
    else:
        phi1 = np.arctan(r2/r1) #4
    r3 = np.sqrt(r2**2 + r1**2) #5

    phi2 = np.arccos(np.clip((a3**2-a2**2-r3**2)/(-2*a2*r3),-1,1)) #6

    Th2 = (phi1 + phi2) * 180/np.pi #7

    phi3 =  phi3 = np.arccos(np.clip((r3**2-a2**2-a3**2)/(-2*a2*a3),-1,1)) #8

    Th3 = (phi3-np.pi) * 180/np.pi #9


    th1_E.delete(0,END)
    th1_E.insert(0,np.around(Th1,3))

    th2_E.delete(0,END)
    th2_E.insert(0,np.around(Th2,3))

    th3_E.delete(0,END)
    th3_E.insert(0,np.around(Th3,3))

    ARTICULATED = DHRobot([
        RevoluteDH(a1,0,(90.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a2,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
        RevoluteDH(0,a3,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2])
        ], name="ARTICULATED")
    
    print(ARTICULATED)
    ARTICULATED.teach(q=[Th1, Th2, Th3])


FI = LabelFrame(gui, text="    Link Lengths and Joint Variables    ", font=("Helvetica", 12, "bold"), bd=0)

FI.grid(row=0, column=0, padx=10, pady=10, sticky=N+W)

a1 = Label(FI, text="a1 =",font=(10))
a1_E = Entry(FI,width=5,font=(10))
cm1 = Label(FI,text=("cm"),font=(10))

a2 = Label(FI,text=("a2 = "),font=(10))
a2_E = Entry(FI,width=5,font=(10))
cm2 = Label(FI,text=("cm"),font=(10))

a3 = Label(FI,text=("a3 = "),font=(10))
a3_E = Entry(FI,width=5,font=(10))
cm3 = Label(FI,text=("cm"),font=(10))

a1.grid(row=0,column=0)
a1_E.grid(row=0,column=1)
cm1.grid(row=0,column=2)

a2.grid(row=1,column=0)
a2_E.grid(row=1,column=1)
cm2.grid(row=1,column=2)

a3.grid(row=2,column=0)
a3_E.grid(row=2,column=1)
cm3.grid(row=2,column=2)

th1 = Label(FI, text="th1 =",font=(10))
th1_E = Entry(FI,width=5,font=(10))
deg1 = Label(FI,text=("deg"),font=(10))

th2 = Label(FI, text="th2 =",font=(10))
th2_E = Entry(FI,width=5,font=(10))
deg2 = Label(FI,text=("deg"),font=(10))

th3 = Label(FI, text="th3 =",font=(10))
th3_E = Entry(FI,width=5,font=(10))
deg3 = Label(FI,text=("deg"),font=(10))

th1.grid(row=0,column=3)
th1_E.grid(row=0,column=4)
deg1.grid(row=0,column=5)

th2.grid(row=1,column=3)
th2_E.grid(row=1,column=4)
deg2.grid(row=1,column=5)

th3.grid(row=2,column=3)
th3_E.grid(row=2,column=4)
deg3.grid(row=2,column=5)

BF = LabelFrame(gui,text="    Forward & Inverse Kinematics    ",font=("Helvetica", 12, "bold"), bd=0)
BF.grid(row=1, column=0, padx=10, pady=10, sticky=NW,)

FK = Button(BF,text="Forward",font=(10),bg="black",fg="pink", command = f_k)
rst= Button(BF,text="Reset",font=(10),bg="green",fg="blue", command = reset)
IK = Button(BF,text="Inverse",font=(10),bg="yellow",fg="red", command = i_k)

FK.grid(row=0,column=0,columnspan=2,padx=10, pady=10)
rst.grid(row=0,column=2,padx=10,pady=10)
IK.grid(row=0,column=3,padx=10,pady=10)

PV = LabelFrame(gui,text="Position Vectors",font=("Helvetica", 12, "bold"), bd=0)
PV.grid(row=2,column=0)

X = Label(PV,text=("X = "),font=(10))
X_E = Entry(PV,width=5,font=(10))
cm4 = Label(PV,text=("cm"),font=(10))

Y = Label(PV,text=("Y = "),font=(10))
Y_E = Entry(PV,width=5,font=(10))
cm5 = Label(PV,text=("cm"),font=(10))

Z = Label(PV,text=("Z = "),font=(10))
Z_E = Entry(PV,width=5,font=(10))
cm6 = Label(PV,text=("cm"),font=(10))

X.grid(row=0,column=0)
X_E.grid(row=0,column=1)
cm4.grid(row=0,column=2)

Y.grid(row=1,column=0)
Y_E.grid(row=1,column=1)
cm5.grid(row=1,column=2)

Z.grid(row=2,column=0)
Z_E.grid(row=2,column=1)
cm6.grid(row=2,column=2)


gui.mainloop()
