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

| Hierarchical Clustering |
| --- |
| The starting point of hierarchical clustering is a *similarity matrix*  whose elements $x_{ij}$ indicate the distance of node $i$ from node $j$. |   
| Once we have $x_{ij}$, hierarchical clustering iteratively identifies groups of nodes with high similarity. <P> Two different approaches:<br> - *agglomerative*: merge nodes with high similarity into the same community <br> - *divisive*: isolate communities by removing low-similarity links |
| The dendrogram visualizes the order in which the nodes are assigned to specific communities. |

## Comparison
*When to stop? How good is it?*

We need to be able to measure *how good* the partition is!

# Modularity
One of the most basic measure of community quality.<br>
It can be used to find communities, it can be used to measure communities.

$$Q=\frac{1}{2m}\sum_{ij}^{ }\left [ A_{ij} - \frac{k_{i}k_{j}}{2m} \right ]\delta (c_{i}, c_{j})$$

$Q$ is the *modularity*<br>
$m$ is the number of *edges*<br>
sum over all pair of nodes, $\sum_{ij}^{ }$<br>
$A_{ij}$ is the *adjacency matrix*<br>
$k_{i}k_{j}$ are the degree of nodes $i$ and $j$<br>
$\delta (c_{i}, c_{j})$ is a delta function: $1$ if $c_{i}=c_{j}$, $0$ otherwise<br>
$c_{i}, c_{j}$ represent the community membership of nodes $i$ and $j$<br>

What this is doing is comparing **the ACTUAL number of edges inside a community** [which is done by $A_{ij}$, and the delta function] with **the EXPECTED number of edges inside a community** [which is done by degree over $2m$ and the delta function].

We want to **maximize the gap** between the ACTUAL density and the EXPECTED density given a partition.

# Drawbacks and Problems with Modularity

## Resolution Limit
Modularity value largely depends on network size, the total number of edges. As networks become larger, we tend to find larger communities. It cannot be solved below certain resolution.

Modularity cannot find small communities in larger networks. This is not necessarily always a drawback, because you may just want a "rough description" of the network. But it seems counterintuitive that you cannot even find perfect clique (fully connected subgraph) when a network becomes large.

Sever degeneracies: there are many different clustering configurations / community assignments (i.e., structural differences) that have very similar (or the same) modularity values. There is no clear global optima.

## Modularity is difficult to optimize
There are many configurations where modularity is similarly high while the structure is very different. By the nature of the network structure it is very hard to find global optimum.

## Overlapping communities and Link communities
Philosophical and fundamental problem is Modularity and many other methods assume non-overlapping and disjoint community structures. While in society we often encounter highly overlapping communities.

# Map equation and infomap
One nice alternative method which helps overcome some of the issues of Modularity is **infomap** method which uses the quantity called **Map equation**.

Similar to Modularity, it measures the quality of a given clustering. It uses **information theory** to measure the best number of bits needed to encode a territories of random walkers.

$$L(M) = q_{\curvearrowright } H(\mathcal{Q}) + \sum_{i=1}^{m}p_{\circlearrowright}^{i}H(\mathcal{P}^{i})$$

nice qualities:
- robustness against resolution limit
- as well as other good properties
- tends to perform really nicely

## Understanding Infomap
The basic idea of the **infomap** algorithm is to try to encode a random walkers trajectory.

The random walker's trajectory is recorded as a sequence of encoded words representing the node to node or teleportation traverse of the network.

When we have string communities, it is better to have a hierarchical representation. First we encode the community: the identity (e.g., color). Once within a community, then use the codebook for that community as long as it stays within the community. There are special codes that represent exit from a community, then you identify the next community being entered.

# Overlapping Communities
A node is rarely confined to a single community.

Tamas Vicsek et al, *Uncovering the overlapping community structure in complex networks in nature and society* (2005, Nature)

## Clique Percolation
The *clique percolation algorithm* (CFinder) views a community as the union of overlapping cliques.

- two k-cliques are considered adjacent if they share $k - 1$ nodes
- A k-clique community is the largest connected subgraph obtained by the union of all adjacent k-cliques
- k-cliques that cannot be reached from a particular k-clique belong to other k-clique communities

| CFinder |
| ------- |
| The CFinder algorithm identifies all cliques and then builds an $N_{clique}$ x $N_{clique}$ clique-clique overlap matrix $O$, where $N_{clique}$ is the number of cliques and $O_{ij}$ is the number of nodes shared by cliques $i$ and $j$. |

## Link Clustering
While nodes often belong to multiple communities, links tend to be community specific. They capture the precise relationship which defines a node's membership in a community.

| Link-Clustering Algorithm | |
| --- | --- |
| Step 1: Define Link Similarity | $S((i,k),(j,k)) = \frac{\left | \, n_{+}(i) \; \cap \; n_{+}(j) \, \right |}{\left | \, n_{+}(i) \; \cup \;  n_{+}(j) \, \right |}$ <p><p> where $n_{+}(i)$ is the list of neighbors of node $i$, including itself. <P> $S$ measures the relative number of common neighbors $i$ and $j$ have. <p> $S = 1$ if $i$ and $j$ have the same neighbors.|
| Step 2: Apply Hierarchical Clustering   |  |

# Link Communities
The key idea of *link communities* is pervasive overlap. And pervasive overlap means that the overlap between communities is pervasive and not assuming that communities are almost/essentially disjoint.

In *modularity* we strive to find the "cut" which divides the network and identifies the separate communities. But in *link communities* it is argued that this is not possible.

The consequence of this pervasive overlap is: if you look at local structure, it may be rather simple. But when you assemble all of the small local structures, it creates a big tangle. (Example: word association network.)

*Link similarity* is defined between two edges, and we consider only those edges which share a node (if they do not share a node, they are separate and are likely not to be very close). Next, count the neighbors of the nodes and compute the Jaccard Coefficient.

> Jaccard Coefficient: intersection divided by union

With the *link similarity* -- a matrix of similarity measures between edges where every row and column represents an edge -- perform *hierarchical clustering*.

*Partition Density* - essentially graph density for a given community. Calculate the density: the number of edges within the subgraph divided by the number of possible edges. And subtract the number of edges in the minimally connected subgraph with the same number of nodes.

$$D\equiv \frac{2}{M}\sum_{c}^{ }m_{c}\frac{m_{c}-(n_{c} - 1))}{(n_{c}-2)(n_{c}-1)}$$

With partition density, for each link community we can calculate all of the densities.

**Algorithm**
- define the similarity between all of the individual edges
- construct hierarchical tree: dendrogram
- calc partition density for each level
- produces a curve
- find the maximal partition density cut to show the final community structure

group/community membership is naturally given by the edges

intentionally choose the simplest way to obtain link community (define similarity, do hierarchical clustering)

POV: relationships between nodes is more fundamental than the nodes, and is more useful discovering complex structure in networks

# Metrics and Measures
(Newman, M.E.J.)<br>

## Assortative Mixing by Enumerative Characteristics
A network is *assortative* if a significant fraction of the edges in the network run between vertices of the same type. A simple way to quantify assortativity would be to measure that fraction. But that does not prove to be a good measure because it would be $1$ if all vertices are the same type; this becomes a trivial assortativity.

What is desired is the measure to be large in non-trivial cases, and small in trivial cases.

A good measure instead is: find the fraction of edges that run between vertices of the same type, and then subtract from that the fraction of edges we would *expect* to find if edges were positioned at random without regard for vertex type.

Some math brings us to the formula for **Modularity**: the measure of the extent to which like is connected to like in a network.

$$Q=\frac{1}{2m}\sum_{ij}^{ }\left [ A_{ij} - \frac{k_{i}k_{j}}{2m} \right ]\delta (c_{i}, c_{j})$$

> assortative |əˈsôrtətiv|<br>
adjective [ attrib. ]<br>
denoting or involving the preferential mating of animals or marrying of people with similar characteristics.

## Assortative Mixing by Scalar Characteristics
If network vertices with similar values of a *scalar characteristic* (particularly ordered characteristics, like age or income) tend to be connected more often than those with different values then the network is considered assortatively mixed according to that characteristic.

Example: if people are friends with others around the same age as them, then the network is assortatively mixed by age. Sometimes this is called *stratified* by age, which means the same thing.


> stratify |ˈstratəˌfī|<br>
verb (stratifies, stratifying, stratified) [ with obj. ] (usu. as adj. stratified)<br>
form or arrange into strata: *socially stratified cities* | [ no obj. ] : *the residues have begun to stratify*.
> - arrange or classify: *stratifying patients into well-defined risk groups*.
> - place (seeds) close together in layers in moist sand or peat to preserve them or to help them germinate.
> - [ no obj. ] (of seeds) be germinated by stratifying.

## Assortative Mixing by Degree
A special case of assortative mixing by scalar quantity, degree. In a network that shows assortative mixing by degree the high-degree vertices will be preferentially connected to other high-degree vertices, and the low to low.

In an assortative network where high-degree nodes tend to stick together, we expect a "clump" or core of such high-degree nodes in the network surrounded by a less dense periphery of nodes with lower degree. This *core/periphery structure* is a common feature of social networks, many of which are found to be assortatively mixed by degree.

If a network is disassortatively mixed by degree, then high-degree vertices tend to be connected to low-degree vertices. This creates star-like features in the network which are often readily visible.

-----
**Review**
| Question | Answer |
| --- | --- |
| Betweenness centrality can be used to cut important bridge edges and detect communities   | True <p> It was one of the earliest method. It works when the network has clear community structure but tends to fail in more tricky cases.  |
| Which of the following principles aren't consistent with finding communities:   | Cutting a network based on distance from hubs.  |
| Inspecting all possible community partitions of a network is a feasible method for determining the best community structure because it can give us the truly best community structure.    | False  |
| Which of the following explains the modularity approach to community detection?   | Find the partitions that maximize the distance between the actual and expected density.  |
| The modularity approach is an efficient algorithm that works well across all scales. It can finds very small to very large communities.    | False <p> While the algorithm is very efficient, it has a severe limitation in resolution that causes it to merge distinct communities below a detection threshold that will depend upon properties of the network.  |
| Which of the following describes the modularity best?   | Modularity is the difference between the actual number of edges within communities and the expected number of edges within communities  |
| The resolution limit of modularity depends on what two components:   | Size of network and connectivity between modules  |
| Modularity has no intrinsic scale.   | False <br> (see reading: *Resolution limit in community detection*) |
| Modularity tends to do well on graphs with power-law distributed community sizes.  | False  |
| Modularity is usually okay for detecting communities when they are moderately sized with respect to the network.   | True  |
| Modularity tends to be good for detecting very small communities on large graphs.   | False  |
| Which best describes how infomap works:   | Finds community partitions that minimize the encoding scheme.  |
| Infomap can readily be used with directed and weighted graphs without throwing out information.   | True  |
| Aside from just detecting communities infomap also _____   | Detects the flow of information between communities.   |
| In the K-clique method why are the cliques compared with those of a random graph?   | To determine if the communities could have been generated by chance.  |
| How does Link clustering identify nodes that belong to multiple communities?   | Nodes with links that belong to different communities have multiple membership.  |
| Link communities can produce hierarchical memberships from which a dendrogram can be derived.   | True  |

-----
# Discussion
## What are the network communities around us?
> In society, we belong to many social groups. Can you name some of the categories of social groups? For instance, if you are working in a company, everyone in your team should know each other and thus will form a network community. You can also imagine larger groups such as departments also form network communities (you tend to know more people in the same department than other department, etc.). What are the other types of social groups that you participate? <P>
Imagine other networks (e.g. biological, neural, ...). Will they exhibit network communities? Would they have relevance to the function of the whole network? Name some examples of network communities formed in networks other than the social network.

## Communities
> Now that you have been exposed to a whole range of community detection algorithms and have seen some of their advantages and disadvantages think about how they could be used in practice.<p>
> Describe some real-world scenarios where some of these algorithms would succeed or where they would fail.<p>
> How do you think these various algorithms do at capturing what it means to be a "community"?

-----
# References
[Perpetual Enigma (blog)](https://prateekvjoshi.com)<br>
[What Is K-Means Clustering?](https://prateekvjoshi.com/2013/06/06/what-is-k-means-clustering/)<br>
[Partition of a set (Wikipedia)](https://en.wikipedia.org/wiki/Partition_of_a_set)<br>
[Bell number (Wikipedia)](https://en.wikipedia.org/wiki/Bell_number)<br>
[Modularity (Wikipedia)](https://en.wikipedia.org/wiki/Modularity_(networks))<br>
[Map Equation](http://www.mapequation.org/index.html)<br>
