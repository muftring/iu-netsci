# Breadth-First-Search (BFS) Algorithm
Breadth-first Search (BFS) is an algorithm which can serve two similar and related purposes:

(1) Finding the distance to all nodes that are "reachable" from a starting node; where reachable means that by traversing links between nodes one can navigate from the starting point to the destination.

(2) Finding the shortest distance from a starting node to a destination node.

BFS works by initializing all distances as infinity, or some other value which indicates "unknown."

Next, BFS records the distance from the starting node to itself as 0, and to each of starting node's neighbors as 1.

Then, for each neighbor compute the distance for each of its neighbors which has not yet had a distance recorded (distance is infinity or "unknown") as 1 + its own distance. Repeat this process until there are no unvisited nodes.
