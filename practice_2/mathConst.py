#encoding utf-8
import math
constDict={"pi":math.pi,"e":math.e}
s=raw_input("enter math constant:precision\n ")
l=s.split(":")
for k in constDict:
    if l[0]==k:
        print(round(constDict[k],int(l[1])))

