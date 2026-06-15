from ortools.sat.python import cp_model
import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())

    e = [0] * (N + 1)
    l = [0] * (N + 1)
    d = [0] * (N + 1)
    for i in range(1, N + 1):
        ei, li, di = map(int, input().split())
        e[i] = ei
        l[i] = li
        d[i] = di

    t = []
    for _ in range(N + 1):
        row = list(map(int, input().split()))
        t.append(row)

    max_time = max(l[1:N+1]) + max(d[1:N+1]) + max(
        t[i][j] for i in range(N+1) for j in range(N+1)
    )

    model = cp_model.CpModel()
    x = {}
    for i in range(N + 1):
        for j in range(N + 1):
            if i != j:
                x[i, j] = model.NewBoolVar(f"x[{i}][{j}]")
    start = [None] * (N + 1)
    start[0] = model.NewIntVar(0, 0, "start[0]")
    for i in range(1, N + 1):
        start[i] = model.NewIntVar(e[i], l[i], f"start[{i}]")
    arcs = []
    for i in range(N + 1):
        for j in range(N + 1):
            if i != j:
                arcs.append((i, j, x[i, j]))
    model.AddCircuit(arcs)
    M = max_time
    for i in range(N + 1):
        for j in range(1, N + 1):
            if i != j:
                model.Add(
                    start[j] >= start[i] + d[i] + t[i][j] - M * (1 - x[i, j])
                )
    total_travel = sum(
        t[i][j] * x[i, j]
        for i in range(N + 1)
        for j in range(N + 1)
        if i != j
    )
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 55.0
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        route = []
        current = 0
        visited = set([0])
        for _ in range(N):
            for j in range(1, N + 1):
                if j not in visited and solver.Value(x[current, j]) == 1:
                    route.append(j)
                    visited.add(j)
                    current = j
                    break
        print(N)
        print(" ".join(map(str, route)))
    else:
        unvisited = list(range(1, N + 1))
        route = []
        current = 0
        current_time = 0
        while unvisited:
            candidates = []
            for j in unvisited:
                arr = current_time + t[current][j]
                s = max(arr, e[j])
                if s <= l[j]:
                    candidates.append((s, j))
            if candidates:
                candidates.sort()
                _, best = candidates[0]
            else:
                best = min(unvisited, key=lambda j: t[current][j])
            arr = current_time + t[current][best]
            current_time = max(arr, e[best]) + d[best]
            current = best
            route.append(best)
            unvisited.remove(best)
        print(N)
        print(" ".join(map(str, route)))

solve()
