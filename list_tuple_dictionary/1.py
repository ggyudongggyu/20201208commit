fruit =["딸기","사과","바나나","복숭아","키위","복숭아","복숭아","사과","바나나"]

d={}

for f in fruit:
                    #f에는 fruit 안에 있는 애가 하나씩 차례로 들어가는 자리
    if f in d:      #"f"라는 key 가 d 라는 딕셔너리에 들어있어?
        d[f]= d[f]+1
    else:
        d[f] = 1    #f 에 들어있는 key가 아직 딕셔너리에 한 번도 들어가지 않았던 애라면 1부터 세줘야하니까
print(d)