import random

N = 17

def CheckSort(a,n):
    Sorted = True
    for i in range(n):
        if a[i] > a[i+1]:
            Sorted = False
        if not Sorted:
            break
    if Sorted: print('정렬 완료')
    else: print('정렬 오류')

def ShellSort(a, n) :
    h = 1
    while h<n:
        h = h*3 + 1
    while h>0:  # h=13 / 4
        for i in range(h+1, n+1): #14, 15 / 5,15
            v = a[i]        #v=a[14] / a[6]
            j = i           #j=14    /  6
            while j>h and a[j-h]>v: #14>13 and a[1] 14 > a[14] 1 / 6>4 and a[2]>a[6]
                a[j] = a[j-h] # a[14]자리에 a[1] 값 넣기
                j -= h #j = 14-13 = 1
            a[j] = v #a[1]자리에 a[14]값 넣기 : 교환 완료 (while문 안돌면 a[5]=a[5]처럼 걍 그대로임.)
        h//=3

def main():
    a=[random.randint(1,50) for i in range(0, N+1)]
    a[0]=-1
    print(a)
    ShellSort(a,N)
    CheckSort(a,N)
    print(a)

if __name__=='__main__':
    main()
