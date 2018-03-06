# Communities

## Introduction
Clustering: your friends tend to know each other, and we form triangles.

In real networks, we form triangle and also larger scale structures called communities.

> Proteins form protein complexes to do certain job. Each complex is a molecular machine that does something.

- How can we define these communities?
- How can we identify them?
- What is the significance of these communities in network science?

### Why do we want to study network communities?
It is a fundamental method and aspect of many networks. Many analysis start with finding communities.

> **k-means clustering**<br>
> k-means clustering is a general data science algorithm.<br>
> Clustering is a basic and fundamental unsupervised learning method that gives useful insight into a data set.<br>
> Usually the communities correspond to some units in the network that bears some significance.
> Functional groups can be identified by structural communities.
> Network communities can serve as really basic analysis, but tend to correspond to important functional units (in bio system) or some important units.
> In social systems, network community often correspond to meaningful groups: data science program, our school, faculty group, etc.

Early ideas:
- <u>graph cuts</u>: with a graph, and a defined flow, which cut can you make which breaks the network into two parts while minimizing the sum of the weights destroyed. How to cut a network into two pieces in a nice way.
- <u>hierarchical clustering</u>: define some measure of similarity between nodes
- <u>betweenness</u>: the br

# Key Ideas
1. Communities should be **separable**: "Let's find cuts"
    - *divisive* method: break the network into parts
2. Communities should be **dense**: "let's find dense regions"
    - *agglomerative* method: start from some seed, and grow clusters

## Separable

### Kernighan-Lin Algorithm (graph cuts)
- originally for the layout of digital circuits
- assume almost equal size groups

Objective: to "break" network into separable groups
- so that they may be stored in a distributed database (for size and scale)
- minimize crosstalk: we don't want database nodes to have to 'talk' with each other all the time...

Approach:
- start from almost equal size groups (two groups), randomly assigned
- swap random pair of nodes
- see whether decrease sum of weight that go across the clusters

Goal:
- find the configuration where the sum of weight is minimized
- fewer edges between communities

### Edge Betweenness (Girvan & Newman)
> **betweenness** measures how a node participates in shortest path based communication int he network

Edge Betweenness: similar notion, how many times an *edge* participates in the shortest path in all pairs of nodes compared to total number of shortest paths.

Edges connecting communities (groups, clusters) tend to have large edge betweenness because they are between the groups.

Approach:
- find the edge with maximum edge betweenness
- cut that edge
- calculate edge betweenness again
- repeat
- eventually the communities will become clear

## Dense
*Perfect* communities: cliques (the most dense structure in a network)

*clique*: given a set of nodes, a clique is a subgraph that has every possible edge between them; every node is connected to every other node in the subgraph

Idea: just find cliques in the graph, and there are the communities

Problem: cliques are not really prevalent in networks, and they will not cover the whole graph.

### Density
Extension of the Idea: expand to more imperfect cliques, can simply generalize imperfect clique to *graph density*

Given a set of nodes, and edges, we can calculate graph density:

$$D = \frac{L}{\frac{n(n-1)}{2}}$$

L = number of edges<br>
n nodes, "n choose 2" possibilities of edges<br>

Density can be used as a guide to measure how close the subgraph is to a clique.

### Hierarchical Clustering
Start from a single node as its own community. Expand by finding what's the aggregation that you can get the most dense structure.

One Approach:<br>
distance or similarity measure of nodes, based on overlap of neighbors, then did hierarchical clustering

## Comparison
*When to stop? How good is it?*

We need to be able to measure *how good* the partition is!

# Modularity

-----
**Review**
| Question | Answer |
| --- | --- |
| Betweenness centrality can be used to cut important bridge edges and detect communities   | True <p> It was one of the earliest method. It works when the network has clear community structure but tends to fail in more tricky cases.  |
| Which of the following principles aren't consistent with finding communities:   | Cutting a network based on distance from hubs.  |
| Inspecting all possible community partitions of a network is a feasible method for determining the best community structure because it can give us the truly best community structure.    | False  |
| Which of the following explains the modularity approach to community detection?   | Find the partitions that maximize the distance between the actual and expected density.  |
| The modularity approach is an efficient algorithm that works well across all scales. It can finds very small to very large communities.    | False <p> While the algorithm is very efficient, it has a severe limitation in resolution that causes it to merge distinct communities below a detection threshold that will depend upon properties of the network.  |

-----
## Discussion
> **What are the network communities around us?** <p>
> In society, we belong to many social groups. Can you name some of the categories of social groups? For instance, if you are working in a company, everyone in your team should know each other and thus will form a network community. You can also imagine larger groups such as departments also form network communities (you tend to know more people in the same department than other department, etc.). What are the other types of social groups that you participate? <P>
Imagine other networks (e.g. biological, neural, ...). Will they exhibit network communities? Would they have relevance to the function of the whole network? Name some examples of network communities formed in networks other than the social network.

-----
# References
[Perpetual Enigma (blog)](https://prateekvjoshi.com)<br>
[What Is K-Means Clustering?](https://prateekvjoshi.com/2013/06/06/what-is-k-means-clustering/)<br>
[Partition of a set (Wikipedia)](https://en.wikipedia.org/wiki/Partition_of_a_set)<br>
[Bell number (Wikipedia)](https://en.wikipedia.org/wiki/Bell_number)<br>
[Modularity (Wikipedia)](https://en.wikipedia.org/wiki/Modularity_(networks))
