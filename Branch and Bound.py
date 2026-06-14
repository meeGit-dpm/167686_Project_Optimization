import sys
sys.setrecursionlimit(10**7)

N = int(input())

e = [0]*(N+1)
l = [0]*(N+1)
d = [0]*(N+1)

for i in range(1, N+1):
    e[i], l[i], d[i] = map(int, input().split())

t = [list(map(int, input().split())) for _ in range(N+1)]

best_cost = float('inf')
best_path = None

#cheapest_out[i] is the cheapest cost to go out from node i
cheapest_out = [float('inf')] * (N + 1)
for i in range(N+1):
    for j in range(N+1):
        if i != j:
            cheapest_out[i] = min(cheapest_out[i], t[i][j])

def dfs(cur, time, cost, path, unvisited):
    global best_cost, best_path

    # if all node are visited
    if not unvisited:
        if cost < best_cost:
            best_cost = cost
            best_path = path[:]
        return
    
    #prune according to lower bound
    #if sum(sum(cheapest cost[i] for i in unvisited), cost)  still bigger than the best_cost => prune
    lb = cost + cheapest_out[cur]
    for k in unvisited:
        lb += cheapest_out[k]
    if lb >= best_cost:
        return        

    # try all branches

    #the customer with the sooner deadline should be served first
    candidates = sorted(
        unvisited,
        key=lambda x: (l[x])                           
    )
    for j in candidates:
        arrive = time + t[cur][j]                     #the time in which workers arrive at the node
        start = max(arrive, e[j])                     #the time in which workers start doing his job (if he arrive too soon, he must wait)

        if start > l[j]:                              #if the worker arrive too late => prune
            continue

        #check whether there is any remaining customers that can't be served because of the deadline => prune
        feasible = True                              
        new_time = start + d[j]                       #the time when the worker just finish serving customer j
        for k in unvisited:
            if k != j and new_time > l[k]:            #j haven't been popped yet
                feasible = False
                break
        if not feasible:
            continue

        unvisited.remove(j)
        path.append(j)

        dfs(
            j,
            start + d[j],
            cost + t[cur][j],
            path,
            unvisited
        )

        path.pop()
        unvisited.add(j)


dfs(0, 0, 0, [], set(range(1, N+1)))

print(N)
print(*best_path if best_path else [])