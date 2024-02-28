import numpy as np
import math

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

xe = float(input("X = "))
ye = float(input("Y = "))
ze = float(input("Z = "))

if xe == 0:
    Th1 = (np.pi/2) * 180/np.pi if ye > 0 else -np.pi/2
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

print("Th1 = ", np.around(Th1,3))

print("Th2 = ", np.around(Th2,3))

print("Th3 = ", np.around(Th3,3))
