import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    N, K = int(input_data[0]), int(input_data[1])
    d = [0] + [int(x) for x in input_data[2:2+N]]
    t = []
    idx = 2 + N
    for _ in range(N + 1):
        row = [int(x) for x in input_data[idx : idx + N + 1]]
        t.append(row)
        idx += N + 1

    # K tuyen duong bat dau va ket thuc tai depot (0)
    routes = [[0, 0] for _ in range(K)]
    costs = [0] * K

    # Xep khach hang thoi gian giam dan  (khoang cach toi depot + thoi gian dich vu)
    customers = sorted(range(1, N + 1), key=lambda u: -(t[0][u] + d[u]))

    for u in customers:
        best_k, best_pos, min_new_cost = -1, -1, float('inf')
        for k in range(K):
            r = routes[k]
            for i in range(1, len(r)):
                #Chen u vao giua 2 dia diem
                prev, nxt = r[i-1], r[i]
                added_cost = - t[prev][nxt] + t[prev][u] + d[u] + t[u][nxt]
                new_cost = costs[k] + added_cost
                if new_cost < min_new_cost:
                    min_new_cost = new_cost
                    best_k = k
                    best_pos = i
        
        # Chèn khách hàng vào vị trí tối ưu nhất tìm được
        routes[best_k].insert(best_pos, u)
        costs[best_k] = min_new_cost

    # In kết quả
    print(K)
    for r in routes:
        print(len(r))
        print(*(r))

if __name__ == '__main__':
    solve()