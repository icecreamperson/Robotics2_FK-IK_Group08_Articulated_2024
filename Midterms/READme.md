# ARTICULATED MANIPULATOR MIDTERM PROJECT BY GROUP 8 (MEXE 3201)

![1](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/f9601f29-9340-4d25-845e-4853257ebfad)
![ROBOTICS 2 MIDTERM PROJECT BY GROUP 8](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/06d08943-64bc-4cdc-8f13-886ea41e0ca0)


![5](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/285f252a-e5fa-41ea-827a-23effbaafe6e)
![ROBOTICS 2 MIDTERM PROJECT BY GROUP 8 (4)](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/ee88b38a-1fd9-41a8-b927-4605469190f7)


![3](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/bee97a23-9b91-4deb-b297-95bde5317030)


![4](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/6d558b9f-ee97-4c1d-b199-724d5ef12b76)
## Link for Task 1 
### : https://drive.google.com/file/d/1pcPDunTcaHPL8EHjLOVDfUVcWlLeAxsG/view?usp=drive_link


![5](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/b03ab935-da5f-4c57-9002-fa0c3f66ffb1)
## Link for Task 2 
### : https://drive.google.com/file/d/1-NiTzMYp4pNwU4eMX4EKbJMV1eX-IWif/view?usp=drive_link


![6](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/9778e7b2-c035-46d7-a883-5590818f5b7d)
## Link for Task 3 
### : https://drive.google.com/file/d/1FBTull5baPmBD6tbocNk8-yk4RmCKwyk/view?usp=drive_link


![7](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/18cb0a23-d80e-436c-9926-0f846209fe27)
## Link for Task 4 
### : https://drive.google.com/file/d/1GVMg8_DskSPzaUSE8biwdKrL2brmhsvi/view?usp=drive_link


![8](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/db2d65f1-2233-4709-bac6-6407e5a52eee)
## Link for Task 5
### : https://drive.google.com/file/d/1fsB76JGAQz2QJ551aGj3O9OhLXT0w0Nw/view?usp=drive_link
												
# CODES OF THE GUI
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


												
## I. ABSTRACT OF THE PROJECT
![9](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/91171d92-ecea-4506-a5f4-b947260d5e35)
![ROBOTICS 2 MIDTERM PROJECT BY GROUP 8 (1)](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/08f4696e-ac8b-4a9a-82b8-9e9b600ea1a5)

    
## II. INTRODUCTION OF THE PROJECT	
![10](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/35ea723d-ddcb-4a21-abd9-e17e63ef9606)
![1](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/1db9851a-6527-4004-b384-c029f8b00342)


## III. DEGREES OF FREEDOM OF ARTICULATED MANIPULATOR DESCRIPTION AND COMPUTATION
![2](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/742eaef0-7ddd-4e0e-bf1e-e84ba9866207)
![3](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/36ee02af-68a7-44b4-bdaa-92a644d69edd)
 ![1](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/b611dfde-fdc7-4a3e-bbd8-049e6d636cfd)

## IV. KINEMATIC AND D-H FRAME ASSIGNMENT OF ARTICULATED MANIPULATOR DESCRIPTION AND COMPUTATION
![4](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/371ebb74-ebba-41c1-8181-64a132a2b19a)
![5](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/d550dcd1-4a99-4796-bd1d-44eba5d50100)
![6](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/d18f628d-06e6-4cf8-937a-243339590d05)
![2](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/a8454bbf-d675-4ec5-8c13-13815c792751)



## V. D-H PARAMETRIC TABLE OF ARTICULATED MANIPULATOR DESCRIPTION AND COMPUTATION
![7](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/2a3e76b9-ca02-42e6-be0c-232491c8302d)
![8](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/7f28ac75-80f9-4812-875f-d06561b89c07)
![3](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/81e9571f-814b-4b91-a03d-368278af45e7)

## VI. HOMOGENEOUS TRANSFORMATION MATRIX (HTM) OF ARTICULATED MANPULATOR DESCRIPTION AND COMPUTATION 
![9](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/82ca5cc6-e4d2-4eb5-91fd-2690694323eb)
![1](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/bcf42127-0c4f-49e8-b744-b851112d8fe0)

## VII. INVERSE KINEMATICS OF ARTICULAATED MANIPULATOR DESCRIPTION AND COMPUTATION 
![10](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/29c36577-85c2-4ac9-b868-175aadc22f8a)
![2](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/29e9d60b-eeb0-47f7-9069-27cd76403ec8)


## VIII. FORWARD AND INVERSE KINEMATICS GUI CALCULATOR OF ARTICULATED MANIPULATOR DESCRIPTION AND COMPUTATION 
![11](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/5a3781c9-98f6-4011-aca8-4a6b60988d85)
![ROBOTICS 2 MIDTERM PROJECT BY GROUP 8 (2)](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/b5b7a600-2c23-478d-85eb-aa00fdf7df1d)
![6](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/82c190b6-cdbd-4523-aa82-c48ee353402d)

# WRITTEN COMPUTATIONS

![431955874_311135385069916_189506793963735804_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/6fd234ce-42cc-4fbf-8490-9f0f2c9a5d7f)

![431818087_478293414527927_7807894219660866390_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/06ae6289-35e9-44a2-a477-9e07e197cb8f)

![432066222_830165592275627_2153396339024100678_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/f6f7e88f-641e-4cb9-aa07-30fab33998b7)

![431765965_1185118899179360_2880107292439594602_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/1986d28c-7f88-4c95-9c59-c7bb03549f9b)

![431914302_408057295172993_1094853825774276709_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/fe967c03-6d42-4fdf-af0a-a501ef4c7cb7)

![431929678_794587359237064_3604829832495344217_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/56cd008f-ed06-4b6d-8b96-b74f2b888048)

![431850797_328834029820854_5317256990933375396_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/eeb89f9c-a92f-4c7c-b769-8c8b967a8884)

![431764006_1096476241650452_9187984347851031875_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/d3b0bac2-88f3-4bcf-89c7-8e045e7cde35)

![431825598_440803234972364_7780528952483554656_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/02e66ab3-76f6-4ff5-a6fb-61fb3e552fb2)

![431820687_452620737166863_2560586139871265957_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/21512d2a-fa8d-4145-bdad-4658019d808d)

![431781067_943960330786786_5572433538421729061_n](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157708843/dd1a789f-79ff-4fc0-8cb0-9cc86566a14f)


## CONCLUSION
![ROBOTICS 2 MIDTERM PROJECT BY GROUP 8 (3)](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/7d2b3ee6-0376-48dd-85dc-65336ba8a129)

## IX. REFERENCES												
![12](https://github.com/icecreamperson/Robotics2_FK-IK_Group08_Articulated_2024/assets/157493649/9fa1e425-b89d-46b8-bfab-116a9f5da215)
https://images.app.goo.gl/5dayrQQEUJ8dkd6m6
