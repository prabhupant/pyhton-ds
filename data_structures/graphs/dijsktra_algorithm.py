'''When iterating across nodes, always choose the smallest path with an un-visited vertex. 
Store all distance + vertices in a min heap to automatically get the next shortest path. 
If there is a limit on the amount of edges that can be visited (Ex: LeetCode Cheapest Flights Within K Stops), 
maintain an array tracking the maximum edges to get to a vertex, and if the number of edges taken goes up, do not proceed with the iteration.

Time complexity: O(V + E x log(V)) with min heap'''

min_heap = []
heapq.heappush(min_heap, [0, k + 1, src]) # only need 'k + 1' if max k edges requirement
visited = set()
edges_to_vertex = [0] * n # only needed if max k edges requirement

while min_heap.peek() is not None:
    distance, edge_count, vertex = heapq.heappop(min_heap)
    if vertex in visited:
        continue
    visited.add(vertex)
    if vertex == dst:
        return distance

    # only needed if max k edges requirement
    if edges_to_vertex[vertex] >= edge_count:
        continue
    edges_to_vertex[vertex] = edge_count

    if vertex in edges:
        for edge in edges[vertex]:
            heapq.heappush(min_heap, [distance + edge[1], edge_count - 1, edge[0]])

return -1
