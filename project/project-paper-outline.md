# Exploring Robustness in Dynamic Graphs

**Suggested outline:**
- Abstract
- Introduction
  - Motivation and review
  - Hypothesis, research questions, etc.
- Methods
- Results
- Discussion
- Conclusion
- References
- (Optional) Appendix

**Outline (WIP):**
1. Introduction
  - objectives
  - background material on graphs / networks / complex systems
  - approach
2. about Robustness
3. about Dynamic graphs
4. Exploration
  - Robustness in Dynamic Graphs
  - approach / techniques / tools
5. Results
6. Conclusion

-----

# Sections

## Abstract
(lifted from proposal - may need modification)

**Abstract.** A *dynamic graph* is a graph "in motion;" it changes over time. A static graph is one which never changes. A dynamic graph may be additive in nature, where vertices or edges are added to the graph. Or, a dynamic graph may be subtractive in nature, where elements are removed. These natures are not mutually exclusive, as a dynamic graph may demonstrate both additive and subtractive behaviors. The *robustness* of a graph is a measure of how well the graph maintains its structure, form, and integrity when undergoing drastic unexpected change. The measures generally used to reflect robustness are related to connectivity, path length, and clustering. This project aims to examine robustness in dynamic graphs by constructing models of behavior (both normal and unexpected), building an application which will realize the models and have them act on graphs, and implementing a means to maintain accurate measures for critical characteristics like shortest path lengths.



**Motivation**

To understand ... how dynamic graphs respond to different "threats" under their normal dynamic behavior (how can we model this? how can we apply the model programmatically? how can we see the model in action?) and how models can be created (augmented) to cope with various threats.


**Questions to answer**

What is a dynamic graph (network)? Provide a basic definition, provide some mathematical foundation,

What is robustness? Define robustness at a high-level. What are threats? Define two types of threats: failure, attack.

Need to bring in **Epidemics** and the models we studied (and additional models), and the concepts and types of immunization, and Epidemiology.

Is this bringing us towards *Network Medicine*?

## Methods

Incremental approach:
- be able to construct a simple dynamic network
- be able to observe simple changes
- can we model this? (with existing tools and libraries, or DIY)

- looking at DyNetX
- looking at NDlib
- looking at Cubix

- Python code to emit events to Gephi:
  - http://www.eecs.wsu.edu/~yyao/DirectedStudyII/src/Citation/GephiJsonClient.py

-----

# Introduction
## from [1]
A graph G is a pair (V, E), where V is a finite set of vertices or nodes, and E is a set of edges, each being an unordered pair {u, v} of distinct nodes.

dynamic graphs are graphs that change over time

definitions of (static) graphs and networks involve the following entities: V (a set of nodes), E (a set of edges), f (map vertices to numbers), and g (map edges to numbers). A dynamic graph is obtained when any of these entities changes over time.

There are some basic kinds of dynamic graphs:
- *node-dynamic*, the set of V varies over time; some nodes may be added or removed. When nodes are removed, the incident edges are also removed.
- *edge-dynamic*, the set of E varies over time; edges may be added or removed.
- *weight-dynamic*, the weights on vertices or edges changes
- *fully-dynamic*, all aspects of the graph may change

A dynamic graph can be viewed as a discrete sequence of static graphs. The properties of each static snapshot of a dynamic graph can be studied using the knowledge that has been developed for static graphs.

**Aside:** Logic Programming is based on a subset of predicate logic, called Horn Logic
predicates can also be viewed as relations, logic programming is also known as relational programming
There is quite a close connection between logic programming and graph theory

Dynamic graphs can be modeled using a logic program. The logic program can then be executed to discover interesting properties of the dynamic graph being modeled.

**ToDo:** provide a simple example which illustrates this concept

## from [2]
graphs are subject to discrete changes, such as insertions or deletions of vertices or edges

by dynamic graph we denote a graph that is subject to a sequence of updates

**Aside:** In a typical dynamic graph problem one would like to answer queries on dynamic graphs, such as, for instance, whether the graph is connected or which is the shortest path between any two vertices. The goal of a dynamic graph algorithm is to update efficiently the solution of a problem after dynamic changes, rather than having to recompute it from scratch each time.

**ToDo:** pick one algorithm and provide some high-level details

## from [3]
Concept of *Dynamic Connectivity*

The set V of vertices is fixed, but the set E of edges can change. Three cases:
1. Edges are only added (incremental connectivity)
2. Edges are only deleted (decremental connectivity)
3. Edges can be added and removed (fully dynamic connectivity)

## from [4]
A common point in all these areas () is that the system structure - the network topology - varies in time. Furthermore the rate and/or degree of the changes is generally too high to be reasonably modeled in terms of network faults or failures: in these systems changes are not anomalies but rather integral part of the nature of the system.

**Concept:** (formalism) / section 3 / This paper's main contribution is a unified framework called TVG.

A time-varying graph (TVG) is described by: $\mathcal{G}=(V, E, \mathcal{T}, \rho, \zeta)$

where:
- $V$ is the set of nodes
- $E$ is the set of edges
- $\mathcal{T}$ a time span, the lifetime of the system, where $\mathcal{T} \subseteq \mathbb{T}$
- $\rho : E \times \mathcal{T} \rightarrow \left \{ 0, 1 \right \}$ is called a presence function, which indicates whether a given edge is available at a given time
- $\zeta : E \times \mathcal{T} \rightarrow \mathbb{T}$ is called a latency function

The model can naturally be extended by adding node presence functions, and node latency functions:

- $\psi : V \times \mathcal{T} \rightarrow \left \{ 0, 1 \right \}$
- $\varphi : V \times \mathcal{T} \rightarrow \mathbb{T}$

## from [5]
The concept of dynamic networks is widely used for the study of complex networks with a variable structure of various natures. [...] a theoretical basis is required. The dynamic graph theory can provide such a basis. The main subject of this theory is the dynamic graph, which provides a model of a dynamic network.

Considered as a model of a dynamic network, a dynamic graph $\Gamma$ is a sequence of classical graphs $G_{l}$ that have no parallel edges and loops; transitions between these graphs are described by various graph-theoretic operations $\phi(G_{l}) = G_{l+1}$ (addition or removal of a graph element). The index $l$ corresponds to a kind of "topological time" at which the graph structure is modified.

In the general case, a dynamic graph is a sequence of finite unweighted (not necessarily connected) graphs $G_{1}, G_{2}, ... G_{L}, ...$ in which the next graph $G_{l+1}$ is obtained by applying an operation $\phi(G_{l}) = G_{l+1}$.

-----

How to represent?
- Time-ordered snapshots
- Stream of time-ordered events

-----

# References
[1] F.Harary, G.Gupta, *Dynamic Graph Models*, Mathl. Comput. Modelling, Vol.25, No.7, pp.79-87, 1997<br>
[2] C.Demetrescu et al, *Dynamic Graphs*, Handbook of Data Structures and Applications, 1ed, CRC Press, 2001<br>
[3] Dynamic connectivity, Wikipedia, 2017<br>
[4] A.Casteigts et al, Time-Varying Graphs and Dynamic Networks, Proc. Adhoc-Now'11, 2010<br>
[5] A. A. Kochkarova, R. A. Kochkarov, and G. G. Malinetskii, Issues of Dynamic Graph Theory, Computational Mathematics and Mathematical Physics, 2015, Vol. 55, No. 9, pp. 1590–1596, 2015
