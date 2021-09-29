adj_list = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["B", "F"],
    "D" : [],
    "E" : ["F"],
    "F" : []
}

color = {}  # W, G, B By default every vertex will be white, then when its first visited,
# it will be G and once all of its neighbors are explored it will turn B

parent = {}
travel_time = {}  # [start, end] start will be when the color turns G and it will end when it turns B
dfs_traversal_output = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    travel_time[node] = [-1, -1]

time = 0
def dfs(u):
    global time
    color[u] = "G"
    travel_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs(v)

    color[u] = "B"
    travel_time[u][1] = time
    time += 1

dfs("A")
print(dfs_traversal_output)