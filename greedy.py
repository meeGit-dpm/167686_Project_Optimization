import sys

#992

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])

    #Thoi gian bao tri
    d = [0] + [int(x) for x in input_data[2:2+N]]

    t = []
    idx = 2 + N
    for _ in range(N + 1):
        row = [int(x) for x in input_data[idx : idx + N + 1]]
        t.append(row)
        idx += N + 1

    routes = [[0] for _ in range(K)]
    current_time = [0] * K  
    current_pos = [0] * K   
    unvisited = set(range(1, N + 1))  

    while unvisited:
        #Tim nhan vien co thoi gian tich luy nho nhat
        best_k = -1
        min_time = float('inf')
        for k in range(K):
            if current_time[k] < min_time:
                min_time = current_time[k]
                best_k = k

        #Tim khach hang chua tham gan best_k nhat
        pos = current_pos[best_k]
        best_u = -1
        min_cost = float('inf')
        
        for u in unvisited:
            cost = t[pos][u] + d[u]
            if cost < min_cost:
                min_cost = cost
                best_u = u

        routes[best_k].append(best_u)
        current_time[best_k] += t[pos][best_u] + d[best_u]
        current_pos[best_k] = best_u
        unvisited.remove(best_u)

    #Nhan vien quay ve diem xuat phat
    for k in range(K):
        pos = current_pos[k]
        routes[k].append(0)
        current_time[k] += t[pos][0]

    print(K)
    for k in range(K):
        print(len(routes[k]))
        print(*(routes[k]))

if __name__ == '__main__':
    solve()