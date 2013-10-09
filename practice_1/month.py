#encoding=utf-8
strMonth=raw_input("Enter some month: ")
strMonth=strMonth.lower()
s=""
monthDict={"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}
for k in monthDict:
    if strMonth==k:
        s=k
if s=="":
    print("This isn't a month")
else:
    print(monthDict[s])
