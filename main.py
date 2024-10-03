from queue import PriorityQueue

INF = int(1e12)
N = 5

adj_list = [[] for _ in range(N)]
dist = [INF] * N

# Create Adjacency List
adj_list[0].append([1, 5]); adj_list[0].append([3, 1]);
adj_list[1].append([2, 2])
adj_list[2].append([4, 2])
adj_list[3].append([1, 2]); adj_list[3].append([4, 7]);

# Execute Dijkstra Algorithm with standard(start) node '0'
pq = PriorityQueue()
pq.put([0, 0])
dist[0] = 0

while not pq.empty(): # pq.queue
    cur_dist, cur_node = pq.get()
    for adj_node, adj_dist in adj_list[cur_node]:
        temp_dist = cur_dist + adj_dist
        if temp_dist < dist[adj_node]:
            pq.put([temp_dist, adj_node])
            dist[adj_node] = temp_dist

# Print result
print(dist)