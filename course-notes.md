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

### Basic Components
- vertices, nodes
- edges, links

`N` = number of nodes, or size of the graph   
`L` = the number of links   
`k` = the *degree* of a node

### Types
- links can be directed or undirected
- directed graphs are called *digraphs*

### Utility
in order to apply network theory to a system, careful consideration must precede our choice of nodes and links, ensuring their significance to the problem we wish to explore

### Degree
A key property of each node is its *degree*, denoted by `k`; this represents the number of links a node has to other nodes.

The total number of links `L` can be expressed as the sum of node degrees `k`:

$$L = \frac{1}{2} \sum_{i=1}^{N}k_{i}$$

The 1/2 factor corrects for the fact that each link will be counted twice, once from each node it connects.

#### Average Degree
The *average degree*, denoted `<k>`, can be derived as:

$$\left \langle k \right \rangle = \frac{1}{N}\sum_{i=1}^{N}k_{i} = \frac{2L}{N}$$

We have a factor of 2 here (in the simplified form) because every edge is counted by two nodes.

<u>Question:</u> Why do we want to know the average (mean) degree of a network?
- it gives us a good sense of *density* of the graph
- if the average degree is very small, or less than 1, then there should be a lot of nodes without any connections
- if the average degree is very big, approaching the number of nodes in the network, then we should see that the network is very dense, and almost *completely connected*

#### Degree Distribution
The *degree distribution*, denoted p<sub>k</sub>, provides the probability that a randomly selected node in a network has degree `k`. Since P<sub>k</sub> is a probability, it must be normalized:

$$\sum_{k=1}^{\infty}P_{k} = 1$$

For a network with `N` nodes, the degree distribution is the normalized histogram given by:

$$P_{k} = \frac{N_{k}}{N}$$

where N<sub>k</sub> is the number of degree-`k` nodes.

### Weight
A value `w` is associated with the links

### Strength
The sum of all weights `w` for links connected to the node, denoted as `S`.

### Directed
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

## Real Networks are Sparse

## Weighted Networks

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
