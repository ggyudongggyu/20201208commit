year = int(input())
if (year<1 or year>4000):
    print("Error")
elif( year%4==0 and year%100!=0) or year%400==0:
    print("1")
else:
    print("0")
