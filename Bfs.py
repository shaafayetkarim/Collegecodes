import queue

adj = { 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }


def bfs(vertex, adj):
  vis = []
  q = queue.Queue()
  popped_res = []
  q.put(vertex)
  vis.append(vertex)
  
  while q.qsize() != 0:
    top = q.get()
    popped_res.append(top)
    for child in adj[top]:
      if child in vis:
        continue
      vis.append(child)
      q.put(child)
  
  
  return popped_res

print(bfs(0, adj))