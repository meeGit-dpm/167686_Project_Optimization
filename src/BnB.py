import sys

input = sys.stdin.readline
N, K = map(int, input().split())
d = [0] + list(map(int, input().split()))  
movement_cost = [list(map(int, input().split())) for _ in range(N + 1)]

best_time = float('inf')
best_routes = []

# Memoization
mem = {}

def DFS(unvisited, worker_routes, worker_times, cur_positions):
    global best_time, best_routes

    # Keep track of the state which has been solved
    key = (frozenset(unvisited), tuple(cur_positions))
    if key in mem and mem[key] <= max(worker_times):
        return
    else:
        mem[key] = max(worker_times)

    # Base case
    if not unvisited:
        total_times = [
            worker_times[k] + movement_cost[cur_positions[k]][0] if worker_routes[k] else 0
            for k in range(K)
        ]
        maximum_time = max(total_times)
        if maximum_time < best_time:
            best_time = maximum_time
            best_routes = [route + [0] for route in worker_routes]
        return

    # Recursion
    for nodes in list(unvisited):
        unvisited.remove(nodes)
        for k in range(K):
            last_pos = cur_positions[k]
            move_cost = movement_cost[last_pos][nodes]
            service_cost = d[nodes]
            total = worker_times[k] + move_cost + service_cost

            # Pruning
            if total >= best_time:
                continue

            # apply
            worker_routes[k].append(nodes)
            worker_times[k] += move_cost + service_cost
            cur_positions[k] = nodes

            DFS(unvisited, worker_routes, worker_times, cur_positions)

            # undo
            worker_routes[k].pop()
            worker_times[k] -= move_cost + service_cost
            cur_positions[k] = last_pos
        unvisited.add(nodes)
            
init_route = [[] for _ in range(K)]
init_time = [0] * K
init_pos = [0] * K
unvisited_customers = set(range(1, N + 1))

DFS(unvisited_customers, init_route, init_time, init_pos)

print(K)
for route in best_routes:
    route = [0] + route 
    print(len(route))
    print(*route)
