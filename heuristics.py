import random
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
d = [0] + list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N + 1)]

def compute_max_time(routes):
    max_time = 0
    for route in routes:
        if len(route) <= 2:
            continue
        time = 0
        # Tinh thoi gian hanh trinh cua ky thuat vien
        for i in range(len(route) - 1):
            time += matrix[route[i]][route[i+1]]
            if i > 0:  # Tinh thoi gian dich vu cho khach hang (khong ke khoi dau)
                time += d[route[i]]
        max_time = max(max_time, time)
    return max_time

# Khoi tao lan can
def try_neighbor_swap(routes, best_cost):
    a, b = random.sample(range(K), 2)
    if len(routes[a]) > 2 and len(routes[b]) > 2:
        i = random.randint(1, len(routes[a]) - 2)
        j = random.randint(1, len(routes[b]) - 2)
        
        # Hoan doi 2 khach hang
        routes[a][i], routes[b][j] = routes[b][j], routes[a][i]
        cost = compute_max_time(routes)
        
        if cost < best_cost:
            return cost
        # Hoan doi lai neu khong tot hon
        routes[a][i], routes[b][j] = routes[b][j], routes[a][i]
    return best_cost

def try_neighbor_swap_multiple(routes, best_cost, num_nodes=2):
    a, b = random.sample(range(K), 2)
    if len(routes[a]) - 2 >= num_nodes and len(routes[b]) - 2 >= num_nodes:
        idx_a = random.sample(range(1, len(routes[a]) - 1), num_nodes)
        idx_b = random.sample(range(1, len(routes[b]) - 1), num_nodes)
        
        # Hoan doi nhieu khach hang cung luc
        for i in range(num_nodes):
            routes[a][idx_a[i]], routes[b][idx_b[i]] = routes[b][idx_b[i]], routes[a][idx_a[i]]
            
        cost = compute_max_time(routes)
        if cost < best_cost:
            return cost
            
        # Quay lai neu khong tot hon
        for i in range(num_nodes):
            routes[a][idx_a[i]], routes[b][idx_b[i]] = routes[b][idx_b[i]], routes[a][idx_a[i]]
    return best_cost

def try_neighbor_move(routes, best_cost):
    a, b = random.sample(range(K), 2)
    if len(routes[a]) > 2:
        i = random.randint(1, len(routes[a]) - 2)
        customer = routes[a].pop(i)
        j = random.randint(1, len(routes[b]) - 1)
        routes[b].insert(j, customer)
        
        cost = compute_max_time(routes)
        if cost < best_cost:
            return cost
            
        # Quay lai neu khong tot hon
        routes[b].pop(j)
        routes[a].insert(i, customer)
    return best_cost

# Khoi tao bang thuat toan tham lam
def greedy():
    technicians = [{'route': [0], 'work': 0} for _ in range(K)]
    visited = [False] * (N + 1)
    visited[0] = True

    customers = list(range(1, N + 1))
    random.shuffle(customers)

    for _ in range(N):
        best_cost = float('inf')
        best_tech = -1
        best_cust = -1

        for cust in customers:
            if visited[cust]:
                continue
            for k in range(K):
                last_node = technicians[k]['route'][-1]
                cost = technicians[k]['work'] + matrix[last_node][cust] + d[cust]
                if cost < best_cost:
                    best_cost = cost
                    best_tech = k
                    best_cust = cust

        if best_tech != -1:
            technicians[best_tech]['route'].append(best_cust)
            technicians[best_tech]['work'] += matrix[technicians[best_tech]['route'][-2]][best_cust] + d[best_cust]
            visited[best_cust] = True

    for tech in technicians:
        tech['route'].append(0)

    return [tech['route'] for tech in technicians]

# Vong lap chinh cua thuat toan leo doi
def hill_climbing(routes, max_iter=20000):
    best_cost = compute_max_time(routes)

    for _ in range(max_iter):
        # Duyet cac loai lan can va chon lan can tot nhat
        old_cost = best_cost
        
        best_cost = try_neighbor_swap(routes, best_cost)
        if best_cost < old_cost: continue
        
        best_cost = try_neighbor_swap_multiple(routes, best_cost)
        if best_cost < old_cost: continue
        
        best_cost = try_neighbor_move(routes, best_cost)
        
    return routes

init_routes = greedy()
improved_routes = hill_climbing(init_routes)

print(K)
for route in improved_routes:
    print(len(route))
    print(" ".join(map(str, route)))