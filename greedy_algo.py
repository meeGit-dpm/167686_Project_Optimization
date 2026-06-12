import sys
import math

def solve():
    def token_generator():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = token_generator()



    first_token = next(tokens)
    if not first_token:
        return
    
    N = int(first_token)
    
    e = [0] * (N + 1)
    l = [0] * (N + 1)
    d = [0] * (N + 1)
    
    for i in range(1, N + 1):
        token_e = next(tokens)
        token_l = next(tokens)
        token_d = next(tokens)
        
        if token_e is None or token_l is None or token_d is None:
            return
        e[i] = int(token_e)
        l[i] = int(token_l)
        d[i] = int(token_d)
        
    t = []
    for i in range(N + 1):
        row = []
        for j in range(N + 1):
            token_val = next(tokens)
            if token_val is None:
                return
            row.append(int(token_val))
        t.append(row)
        
    visited = [False] * (N + 1)
    path = []
    curr_node = 0  
    curr_time = 0  
    
    for _ in range(N):
        best_node = -1
        min_completion = math.inf
        
        feasible_candidates = []
        for v in range(1, N + 1):
            if not visited[v]:
                arrival = curr_time + t[curr_node][v]
                if arrival <= l[v]:
                    feasible_candidates.append(v)
                    
        if feasible_candidates:
            # Chon nguoi co the hoan thanh som nhat
            for v in feasible_candidates:
                arrival = curr_time + t[curr_node][v]
                start = max(arrival, e[v])
                completion = start + d[v]
                if completion < min_completion:
                    min_completion = completion
                    best_node = v
        else:
            # Neu khong co ung vien kha thi, chon khach hang co kha nang den som nhat
            min_arrival = float('inf')
            for v in range(1, N + 1):
                if not visited[v]:
                    arrival = curr_time + t[curr_node][v]
                    if arrival < min_arrival:
                        min_arrival = arrival
                        best_node = v
            if best_node != -1:
                arrival = curr_time + t[curr_node][best_node]
                start = max(arrival, e[best_node])
                min_completion = start + d[best_node]
                
        if best_node != -1:
            visited[best_node] = True
            path.append(best_node)
            curr_node = best_node
            curr_time = min_completion
        else:
            break
            
    print(N)
    print(" ".join(map(str, path)))

if __name__ == '__main__':
    solve()