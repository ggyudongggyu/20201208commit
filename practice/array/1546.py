time = int(input())
score = list(map(float, input().split()))
MAX = max(score)
new_score=[]
for i in range(time):
        x = score[i]/MAX * 100
        new_score.append(x)
y=sum(new_score) / len(new_score)
print("%.2f" %y)
