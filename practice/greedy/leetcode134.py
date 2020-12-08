gas = [1,2,3,4,5]
cost = [3,1,8,1,2]

def solution(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    start , fuel = 0, 0
    for i in range(len(gas)):
        if gas[i] + fuel < cost[i]:
            start = i+1
            fuel = 0 
        else:
            fuel += gas[i] - cost[i]
    return start
            
print(solution(gas, cost))