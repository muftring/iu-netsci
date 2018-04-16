# Network Science
- [Graph Theory](topics/graph-theory.md)
  - [Adjacency Matrix](topics/adjacency-matrix.md)
  - [Breadth First Search](topics/breadth-first-search.md)
  - [Dijkstra's Algorithm](topics/dijkstras-algorithm.md)
- [Distributions](topics/distributions.md)
  - [Binomial Distribution](topics/binomial-distribution.md)
  - [Poisson Distribution](topics/poisson-distribution.md)
  - [Power-Law Distribution](topics/power-law-distribution.md)
- [Random Networks](topics/random-networks.md)

- [Friendship Paradox](topics/friendship-paradox.md)
- [The Small World Phenomenon](topics/small-world-phenomenon.md)
- [The Strength of Weak Ties](topics/strong-ties-vs-weak-ties.md)

- [Barabasi-Albert Model](topics/barabasi-albert-model.md)
- [Scale-Free Networks](topics/scale-free-networks.md)
- [Centralities](topics/centralities.md)
  - [Centralities Reference (PDF)](topics/centralities-reference.pdf)
- [Communities](topics/communities.md)
  - Community Detection
  - Edge Betweenness
  - Hierarchical Clustering
  - Modularity
  - Map equation and infomap
  - Clique Percolation
  - Link Clustering
  - Link Communities
  - Assortative Mixing
- [Random Graphs](topics/random-graphs.md)
  - Percolation
  - Mathematical Model
  - Erdos-Renyi model
  - Configuration Model
  - Generating Functions
- [Epidemics](topics/epidemics.md)
  - Network Epidemics
  - Spreading Phenomena
    - Epidemic Modeling
    - Immunization
  - Network Epidemiology
- [Social Influence](topics/social-influence.md)
- [Information Diffusion](topics/information-diffusion.md)

- [Glossary](topics/glossary.md)
- [Symbols and Terms](topics/symbols-and-term.md)
- [References](references.md)

## Guiding Questions and Thoughts

"why should I care?" or "why is this important?"

Why do we want to study network science? The first two weeks will focus on this and the following questions:

First, what is a network?

Second, why do we talk about "complex systems" and how are they connected to "networks"?

Third, what kinds of complex systems and networks are around us?

Then, what can we do by studying network science? or why now?

# Networks

## What is a Network?

A set of *vertices* (or nodes) connected by *edges* (or links)

Nodes are individual elements of the system

Edges represent relationships
- stronger relationship: weight
- direction of relationship

system = elements + connections

## What is a Complex System?
(and what is the connection to networks?)

A *complex system* is described as having...
1. many parts
2. complex interactions

Understanding simple individual elements does not allow us to understand the whole system.

A complex system is a system with many parts that are interacting with each other in non-trivial ways.

Networks are about the individual elements (the nodes), and their interactions (the links). The network captures the backbone or structure of complex systems.

**Summary:**

1. We are living in complex systems (society, earth), and we are complex systems (brain, organs, cells)
2. Complex systems: complex interactions of many elements
3. The "structure" of complex systems can often be represented as networks

**Review**

| Question | Answer |
| --- | --- |
| What characterizes a cascading failure? | Subsequent failures that propagate to connected elements |
| How can interconnectivity lead to system vulnerability? | By a cascading failure of a single local failure |
| What has NOT been important in attracting attention to network science? | Major breakthroughs in computer networking protocols |
| Which is not one of the key characteristics of complex systems? | Decomposable |
| Which of the following would not be considered a complex system? | Ideal gases |
| What is not a basic building block of a network? | Matrix |

1. Cascading failures are characterized by their initial localized origin and subsequent branching from that origin. This branching can lead to a global failure of the system. Simultaneous and random failures may spark a cascading failure, but it is unlikely that enough failures will occur simultaneously to crash the whole network.
2. Interconnectivity allows localized parts of a system to interact with other localized parts. While this can have many benefits, it also means that failures which otherwise would have remained localized can spread non-locally throughout the system as whole.
3. Network science is a powerful tool and has garnered much attention because it is applicable across domains. This universality arises from commonalities between the processes of many complex systems, allowing us to describe a diverse array of phenomena using a few guiding rules and principles (some of which we will explore throughout this course).
4. Decomposable systems are systems that can be broken down into distinct levels that are largely non-interacting. For example, brownian motion can be understood at a system level as a stochastic process that results from the average movement of billions of molecules in fluid. Complex systems are not decomposable because the non-trivial interaction between their components prevents us from understanding system level behaviors as simple averages of component behavior.
5. Gases, fluids, and many other phenomena that can be readily expressed by either thermodynamics or equations of motions are not usually considered "complex". However, there are exceptions where these types of systems can exhibit near-chaotic behavior and their emergent properties are no longer trivially attained from thermodynamic principles or inferred from dynamical equations.
6. A matrix can be used to express a network, but a network it does not make.

## Networks Around Us
I was searching for "human organ interaction network" and discovered Network Physiology; this seems to be a very newly emerging field. Plamen Ivanov (Boston University) is trying to develop a whole new way of thinking about how the human body works.

"[...] If the research proves fruitful, Ivanov imagines that one day hospital patients will be hooked up to a whole new kind of monitor. Instead of narrowly measuring blood pressure, heart rate, and brain activity, these devices would track the relationships between key organ systems — alerting doctors to cataclysmic phase changes in human health before they occur."

nodes = organs   
links = relationships

Boston Globe article (2015)   
https://www.bostonglobe.com/ideas/2015/11/11/bringing-big-data-bear-organ-failure/Ce4o59gMx265w7UtdofooJ/story.html

Network Physiology: How Organ Systems Dynamically Interact.   
https://www.ncbi.nlm.nih.gov/pubmed/26555073

Keck Laboratory for Network Physiology   
https://sites.google.com/site/labnetworkphysiology/home

How an ‘atlas’ of living organs could save lives   
http://www.futurity.org/organ-atlas-1013522-2/

Focus on Network Physiology and Network Medicine   
http://iopscience.iop.org/journal/1367-2630/page/Focus%20on%20Network%20Physiology%20and%20Network%20Medicine

## Why Networks?

*Cascading failure and connected world*

*Google* -> `PageRank` -> one of the most successful early attempts to make use of the information hidden in the network structure of the web; the whole web is a giant network, and the act of linking a website is something like voting.

*Facebook* -> more directly about networks because the most important asset of Facebook is the social network around the world!

Remember: complexity does not come from the number of elements (remember the sun, which has way way more atoms than earth, yet in many sense a much simpler system?). The difference (between humans with 18,000 genes and rice plants with 32-50,000 genes) is in the interactions and in the network structure. What makes humans complex is the intricate interactions between genes, proteins, and all kinds of biological entities in our body. Having many lego blocks does not automatically lead to a better Lego model.

## Why Now?

Emergence of *Network Science* as a field of research and study occurred in the beginning of the 21st century.

**Two Shaping Forces**
1. The Emergence of Network Maps
  - in the past we lacked the tools to map these networks
  - it was equally difficult to keep track of the huge amount of data behind them
  - the *digital revolution* fundamentally changed the ability to collect, assemble, share and analyze data pertaining to real networks: with effective and fast data sharing methods, and cheap digital storage
2. The Universality of Network Characteristics
> A key discovery of network science is that the architectures of networks emerging in various domains of science, nature and technology are similar to each other, a consequence of being governed by the same organizing principles. Consequently, we can use a common set of mathematical tools to explore these systems.

**Characteristics of Network Science**
1. Interdisciplinary Nature
2. Empirical, Data-Driven Nature
3. Quantitative and Mathematical Nature
4. Computational Nature

**Review**

| Question | Answer |
| --- | --- |
| The universality of network characteristics arises from: | the similarity between organizing principles |
| What was the main reason why network science didn't emerge earlier?  | The lack of data and tools to map networks.  |
| What are some of the key methodological characteristics of network science?  | An emphasis on computational scalability and performance.  |
|    |  The integration of tools and techniques from many different fields of study. |
|   | A focus on empirical and data driven research.  |

1. The organizing principles of the systems underlying the network are the most important factor in giving rise to the universality of network characteristics. The properties and identities of nodes can vary wildly between networks of different kinds, but the nature of the relationships between those components is what ultimately defines how the network becomes structured. In systems science, a system is defined as a combination of 'thinghood' and 'systemhood' properties. The 'thinghood' properties can be atoms, cells, people, companies, etc. and they usually are described as nodes or vertices in a graph. The 'systemhood' properties define the relationships between the 'things', and these are generally described as edges or links in a graph. Universality arises from similarities in these systemhood properties.

## On Motivation

> what drives you has profound implications

Three factors lead to better performance and personal satisfaction:
1. Autonomy: the desire to be self directed
  - management is great if you want compliance
  - if you want engagement, self-directed is better
  - one day of autonomy produces things that might never emerge
2. Mastery: the urge to get better at stuff
  - for fun
  - because you get better at something, and that is satisfying
  - challenge + mastery + making a contribution
3. Purpose:

> when the **profit motive** gets unmoored from the **purpose motive**, bad things happen and people don't do good things; you begin to see the following emerge:
> - bad service
> - crappy products
> - uninspiring places to work

*be guided by your inner drive towards learning, mastery, and fun*

## Misconceptions

*as a student*
1. you will have some misconceptions about network science, and if you are not careful, you'll not be able to fix them! Worse, you may simply become more confident about yourself!
2. Don't be afraid to be wrong and pay attention to yourself and be very careful when you get confused. That's the chance that you can learn something new.

ToDo:   
share what kinds of misconceptions you had and how you fixed them!
