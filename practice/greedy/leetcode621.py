import collections
tasks = ["A","A","A","C","B","D"]
n =2
def solution(tasks, n):
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        print("most common : ", counter.most_common(n+1))
        for task, _ in counter.most_common(n+1):
            sub_count += 1
            result += 1
            counter.subtract(task)

            counter += collections.Counter()
        if not counter:
            break
        print(result)
        print(sub_count)
        result += n - sub_count + 1 
    return result
print(solution(tasks, n))

# print(counter.most_common(3))