import math

def solve():
    N = int(input())
    
    e = [0] * (N + 1)  # Mo cua
    l = [0] * (N + 1)  # Dong cua
    d = [0] * (N + 1)  # Gio phuc vu
    
    for i in range(1, N + 1):
        line = input().split()
        e[i] = int(line[0])
        l[i] = int(line[1])
        d[i] = int(line[2])
        
    t = []
    for i in range(N + 1):
        row = list(map(int, input().split()))
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
            for v in feasible_candidates:
                arrival = curr_time + t[curr_node][v]
                start_service = max(arrival, e[v])
                completion = start_service + d[v]
                
                if completion < min_completion:
                    min_completion = completion
                    best_node = v
        else:
            min_arrival = math.inf
            for v in range(1, N + 1):
                if not visited[v]:
                    arrival = curr_time + t[curr_node][v]
                    if arrival < min_arrival:
                        min_arrival = arrival
                        best_node = v
                        
            if best_node != -1:
                arrival = curr_time + t[curr_node][best_node]
                start_service = max(arrival, e[best_node])
                min_completion = start_service + d[best_node]
                
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