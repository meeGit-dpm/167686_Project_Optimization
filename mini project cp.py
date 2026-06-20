from ortools.sat.python import cp_model
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
d = [0] + list(map(int, input().split()))
matrix = []
for _ in range(N + 1):
    matrix.append(list(map(int, input().split())))

def routing():
    model = cp_model.CpModel()
    x = {}
    for k in range(1, K + 1):
        for i in range(N + 1):
            for j in range(N + 1):
                if i != j:
                    x[i, j, k] = model.NewBoolVar(f"x[{i}][{j}][{k}]")

    UB = N * max(matrix[i][j] for i in range(N+1) for j in range(N+1) if i != j) + sum(d)

    y = {}
    for k in range(1, K + 1):
        y[k] = model.NewIntVar(0, UB, f"y[{k}]")

    self_loop = {}
    for k in range(1, K + 1):
        for i in range(1, N + 1):
            self_loop[i, k] = model.NewBoolVar(f"sl[{i}][{k}]")

    z = model.NewIntVar(0, UB, "z")
    for j in range(1, N + 1):
        model.Add(sum(x[i, j, k] for k in range(1, K + 1) for i in range(N + 1) if i != j) == 1)

    for j in range(1, N + 1):
        for k in range(1, K + 1):
            model.Add(sum(x[i, j, k] for i in range(N + 1) if i != j) + self_loop[j, k] == 1)

    for k in range(1, K + 1):
        arcs = []
        for i in range(1, N + 1):
            arcs.append((i, i, self_loop[i, k]))
        for i in range(N + 1):
            for j in range(N + 1):
                if i != j:
                    arcs.append((i, j, x[i, j, k]))
        model.AddCircuit(arcs)

    for k in range(1, K + 1):
        total = []
        for i in range(N + 1):
            for j in range(N + 1):
                if i != j:
                    cost = matrix[i][j]
                    service = d[j] if j != 0 else 0
                    total.append(x[i, j, k] * (cost + service))
        model.Add(y[k] == sum(total))

    for k in range(1, K + 1):
        model.Add(z >= y[k])
    model.Minimize(z)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 100.0
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(K)
        for k in range(1, K + 1):
            current = 0
            route = [0]
            visited = set()
            while True:
                found = False
                for j in range(N + 1):
                    if current != j and solver.Value(x[current, j, k]) == 1:
                        route.append(j)
                        visited.add(j)
                        current = j
                        found = True
                        break
                if not found or current == 0:
                    break
            if route[-1] != 0:
                route.append(0)
            print(len(route))
            print(" ".join(map(str, route)))
    else:
        print("NO_SOLUTION")

routing()
