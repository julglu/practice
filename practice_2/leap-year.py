#encoding utf-8
reply=raw_input("Enter some year: ")
try:
    year=int(reply)
except:
    print("This isn't a year")
else:
    if year%4==0 and year%100!=0:
        print("This a leap-year")
    else:
        if year%400==0:
            print("This is a leap-year")
        else:
            print("It isn't a leap-year")
