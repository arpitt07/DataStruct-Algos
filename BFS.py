from queue import Queue

adj_list = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["a"]
}

visited = {}
level = {}
parent = {}
bfs_travel_output = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1  # inf

#initialize the start node
source = "a"
visited[source] = True
level[source] = 0
queue.put(source)

while not queue.empty():
   u = queue.get()
   bfs_travel_output.append(u)

   for v in adj_list[u]:
      if not visited[v]:
         visited[v] = True
         parent[v] = u
         level[v] = level[u] + 1
         queue.put(v)

# code to find shortest path to any node from source node
x = 'e'
path = []
while x is not None:
   path.append(x)
   x = parent[x]
path.reverse()
print(path)