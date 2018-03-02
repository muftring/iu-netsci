# Centralities
*Measuring Importance*

## Introduction

- why and when do we want to characterize nodes, links, and other objects in networks?
- what are the key ideas behind network centralities?
- Degree-based centralities:
  - Degree
  - Eigenvector
  - Katz
- Random-walk based centralities: PageRank
- Distance-based centralities: Closeness
- Communication-based centralities: Betweenness

*How can we operationalize 'importance'?*
- degree is just one way
- in many cases degree can become useless
  - social media: following and followers
  - accounts/users/people who simply try to obtain large numbers
  - there is no content
  - concern is on quantity of followers, not quality

**Why?**
- why do we want to measure centralities?
- why do we want to find important nodes or links in a network?

**Basic Ideas**
- what are the fundamental ideas behind these measures?
- often then are really simple ideas
- sometimes those simple ideas can give a lot of information about the network
  - and individual nodes and edges

**How to apply?**

## Discussion

**What does it mean to be important?**
> So, the question is, what does it mean to be **important** in a network? Why do we want to define and identify those important nodes, links, and so on? Please share your thoughts by picking a couple of networks and suggesting several ways to think about the importance of a node, an edge, or any network object. Feel free to discuss how you could define measures of importance.

The human organ network is perhaps a very interesting example to consider here, and it is also a very tricky network to provide a definitive answer to importance.

At a high level, some of the nodes in the human organ network would be: the brain, heart, lungs, stomach, intestines, liver, kidneys, and so on. The links might be blood vessels (arteries and veins), lymph nodes, and some portions of the digestive tract (esophagus, intestines).

Which is most important?

A quick thought might be to answer the brain. After all, this organ is what controls almost everything; without it a human cannot function.

However, the brain cannot function without oxygen which is provided by blood flow. The blood is oxygenated by the lungs and the heart is the pump which circulates blood throughout the body.
So, is the heart or are the lungs more important?

What about all of the complicated mechanisms in the digestive and related organs? Without ingestion of food and water, there is no energy to propel cells to function... in every organ, and in every far reaching place of the human body.

In the case of the human organ network, importance must take on several different measures relative to necessity of function relative to the different aspects of survival.

Ultimately, the brain is probably the most important organ because it does control both voluntary actions (eating, drinking, social contact, awareness of surroundings) and involuntary actions (breathing, heart beating, metabolism, survival instinct) of the human which are necessary for survival. The brain is dependent on many other organs, and there is a multifaceted symbiotic relationship, but ultimately they cannot function without the brain's "orders."

## Many Different Centralities
> There are so many network centralities! How many, or which should we learn??
(see: Periodic Table of Network Centrality)

There are many different rationales and circumstances behind centralities. We need to precisely define what we want from the network.

The key idea: *think of fundamental dynamic processes*
- "Spreading information to neighbors." (**information spreading**)
  - how many neighbors can you reach in one step? *degree* is an important measure.
- "Everyone communicate with everyone else through shortest path." (**communication**)
  - bridge, bottleneck node
- "A random walker walks on the network" (**exploration**)
  - how likely this random walker will reach a certain node -> PageRank

If you assume certain types of these dynamics, you can define certain measure of importance for nodes and links. And then you can identify important parts of the network.

# Degree and diffusion based measures

## Degree
- "spreading"
- Some process that affects the neighbors.
- In parallel (simultaneous, instant to all).

## Eigenvector
- based on the same idea as degree: "spreading"
- but it considers more steps
- a node connected to (perhaps multiple) hubs
- something passed from a node to its neighbors (which are hubs), can then quickly reach even more nodes (in additional steps)
- importance is the sum of neighbors importance

Getting the eigenvector component for each node associated with the leading eigenvalue of the adjacency matrix.

**Problems**
1. it does not work well in directed graph
2. in a large graph with degree distribution is Power Law, or heavy tail, only a few nodes get non-zero Eigenvector Centrality and the rest have value almost zero
    - for a hub connected to other hubs, the Eigenvector Centrality will become so large it belittles every other node
    - all other values will be to small to be valuable

Eigenvector centrality may just identify the biggest hubs and nothing much more.

**Strengths**
- small graphs
- undirected graphs

## Katz
*Solved the main problem of Eigenvector Centrality* by having a pre-term, $\alpha$ and $\beta$. Each node is given a pre-term $\beta$ in each iteration .. and the result is everyone will have non-zero value for the centrality. $\alpha$ can adjust the balance between how large the $\beta$ term will be vs. the Eigenvector centrality term.

Typically set $\beta$ = 1 because the absolute size does not matter, but rather the balance between $\alpha$ and $\beta$ matters.

## PageRank
Historically, it was the main algorithm of the *Google* web search engine.

<u>Idea</u>: *how can we measure the importance of web pages?* Very similar to centrality ideas:

- getting directed links (hyperlinks) are like "voting" - **degre idea**
- getting links from important sites are more important - **Eigenvector centrality idea**
- but if an important site has millions of links and only one of them is linking to me, then it should be discounted
  - let's assume "flow" of random web surfers
  - instead of thinking about "spreading" process

### PageRank: the basic idea
It starts with the below form which is Eigenvector centrality, but includes the concept of *flow* which considers the influence of a node by dividing by the outgoing degree $k_{j}^{out}$.

$$x_{i} = \alpha\sum_{j}^{ }A_{ij}\frac{x_{j}}{k_{j}^{out}}$$

True Eigenvector Centrality behavior is to "send" the full amount of influence (the Eigenvector value) along each outgoing link. But PageRank fairly portions the influence sent along each outgoing link to the proportion relative to the degree of the node.

### Spider Trap problem
Two nodes that link to each other will repeatedly send the same value back-and-forth, causing an endless oscillation of value over time.

| time<br>node| | | | | | | |
|--|-|-|-|-|-|-|-|
| A |0|1|0|1|0|1|...|
| B |1|0|1|0|1|0|...|

This presents convergence...

### Dead End problems
(1) Nodes with no incoming edges will not have any Eigenvector value, and that propagates.. even to nodes which are inbound connected to those nodes, but no others.

(2) Nodes with only incoming edges consume and waste the "flux"

| time<br>node| | | | | | | |
|--|-|-|-|-|-|-|-|
| A |0.5|0|0|...|...|...|...|
| B |0.5|0|0|...|...|...|...|
| C | 0  |  1 |  0 |...|...|...|...|

### PageRank: the final form
- Spider Trap and no incoming edge: random teleport
- Dead End: always teleport

$$x_{i} = \alpha\sum_{j}^{ }A_{ij}\frac{x_{j}}{k_{j}^{out}}+\beta$$

### Conservation of the total flux
Diffusion (walk) instead of spreading:

**spreading** - Eigenvector value is spread along each outgoing link

**diffusion (walk)** - total Eigenvector value is preserved, but portioned equally to each outgoing link

This ensures iteration of PageRank does not diverge, like Eigenvector Centrality case. Also it balances nicely between importance of hubs and other nodes. PageRank prefers to be in hubs, but not as much as Eigenvector Centrality. PageRank tends to distribute importance more equally than Eigenvector Centrality.

# Path-based measures
- think about some communication process happening in networks
- (usually) assume that the communication happens across shortest path
- (usually) assume that everyone talks to everyone else

## Closeness
How *close* is node $x$ to node $y$? It is defined as (with some normalization factor, not represented in the below equation):

$$C(x) = \frac{1}{\sum_{y}^{ }d(y,x)}$$

Notes:
- $d(y,x)$ is the measure of distance from $y$ to $x$
- the sum $\Sigma$ is for all nodes $y$ in the graph
- if the node is close to everyone else, then the distance will be very small
- and the *closeness* value will be very large

Problems:
- sometimes the distance from $y$ to $x$ is not defined
- for example, in a graph with two unconnected clusters
- we cannot sum the undefined distance across all other nodes

## Harmonic centrality
(sometimes simply called *closeness*)<br>
Solves the issue of: the distance from $y$ to $x$ is not defined

$$H(x) = \sum_{y \neq x}^{ }\frac{1}{d(y,x)}$$

Define $d(y,x) = \infty$ if $x$ is not reachable from $y$. If you use the convention that $\frac{1}{\infty} = 0$, then you simply ignore all of the unconnected pairs. That means you can naturally incorporate the extreme cases, where a node or two exist outside and disconnected from a large component.

## Betweenness
*Betweenness* is useful to detect cases when a node connects two larger components; a node *between* many node pairs, it will mediate the communication between many nodes.

$$C_{B}(v) = \sum_{s \neq v \neq t \in V}^{ }\frac{\sigma_{st}(v)}{\sigma_{st}}$$

Consider $s$, $v$, and $t$ which are nodes that are all different and belong to the network. Count the number of *shortest paths* between $s$ and $t$ which is represented by: $\sigma_{st}$.

Why count the number of *shortest paths*? Often there are multiple paths from $s$ to $t$ which have the same shortest path length, and there is no distinction between them.

*Betweenness* involves picking every pair or nodes in the network, and calculating the *shortest path*. 

-----
**Side notes / comments**

"sociology—a subject that views a group of people more like a blob or a network than a totem pole"

"(looking for) those unexpected connections—surprising bonds that might eventually lead to (something)"

-----
**Review**

| Question | Answer |
| --- | --- |
| Given this small graph, calculate the eigenvector centrality of each node. In order to gain a common reference point for the results, rescale the centralities so that their sum equals the number of nodes. What is the rescaled eigenvector centrality of node 7?  | (see notebook)   |
| Which of the following is not a problem of eigenvector centrality?   | It cannot be applied to small networks. |
| For a directed network, it's better to use Katz centrality rather than Eigenvector centrality because it can assign non-zero values even for the nodes that do not belong to SCC.    | True |

-----
**References**   
[Periodic Table of Network Centrality](http://schochastics.net/sna/periodic.html)

[Eigenvectors and Eigenvalues](http://setosa.io/ev/eigenvectors-and-eigenvalues/)
