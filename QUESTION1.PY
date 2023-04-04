#RAMANDEEP SINGH
#22076
p = int(input ("Enter the month in the numeric form "))
q = int(input ("Enter the day in numeric form "))
r = int(input ("Enter the year as two numerical digits"))
t=1

if p >0 and p <=12:
    t = 1
else:
    d=0


if q >0 and q <=31:
    t = 1
else:
    t=0
    
if r >0 and r <=99:
    t = 1
else:
    t=0

if t == 0:
    print("invalid date")
else:
    print("the date is",p,"/",q,"/",r)
    print("Success: Congratulations! you entered the correct date.")


