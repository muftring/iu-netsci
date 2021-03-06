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

Degree distribution plays an important role, especially in scale-free networks. The existence of hubs make scale-free networks special affecting all sorts of dynamics in the network.

How much can we learn about the properties of the network just from the degree distribution?

Once we have the model of random graphs with degree distribution, then we can answer the question given real networks. Is this network something we can expect? (properties of the network - are they expected by the degree distribution or are there some surprising things?)

Random Graph Model is about answering two questions:
- how much does degree distribution decide?
- how much can we learn from degree?
  - Clustering Coefficient
  - Average Path Length
  - and, Percolation properties

# Erdos-Renyi random graph model
There are nodes. For each node, we try to connect to every other node with probability $p$. The average degree is $\left \langle k \right \rangle = p (n-1)$. And $p = \frac{\left \langle k \right \rangle}{(n-1)}$. And the degree distribution follows the *binomial distribution*:

$$Pr(k) = \binom{n  1}{k}p^{k}(1-p)^{n-1-k}$$

because it is essentially trying out probability $p$ and counting how many successes we have.

We can also calculate **Clustering Coefficient**, which is the *number of triangles* divided by the *number of counted triples*. Another definition is to look at the neighbor of every node and calculate how many actual edges are present, and calculate clustering Coefficient for each node and average for whole network.

*number of triangles* = $\binom{n}{3}p^{3}$<br>
Among $n$ nodes, choose $3$, and $p^{3}$ is the probability that every possible edge between these three nodes is present.

*number of connected triples* = $\binom{n}{3}p^{2}$<br>
Similar to above, but the probability is $p^{2}$, because we only need two edges to be connected.

So, *Clustering Coefficient* can be calculated as:<br>

$$\frac{\binom{n}{3}p^{3}}{\binom{n}{3}p^{2}} = p = \frac{\left \langle k \right \rangle}{(n-1)}$$

If you have a large graph, and a small average degree, then because $n-1$ will be very large, an Erdos-Renyi random graph will have a very small Clustering Coefficient.

## The Evolution of a Random Network
(Barabasi, 3.6)

$N$ = the number of nodes in a graph<br>
$N_{G}$ = the largest connected cluster in a graph<br>
$\left \langle k \right \rangle$ = average degree<br>
$p$ = the probability that an edge exists connecting two nodes<br>

Two extreme cases:
- $p = 0$, so $\left \langle k \right \rangle = 0$, meaning all nodes are isolated; therefore the largest component has size $N_{G} = 1$ and $\frac{N_{G}}{N} \rightarrow 0$ for large $N$
- $p = 1$, and $\left \langle k \right \rangle = N-1$, meaning all nodes are connected to each other (forming a complete graph), and therefore $N_{G} = N$ and $\frac{N_{G}}{N} = 1$

> Once $\left \langle k \right \rangle$ exceeds a critical value, $\frac{N_{G}}{N}$ increases, signaling the rapid emergence of a large cluster we call the **giant component**. The condition for the emergence is $\left \langle k \right \rangle = 1$; that is we have a giant component if and only if each node has on average more than one link.

## Four Topological Regimes

### Subcritical Regime
$$0 < \left \langle k \right \rangle < 1$$
$$(p < \frac{1}{N})$$

### Critical Point
$$\left \langle k \right \rangle = 1$$
$$(p = \frac{1}{N})$$

### Supercritical Regime
$$\left \langle k \right \rangle > 1$$
$$(p > \frac{1}{N})$$

### Connected Regime
$$\left \langle k \right \rangle > \ln N$$
$$(p > \frac{\ln N}{N})$$

## Real Networks are Supercritical
(Barabasi, 3.7)

Two predictions of random network theory are of direct importance for real networks:
1. Once the average degree exceeds $\left \langle k \right \rangle = 1$, a giant component should emerge that contains a finite fraction of all nodes. Hence, only for $\left \langle k \right \rangle > 1$ do the nodes organize themselves into a recognizable network.
2. For $\left \langle k \right \rangle > \ln N$ all components are absorbed by the giant component, resulting in a single connected network.

Many real networks do not obey the fully connected criterion. (See reading for supporting argument and material.)

# Configuration Model
In network theory, a key question is: **what is the impact of degree distribution on various network properties?**

If a network exhibits scale-free degree distribution, what would be the expected average path length? or what is expected value of clustering coefficient?

One way to answer:
- generate a lot of random networks which follow a degree distribution
- then calculate the quantity of interest in these random graphs
- this will tell us what to expect given a degree distribution

How can we create a network with a given degree distribution, randomly?

How can we sample a network with a given degree distribution from huge space of all possible graphs?

Idea:
- create the right number of nodes
- assign the nodes the right number of *stubs* (half of an edge)
- randomly connect two stubs to complete the edge
- repeat until all stubs are connected and the whole network is created

> **Configuration Model**: a mathematical formulation and practical method to generate a random network with a given degree distribution.

Approach:
- first create a list where each node id is repeated to match its degree
- shuffle the list
- group each pair of subsequent ids
- each pair to form an edge

| 1 | 1 | 1 | 2 | 2 | 3 | 3 | 4 |
| - | - | - | - | - | - | - | - |

| 1 | 3 | 1 | 4 | 2 | 1 | 3 | 2 |
| - | - | - | - | - | - | - | - |

Yields:

1 $\leftrightarrow$ 3 , 1 $\leftrightarrow$ 4 , 2 $\leftrightarrow$ 1 , 3 $\leftrightarrow$ 2

In many cases these random networks, generated using this *Configuration Model*, can accurately capture many properties of the network.

# Generating Functions
A **generating function** is a "trick" to record a bunch of numbers - open probabilities associated with some integer or count. It is a mathematical function that contains all the information about the probabilities so that we can recover all probability values any time we want.

We need to isolate all the values from each other. The simplest way is using a polynomial, by associating each number with a different power of the polynomial.

$$G(x) = p_{1}x + p_{2}x^{2} + p_{3}x^{3} ...$$

We primarily care about keeping the numbers "safely" inside the polynomial function.

How can we get $p_{1}$ back from the function?

Consider the function like a machine with a bunch of buttons that can be pressed. Each button corresponds to some mathematical operation.

Using *Calculus*, we take the derivative of $G(x)$ ...

$$p_{k}\stackrel{?}{=}\frac{1}{k!}\frac{d^{k}G(x)}{dx^{k}}\Big|_{x=0}$$

Generally:

$$G(x) = \sum_{k=0}^{\infty}a_{k}x^{k}$$

Generating functions are a really useful tool for studying random graphs with arbitrary degree distribution, and other problems in network science.

-----

# Review
| Question | Answer |
| --- | --- |
| The configuration model works by:   | Creating stubs for each node equal to the node's degree and randomly connecting them.  |
| In the configuration model the density of self-edges and multi-edges increases as the network gets larger, causing sampling problems for larger networks.   | False  |
| In the configurational model, in the large-N limit, all networks with the given degree sequence are sampled approximately uniformly.   | True  |
| A giant component of an infinite ER graph is the largest component with more than half of the nodes in the graph.   | False<p>A giant component is a component with non-zero relative size. It doesn't have to contain more than half of the nodes.   |
| In ER graph, when does the transition from subcritical (no giant component) to supercritical happen?   | When the mean degree is 1.   |
| A "graphic" sequence means that   | the sequence can be the degree sequence of some graphs  |

# References
- [Barabasi, chapter 3, esp. sections 3.6 and 3.7](http://networksciencebook.com/)
