# Theory of Random Graphs

# Percolation
When and how is a network "connected?"

This is a fundamental problem that can be mapped into many key problems in network science:
- Epidemics
- Robustness
- Influence
- spreading of information

Understanding the *Percolation Problem* is at the heart of Network Science.

Percolation is a fundamental problem from **Physics**.

Can we find a path or spanning clusters (...)?

Percolation in **Networks**

We have a graph with nodes and no edges.
Start adding edges.
We can describe how many edges are added with probability $p$.
Then we can ask: "given $p$, given the number of edges added to the network, is the network connected? do they form large clusters? or mainly isolated components?"

Connected to many problems in Network Science

# Mathematical Model of Random Graphs
Random graphs with arbitrary degree distribution: what's expected given a degree distribution and what's not?

Degree distribution plays an important role, especially in scale-free networks the existence of hubs makes scale-free networks special affecting all sorts of dynamics in the network.

How much can we learn about the properties of the network just from the degree distribution?

Once we have the model of random graphs with degree distribution, then we can answer the question
given real networks

is this network something we can expect? (properties of the network - are they expected by the degree distribution or are there some surprising things?)

Random Graph Model is about answering two questions:
- how much does degree distribution decide?
- how much can we learn from degree?
  - Clustering Coefficient
  - Average Path Length
  - and, Percolation properties

# Erdos-Renyi random graph model
There are nodes. For each node, we try to connect to every other node with probability $p$. The average degree is $\left \langle k \right \rangle = p (n-1)$. And $p = \frac{\left \langle k \right \rangle}{(n-1)}$. And the degree distribution follows the *binomial distribution*:

$$Pr(k) = \binom{n \;\; 1}{k}p^{k}(1-p)^{n-1-k}$$

because it is essentially trying out probability $p$ and counting how many success we have.

We can also calculate **Clustering Coefficient**, which is the *number of triangles* divided by the *number of counted triples*. Another definition is to look at the neighbor of every node and calculate how many actual edges are present, and calculate clustering Coefficient for each node and average for whole network.

*number of triangles* = $\binom{n}{3}p^{3}$<br>
Among $n$ nodes, choose $3$, and $p^{3}$ is the probability that every possible edge between these three nodes is present.

*number of connected triples* = $\binom{n}{3}p^{2}$<br>
Similar to above, but the probability is $p^{2}$, because we only need two edges to be connected.

So, *Clustering Coefficient* can be calculated as:<br>

$$\frac{\binom{n}{3}p^{3}}{\binom{n}{3}p^{2}} = p = \frac{\left \langle k \right \rangle}{(n-1)}$$

If you have a large graph, and a small average degree, then because $n-1$ will be very large, an Erdos-Renyi random graph will have a very small Clustering Coefficient.
