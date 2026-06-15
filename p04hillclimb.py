import random
import sys
import copy

input = sys.stdin.readline
e = [0]
l = [0]
d = [0]
K = int(input())
for _ in range(K):
    a, b, c = map(int, input().split())
    e.append(a)
    l.append(b)
    d.append(c)
matrix = [list(map(int, input().split())) for _ in range(K + 1)]

# Min route time 
def compute_time(customers):
    time = 0
    current_pos = 0
    total_time = 0
    for next_pos in customers: 
        time += matrix[current_pos][next_pos]
        total_time += matrix[current_pos][next_pos]

        if time < e[next_pos]:
            time = e[next_pos]
        if time > l[next_pos]:
            time = float('inf')
        
        time += d[current_pos]
        current_pos = next_pos

    total_time += matrix[current_pos][0]
        
    return total_time

# Neighborhood operators 
def generate_neighbor_swap(route):
    new_route = list(route)
    if len(new_route) >= 2:
        i, j = random.sample(range(len(new_route)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def generate_neighbor_move(route):
    new_route = list(route)
    if len(new_route) >= 2:
        i = random.randint(0, len(new_route) - 1)
        customer = new_route.pop(i)
        j = random.randint(0, len(new_route))
        new_route.insert(j, customer)
    return new_route
# Greedy initialization
def greedy():
    route = []
    visited = [False] * (K + 1)
    visited[0] = True

    current_node = 0
    current_time = 0
        
    for _ in range(K):
        candidates = []
        for nxt in range(1, K + 1):
            if not visited[nxt]:
                arr_time = current_time + matrix[current_node][nxt]
                if arr_time <= l[nxt]: 
                    candidates.append((arr_time, nxt))

    
        if not candidates:
            remaining = [i for i in range(1, K + 1) if not visited[i]]
            random.shuffle(remaining)
            route.extend(remaining)
            return route

        
        candidates.sort()
        chosen_node = candidates[0][1]

        route.append(chosen_node)
        visited[chosen_node] = True
        
        
        arr_time = current_time + matrix[current_node][chosen_node]
        current_time = max(arr_time, e[chosen_node]) + d[chosen_node]
        current_node = chosen_node

    return route

# Hill Climbing
def hill_climbing(routes, max_iter=10000):
    best_routes = routes
    best_cost = compute_time(routes)

    for _ in range(max_iter):
        # Try Swap
        neighbor = generate_neighbor_swap(best_routes)
        cost = compute_time(neighbor)
        if cost < best_cost:
            best_routes, best_cost = neighbor, cost
            continue

        # Try Move
        neighbor = generate_neighbor_move(best_routes)
        cost = compute_time(neighbor)
        if cost < best_cost:
            best_routes, best_cost = neighbor, cost
            continue

    return best_routes

init_routes = greedy()
improved_routes = hill_climbing(init_routes)

print(K)
print(" ".join(map(str, improved_routes)))