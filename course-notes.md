# Network Science

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


# Friendship Paradox
Consider a random person, Alice, who has M friends.   
Each of Alice's friends has N<sub>1</sub>, N<sub>2</sub>, N<sub>3</sub>, ... N<sub>i</sub> friends, for which the average is &lt;N<sub>i</sub>&gt;   
If we do this many times, which one is larger?
1. A random person's friends (M)?
2. Friends' friends (average of N<sub>i</sub>)?
3. They are the same.

## Facebook
*Graph API Explorer*   
https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=%7Buser-id%7D%2Ffriends&version=v2.11

## Doodles
{image}

## Resolution
Often the average N (the number of friends of friends of a random person) is larger than M (the number of friends of a random person).

Shouldn't they be the same because both of them are randomly picked?

Actually no. You can mathematically prove that for most people in society, their friends have more friends than themselves. How can this be possible?

### The Friendship Paradox
 (https://www.youtube.com/watch?v=httLvVufAYs)
- comparing yourself to your friends is not that accurate
- people with few friends are not that likely to appear in your list of friends
- they are more likely to exist in the general public
- this is due to **Sampling Bias**:
The sample of people you are comparing yourself to is biased to people in general.
- there are relatively more people with lots of friends, and relatively fewer people with not a lot of friends
- <u>Question</u>: how can most people's friends be more popular than them?
- people can count more than once
- the more friends you have, the more averages you influence

### Resolving the Friendship Paradox
> the probability of appearing in one's neighbor is strongly correlated with the number of neighbors

- expect to have more *well connected* nodes in the neighbor of yourself (or any random person)
- if you follow one link you are more likely to get to the people who have many many friends
- follow an edge, you are very likely to read *hubs*
- **hubs**: people with many many Friends
- whenever you follow a link you are very likely to arrive at a  node with many neighbors

This principle applies not only to friends in social networks, but also appears in:
- number of papers that scientists write
- citation networks in papers
- fame

## Friendship paradox beyond the number of friends
Actually, the friendship paradox can be generalized to other characteristics because often the number of connections (friends) has a high correlation with other characteristics. For instance, people have found that in science, "your co-authors tend to have more papers and more citations".

> The origin of the GFP is shown to be rooted in positive correlations between degree and characteristics.

https://www.nature.com/articles/srep04603


## Lessons from the Friendship paradox
> Share your thoughts on the lessons from the friendship paradox!

> Having insanely successful people around you is a law of nature, so don't feel too bad and don't pay too much attention on how well your friends are doing!

I like to think (certainly incorrectly) that I am the insanely successful center of an amazing network! :)

I suppose that even those insanely successful people look around themselves and feel envy towards even more insanely successful people. Where does it end? With Warren Buffett or Bill Gates? If we consider wealth as the ultimate measure of success. But is it?

I firmly believe that there is a paradox surrounding the friendship paradox (wrt social networks), or perhaps it is an analogue: the perception that those with more friends are happier or more successful is wrong, and thus this supports the notion of "don't compare yourself to your friends." At least not in the realm of social networks.

## Which friends are more popular than you?
a more nuanced nature of the friendship paradox

https://arxiv.org/abs/1703.06361


# Graph Theory
(the Geometry of Position)

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

## Networks and Graphs

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

## Degree Distribution of a Randomly Chosen Neighbor and Friendship Paradox

https://youtu.be/77Q_XIBjdeA?t=9m47s

Alice has degree distibution P<sub>k</sub>   
Neighbor is not P<sub>k</sub>   

Reason: the process is different; picking a random person, there is a pool of `N` people and choose randomly one person so we can use P<sub>k</sub>  

Follow a link which seems random, but is slightly different;
the pool of random we a sample from is not the `N` nodes. We sample from the network by following an edge.

When you follow an edge an interesting thing happens.

For the neighbor is it kP<sub>k</sub> because there are `k` ways to arrive at the node (following one of the links to it)

The degree of a randomly selected node is expected to be \<k>   
The degree of a neighbor is <k<sup>2</sup>>

Note: this does not hold for *everyone*; consider a start network and choosing the most connected node.

<u>Conclusion</u>: the friendship paradox is real for the vast majority of nodes in a network; expect that a randomly selected node has far fewer neighbors that its neighbors.

*this presents a foundational effect for many different dynamics and the study of network science*

## Adjacency Matrix
An adjacency matrix is a means for representing a graph. It is a two-dimensional matrix where each vertex is present along the horizontal and vertical. The value in each matrix position indicates whether there is an edge connecting the two vertices.

Simple connectedness between two vertices can be represented using binary values: 0 = no, and 1 = yes. For weighted graphs the value in the each matrix position represents the weight of the edge, with zero again indicating that no relation exists.

This mechanism can be applied to both undirected and directed graphs. In the case where the graph is directed, the order of indexing the matrix indicates the direction of the vertex-to-vertex relationship (i.e., which vertex is connected to the other by the edge).

A vertex's degree can be calculated from an adjacency matrix. In the case of an undirected graph, simply sum the row or column corresponding to the vertex. For a directed graph, sum the vertex's row to obtain in degree, and some the vertex's column to obtain the out degree.

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

## Breadth-First-Search (BFS) Algorithm
Breadth-first Search (BFS) is an algorithm which can serve two similar and related purposes:

(1) Finding the distance to all nodes that are "reachable" from a starting node; where reachable means that by traversing links between nodes one can navigate from the starting point to the destination.

(2) Finding the shortest distance from a starting node to a destination node.

BFS works by initializing all distances as infinity, or some other value which indicates "unknown."

Next, BFS records the distance from the starting node to itself as 0, and to each of starting node's neighbors as 1.

Then, for each neighbor compute the distance for each of its neighbors which has not yet had a distance recorded (distance is infinity or "unknown") as 1 + its own distance. Repeat this process until there are no unvisited nodes.

## Dijkstra's Algorithm

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


## Strong Ties vs. Weak Ties
> Before reading Granovetter's paper, think of ways to define "strength" of a social relationship. Then think about how to measure them. What would be your favorite measure of strength of ties? What are your justifications for that?

### Initial Discussion
Strength of a personal or social relationship is probably best measured subjectively, and mapped onto an imprecise scale: unknown, acquaintance, friend, good friend, best friend, and soul mate.

There are perhaps a set of objective questions (probably aiming towards binary answers) which could be deduced into values. Those values  would feed into a formula of weights and measures that ultimately translate to a single numeric point. Plotting that point on the imprecise spectrum will finally yield the strength of the relationship in a literal term.

Of course, this "scientific" process must leave some "wiggle room" to allow for adjusting the result up or down based on some final subjective opinion.

My personal simple system for measuring the strength of ties would answer the following questions, but not be limited or necessarily be required to have "high scores" for all: (1) how long have I known a person? (2) how many intimate details do I know about their life? (3) how often do we interact on a personal and intimate level? (4) how do each of us feel empathy for each other?

**Review**    
| Question | Answer |
| --- | --- |
| Assume that A and B are friends, and B and C are friends. Then we are sure that  A and C are friends. | False |
| Why is it less likely that a strong tie would be a bridge between social groups? | Because strong ties foster triadic closure, thereby removing their status as a bridge. |
| Weak ties foster local cohesion while strong ties foster global cohesion. | False |

> Two reasons why weak ties are strong (beneficial)   
> (1) Weak ties are bridges that lead to opportunities. But what is a bridge? A bridge is the only path between two points.   
> (2) Weak ties are strong bc they increase SOCIAL COHESION on a global scale but bad for local cohesion.   

Reference:   
https://quizlet.com/97568664/strength-of-weak-ties-flash-cards/

### Weak ties: more discussion
> 1. What's the main argument behind the "strength of weak ties", particularly regarding the job search? Do you agree? If yes, can you provide additional reasons? If no, can you argue your position?
> 2. Are there empirical studies on the strength of weak ties? Do they support Granovetter's argument?
> 3. In addition to the job searching, can there be occasions where weak ties become important or useful?

(1) The main argument behind weak ties and job search is that we spend a lot of time with those of whom we have strong ties, and the rate of "new information" (as it pertains to job opportunities, and such) is relatively low. However, when interacting with acquaintances, with whom we have weak ties, the flow of new information is much greater and more often. Thus it is the weak ties which bring the news of new job opportunities.

I tend to agree with this argument based on personal experience. In general, my best friends (those which whom I have stronger ties) and I discuss many topics but jobs and job opportunities are usually very infrequent. At a local Meetup group, where I interact with a group of peers with whom I am generally just acquainted (weaker ties) the discussion is around technology, projects, and then naturally and invariably leads to jobs and who is hiring.

(2) two studies cited by Granovetter:
- Korte's 1967 *Small World study*, and Korte + Milgram's 1970 *Acquaintance Networks*. These studies follow what we know from prior reading: a booklet is passed through a network, and at each step an indicator of "friend" or "acquaintance" is noted about the receiver. The completion rate for "friend" was lower than for "acquaintance," and thus he claims support for his argument
- the 1961 study by Rapport + Hovarth, *Large Sociogram*; this study analyzed the social connectivity from an ordered list of best friends. The smallest number of connections were made from the first and second choices: presumably the strongest friendships (ties). The greatest number of people were reached through the seventh and eighth choices, presumably much weaker ties.

(3) The importance/usefulness of weak ties can be extended beyond professional and career networking. Introducing people for possible romantic relationship would seem to be a logical extension of this. Out of a desire not to create an issue or tension in a triadic form, one would probably only introduce people with whom we have weak ties. This point (about triadic tension) is one of Granovetter's first points.


# Random Networks
<u>Definition</u>: *A random network consists of N nodes where each node pair is connected with p probability.*

To construct a random network, follow these steps:

1. Start with N isolated nodes
2. Select a node pair and generate a random number between 0 and 1. If the number exceeds *p*, connect the node pair, otherwise leave them disconnected.
3. Repeat step 2 for each of the $\frac{N(N-1)}{2}$ node pairs.

**Review**
| Question | Answer |
| --- | --- |
| Suppose someone generated an Erdos-Renyi random graph with N=500 and p=0.03, what would the (theoretical) expected average degree of the network be?  | 14.97  |
| Suppose someone wanted to find the expected number of links in the same graph (N=500, p=0.03). What would they get?  | 3742.5  |
| Suppose I wanted to generate an Erdos-Renyi random graph that has 250 nodes with an average degree of 6. What would I choose for the connection probability p?  | 0.024  |

See: `week-04/random-networks.ipynb`

## Degree Distribution
In a given realization of a random network some nodes gain numerous links, while others acquire only a few or no links. These differences are captured by the degree distribution *p<sub>k</sub>* which is the probability that a randomly chosen node has degree *k*.

### Binomial distribution
In a random network the probability that node *i* has exactly *k* links is the product of three terms... [Barabasi, 3.4.1]

The degree distribution of a random network follows the binomial distribution:

$$p_{k} = \binom{N-1}{k}p^{k}(1-p)^{N-1-k}$$

### Poisson Distribution
Poisson is not an exact formula, but it is a really good approximation when *N* is large. It is sometimes called: *The Limit of Rare Events*, and it is generally denoted as:

$$P(x)=\frac{\mu ^{x}}{x!}e^{-\mu}$$

where the average total number of events is $\mu$.   
Reference: https://www.youtube.com/watch?v=C6x0n3AbuwM

For networks we use this formula:

$$p_{k}=e^{-\left \langle k \right \rangle}\frac{\left \langle k \right \rangle^{k}}{k!}$$

Describes the number of events that occur in constant rate independently. Poisson is not about discrete trial, but rather things that happen in continuous time.

Rationale behind why we can use Poisson to approximate Binomial distribution:
- large *N* acts like *continuous time*
- *k* events acts like *rate*

Additional notes:
- Poisson is easy to calculate
- Binomial Distribution is harder to calculate

See also: [Barabasi, 3.4.2]

# The Small World Phenomenon
Small-world Phenomena is a means to show how interconnected networks really are, no matter their size. The basic tenet is that on average any two nodes in a network are likely to be connected and they are really not that far away from each other.

This principle has been demonstrated repeatedly on social networks, where there is a high likelihood that any two randomly selected individuals can be connected to each other through their friendship or professional networks in no more than 6 links on average. Hence, the proliferation of the term Six Degrees of Separation.

A social network exhibits the small-world phenomenon if, roughly speaking, any two individuals in the network are likely to be connected through a short sequence of intermediate acquaintances. [https://www.cs.cornell.edu/home/kleinber/swn.d/swn.html]

Six degrees of separation is the idea that all living things and everything else in the world are six or fewer steps away from each other so that a chain of "a friend of a friend" statements can be made to connect any two people in a maximum of six steps. It was originally set out by Frigyes Karinthy in 1929 and popularized in an eponymous 1990 play written by John Guare. [https://en.wikipedia.org/wiki/Six_degrees_of_separation]

The small-world experiment comprised several experiments conducted by Stanley Milgram and other researchers examining the average path length for social networks of people in the United States. The research was groundbreaking in that it suggested that human society is a small-world-type network characterized by short path-lengths. The experiments are often associated with the phrase "six degrees of separation", although Milgram did not use this term himself. [https://en.wikipedia.org/wiki/Small-world_experiment]

## Discussion

The discovery by the the Milgram experiment that people can be connected on average by only several steps is a surprising result, or is it? One can come up with reasons for both sides: is the small world phenomenon and Milgram's results surprising or trivial?

1. Find reasons why they are surprising.   

    Without knowing the principles behind the Small World Phenomenon, it seems quite counterintuitive; especially as the physical distance between the two (source and target) is increased. One might believe that in a local area -- such as Boston, Cambridge, and stretching into the eastern Massachusetts suburbs -- that the number of links between source and target would be small, certainly 5 or fewer. This might even hold true for a larger regional area: for example the territory covered by New England, New York, and perhaps stretching into the nearer Mid Atlantic states.

    It would seem that this would not hold outside the local area and regional areas. Once entering into a national level (the size of the United States of America) and certainly into the global level, it would seem that more links would be needed to connect source and target.

    However, Milgram's experiment has shown that distance -- even in the 1960s, long before the advent of the Internet and even fundamental electronic means of communication (i.e., email) -- is not really a factor.

2. Find reasons why they are not surprising.

   Social circles are not limited to a proximity. They can extend far beyond where a source and target live.

   All life experiences -- school, university, employment, spiritual and religious, and other extracurricular activities -- expose us to new and different people, whom we befriend (for a reason, a season, or a lifetime) and even the briefest of these can be reignited in a moment. This seems especially true as more and more families move around, and college is less and less just a "local" group of students.   

3. Which one is more convincing to you and why?

   I tend to believe this is not surprising. After a considerable amount of thought, and re-reading some of the Milgram paper, I just found it more believable; even before the dawn of the Connected-through-the-Internet age.

4. There are some critical limitations of Milgram's study. Discuss the limitations of Milgram's experiment. How can you design a better experiment if you do it now?

   One could argue that the two places of origin were very similar due to their close proximity: Kansas and Nebraska. Also, both of the targets were in the Boston, Massachusetts area. To be perhaps more "random," the sources and destinations could be 4 different places. And, perhaps one route should travel west and one should travel east; or the general travel direction should not be the same for both groups.

   Milgram himself also alluded to a follow-up study which would cross more socio-economic boundaries (race, ethnicity, education, and employment).

   A different experiment, with an aim to explore the socio-economic boundaries, might involve more routes (i.e., targets) and more source places trying to reach the same target.

5. What would be real-world implications of small-worldness and 6 degrees of separation?

   In general, the small-world phenomenon implies a certain level of connectedness between almost all people in the world. What this may mean -- in a real life situation -- is that two strangers that meet in an airport lounge could sit down over a cup of coffee and talk for an hour (or so) and find a path of 6 or fewer friends which connect them.

6. (Optional) Share any funny or interesting small-world episodes that you have experienced and suggest an explanation for this result.

## Understanding Small World Phenomenon

### Trivial?
- You have 100 friends
- each of them have 100 friends
- and each of them have 100 friends
- and so on...

Consider the mathematics of this:   
`100 x 100 x 100 x ...`

Very quickly -- by growing exponentially at each stage -- grows into a very large number; well into the millions and billions with a relatively small number of steps.

### Surprising?
It doesn't work like that in real life. It would only work if there was no overlap in each of the friend circles. In real life, you and each of your friends will have friends in common. There is generally a lot of overlap between friends and friends of friends. Given this, the multiplication factor will be much smaller than the example given above.

## References
The Science of Six Degrees of Separation
- https://www.youtube.com/watch?v=TcxZSmzPw8k

-----
# Network of The Week

## January 29, 2018
Network of The Week (Jan. 29, 2018 submission)

**Who owns everything in Big Media today**

https://www.recode.net/2018/1/23/16905844/media-landscape-verizon-amazon-comcast-disney-fox-relationships-chart

The nodes are the content providers and the distributors (i.e., cable TV providers) and internet streaming video services.

The links are directed, and show the percent stake one has in the other.

This network shows some interesting relationships developing between the distributors and providers. The big distributors are either outright buying content provider or investing a stake in one. This is in reaction to companies like Netflix, Hulu and Amazon making their way into both sides of the market sort, but also remaining "distributor agnostic."

The network is really beginning to move from very disconnected, to a more connected network. In time we should expect more links between nodes.

-----

# Slightly Off-Topic Notes

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

-----

# Extraneous Learned Items

**ideal gas**   
noun *Chemistry*   
- a hypothetical gas whose molecules occupy negligible space and have no interactions, and that consequently obeys the gas laws exactly.

-----
# Schedule

## Week 0
- On Motivation
- Misconceptions
- Self Assessment

## Week 1
- Networks
- Complex Systems
- The emergence of *Network Science* as a field of study and discipline

## Week 2
- Graph Theory (intro)
- Adjacency Matrix
- Friendship Paradox

## Week 3
- Breadth First Search
- Dijkstra's Algorithm
- Clustering
- The Small World Phenomenon

## Week 4
- strong ties vs. weak ties
- random graphs and their properties
- the Watts-Strogatz network model

-----
# Glossary

| Term | Definition |
| --- | --- |
| complex system   |  ? |
| edge   |  ? |
| graph   |  ? |
| link   |  ? |
| network  | ?   |
| node   |  ? |
| vertex   |  ? |

-----
# References

[barabasi]  

[codecogs]  https://latex.codecogs.com

[html-math]

Heavy Tailed Degree Distributions
- https://networkedworld.wordpress.com/2012/10/19/heavy-tailed-degree-distributions/

Links for math equations in Markdown:
- https://stackoverflow.com/questions/11256433/how-to-show-math-equations-in-general-githubs-markdownnot-githubs-blog
- http://sites.psu.edu/symbolcodes/codehtml/#math
- https://www.keynotesupport.com/websites/greek-letters-symbols.shtml
- https://www.mathjax.org
-

http://www.cs.cornell.edu/home/kleinber/networks-book/

https://www.cs.cornell.edu/home/kleinber/swn.d/swn.html
