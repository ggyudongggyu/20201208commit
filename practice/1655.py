def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr

case  = int(input())
list = []
res = []
x = int(input())
list.append(x)
res.append(x)
for i in range(case-1):
    list.append(int(input()))
    list = quick_sorted(list)
    if len(list)%2==0:
        res.append(list[len(list)//2 - 1])
    else:
        res.append(list[len(list)//2])

for i in res:
    print(i)
