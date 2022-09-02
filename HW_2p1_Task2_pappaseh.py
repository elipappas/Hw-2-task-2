# Assignment Title (include Task number if applicable)
# File: HW_2p1_Task2_pappaseh.py
# Date:    25 January 2022
# By:      Eli Pappas
# Section: 013
# Team:    181
# 
# ELECTRONIC SIGNATURE
# Eli Pappas
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
import math
data = open("/Users/elipappas/Downloads/Refraction.txt")
lines = data.readlines()
n1 = []
theta1 = []
n2 = []
theta2 = []

for i in range(len(lines)):
    splitData = lines[i].split()
    n1.append(splitData[0])
    theta1.append(splitData[1])
    n2.append(splitData[2])

n1.remove(n1[0])
theta1.remove(theta1[0])
n2.remove(n2[0])
for x in range(len(n1)):
    thetaD = (float(theta1[x])*math.pi)/180
    arcSin = (float(n1[x])*math.sin(thetaD))/float(n2[x])
    theta2.append(math.asin(arcSin))
    
file = open("HW_2p1_Task2.txt ", "w")
file.write("n1   theta1   n2   theta2"+"\n")
for x in range(len(n1)):
    rn1 = round(float(n1[x]),1)
    rtheta1 = round(float(theta1[x]),1)
    rn2 = round(float(n2[x]),1)
    rtheta2 = round(((float(theta2[x])*180)/math.pi),1)
    print(rtheta2)
    file.write(str(rn1)+"   "+str(rtheta1)+"   "+str(rn2)+"   "+str(rtheta2)+"\n")

file.close()

