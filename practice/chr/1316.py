cnt = 0
for i in range(int(input())):
    word = input()
    cnt += list(word) == sorted(word, key=word.find)
print(cnt)

# sorted 에서 key=word.find 로 설정하면
# "a"부터 정렬되는것이 아니라,
# word 에서 찾아지는 character 순서대로 정렬된다. 
