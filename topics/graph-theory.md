# Graph Theory
[Graph Theory](https://en.wikipedia.org/wiki/Graph_theory): the Geometry of Position

> the birth of graph theory, which is linked to the history of a town called Königsberg and its 7 bridges

## The Bridges of Königsberg
<u>Problem:</u>   
Back in 1735, a City, a River, an Island, and seven bridges. Can one walk across all seven bridges and never cross the same bridge twice?

Leonard Euler mathematically proved that such a path does not exist.

<u>Observations:</u>   
- nodes with an odd number of links must be either the starting point or the end point
- a path cannot exist in a graph with that has more than two nodes with odd number of links

> some problems become simpler and more tractable if they are represented as a graph

> networks have properties encoded in their structure that limit or enhance their behavior

## Basic Components
- vertices, nodes
- edges, links

`N` = number of nodes, or size of the graph   
`L` = the number of links   
`k` = the *degree* of a node

## Types
- links can be directed or undirected
- directed graphs are called *digraphs*

## Utility
in order to apply network theory to a system, careful consideration must precede our choice of nodes and links, ensuring their significance to the problem we wish to explore

## Degree
A key property of each node is its *degree*, denoted by `k`; this represents the number of links a node has to other nodes.

The total number of links `L` can be expressed as the sum of node degrees `k`:

$$L = \frac{1}{2} \sum_{i=1}^{N}k_{i}$$

The 1/2 factor corrects for the fact that each link will be counted twice, once from each node it connects.

## Average Degree
The *average degree*, denoted `<k>`, can be derived as:

$$\left \langle k \right \rangle = \frac{1}{N}\sum_{i=1}^{N}k_{i} = \frac{2L}{N}$$

We have a factor of 2 here (in the simplified form) because every edge is counted by two nodes.

<u>Question:</u> Why do we want to know the average (mean) degree of a network?
- it gives us a good sense of *density* of the graph
- if the average degree is very small, or less than 1, then there should be a lot of nodes without any connections
- if the average degree is very big, approaching the number of nodes in the network, then we should see that the network is very dense, and almost *completely connected*

## Degree Distribution
The *degree distribution*, denoted p<sub>k</sub>, provides the probability that a randomly selected node in a network has degree `k`. Since P<sub>k</sub> is a probability, it must be normalized:

$$\sum_{k=1}^{\infty}P_{k} = 1$$

For a network with `N` nodes, the degree distribution is the normalized histogram given by:

$$P_{k} = \frac{N_{k}}{N}$$

where N<sub>k</sub> is the number of degree-`k` nodes.

## Weight
A value `w` is associated with the links

## Strength
The sum of all weights `w` for links connected to the node, denoted as `S`.

## Directed
In directed graphs the degree is distinguished by **in** and **out** which indicate the direction of the link relative to the node; **in** is a link arriving at the node, **out** is a link departing from the node. These are denoted k<sub>in</sub> and k<sub>out</sub> respectively. The total degree can be represented as k<sub>total</sub> = k<sub>in</sub> + k<sub>out</sub>.

Additionally, strength can be distinguished by **in** and **out**; the weights `w` on the links are summed by direction and denoted S<sub>in</sub> and S<sub>out</sub>.

## Adjacency Matrix
[Adjacency Matrix](adjacency-matrix.md)

## Real Networks are Sparse
(TBD)

## Weighted Networks
(TBD)

## Paths and Distances
A *path* is a route that runs along the links of the network.   
A *path's length* represents the number of links the path contains.

## Shortest Path
The shortest path between nodes *i* and *j* is the path with the fewest number of links. The shortest path is often called the distance between nodes *i* and *j*, and is denoted *d*<sub>*ij*</sub> or simply *d*.

## Network Diameter
The *diameter* of a network, denoted *d*<sub>*max*</sub>, is the maximum shortest path in the network. It is the largest distance recorded between any pair of nodes.

## Average Path Length
The *average path length*, denoted $\left \langle d \right \rangle$, is the average distance between all pairs of nodes in the network.

## Connectedness
The network (behind any system) must be capable of establishing a path between any two nodes. This is a key utility of most networks: they ensure connectedness.

In an undirected network, <u>nodes</u> i and j are *connected* if there is a path between them. They are *disconnected* if such a path does not exist.

A <u>network</u> is *connected* if all pairs of nodes in the network are connected. A network is *disconnected* if there is at least one pair of nodes that are not connected.

## Components
A *component* (subnetwork) is a subset of nodes in a network, so that there is a path between any two nodes that belong to the component.

If a network consists of two components, a properly placed single link can connect them, making the network connected. Such a link is called a *bridge*.

## Clustering Coefficient
The *clustering coefficient* captures the degree to which neighbors of a given node link to each other.

$$C_{i} = \frac{2L_{i}}{k_{i}\left ( k_{i} - 1 \right )}$$

$C_{i}$ measures the network's local link density: the more densely interconnected the neighborhood of node *i*, the higher is its local clustering coefficient.

The degree of clustering of a whole network is captured by the *average clustering coefficient* $\left \langle C \right \rangle$, representing the average of $C_{i}$ over all nodes:

$$\left \langle C \right \rangle = \frac{1}{N}\sum_{i = 1}^{N}C_{i}$$


**Review**
| Question | Answer |
| --- | --- |
| All networks exhibit the friendship paradox. | True |
| Networks with a heavy-tailed degree distribution is guaranteed to exhibit strong friendship paradox.    | False. <P> A counter example is a network with cliques (fully connected subgraphs) with different sizes. Each node's neighbor has the exactly same degree as the node in this network, although the degree distribution  can be arbitrarily tuned.   |
| Even a random (ER) network can exhibit the friendship paradox.  | True |
