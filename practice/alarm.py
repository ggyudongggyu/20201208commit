h,m = map(int, input().split())
if (h<0 or h>24 or m<0 or m>60):
    print("Error")

if m>=45:
    mm=m-45
    print(str(h)+" "+str(mm))
else:
    hh=h-1
    if hh<0:
        hh=hh+24
    mmm=m+15
    print(str(hh)+" "+str(mmm))
