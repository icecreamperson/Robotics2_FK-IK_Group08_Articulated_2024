import numpy as np
import math

#Inverse Kinematics Using Graphical Method

#link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

#Position Vector in mm
xe = float(input("X = "))
ye = float(input("Y = "))
ze = float(input("Z = "))

Th1 = np.arctan(ye/xe) #1
r1 = np.sqrt(ye**2 + xe**2) #2
r2 = ze - a1 #3
phi1 = np.arctan(r2/r1) #4

r3 = np.sqrt(r2**2 - r1**2) #5
phi2 = np.arccos((a3**2-a2**2-r2**2)/(-2*a2*r3)) #6

Th2 = (phi1 + phi2) * 180/np.pi #7

phi3 =  np.arccos((r3**2-a2**2-a3**2)/(-2*a2*a3)) #8

Th3 = (phi3*180/np.pi) - 180 #9

print("Th1 = ", np.around(Th1,3))

print("Th2 = ", np.around(Th2,3))

print("Th3 = ", np.around(Th3,3))