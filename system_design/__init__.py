edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]

connections = dict()

for v1, v2 in edges:
    connections[v1] = v2
    connections[v2] = v1

print(len(connections.keys()))
print(connections)
print(connections.copy())