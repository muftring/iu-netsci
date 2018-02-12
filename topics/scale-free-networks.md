# Scale-Free Networks
Why many real networks are very different from Poisson distribution.

Why is it important to have *hubs*?

## Hubs
*Hubs* are highly connected nodes; a node that possesses an exceptionally large number of links is called a hub.

Hubs are not unique the the Web (WWW); they are encountered in most real networks.

### The Largest Hub
<u>Question</u>: How does the network size affect the size of its hubs?

To answer this we calculate the maximum degree, $k_{max}$, called the *natural cutoff* of the degree distribution $p_k$. It represents the expected size of the largest hub in a network.

For a scale-free network the natural cutoff is:

$$k_{max}=k_{min}N^\frac{1}{\gamma^-1}$$

the larger a network, the larger is the degree of its biggest hub

## Scale-Free Property
There is a deeper organizing principle which is representative of *hubs*. We call this the scale-free property. The *degree distribution* of real networks thus becomes very important; it allows us to uncover and characterize scale-free networks.

## Scale-Free Network
<u>Definition</u>: a *Scale-Free Network* is a network whose degree distribution follows a *Power Law*.

## Discussion
One really important, but hidden, assumption in the Watts-Strogatz model is that "people are more or less similar."

Hollywood Movie Actor Network analysis

Watts-Strogatz:
- distance
- path length
- clustering
- did not consider heterogeneity of the nodes of the graph
- did not measure the degree distribution

Barabasi-Albert-Jeong:
- looked at the degree distribution

> For *degree distribution*, the Poisson distribution is expected when you assume Erdos-Renyi (ER) random graph.

**Heterogeneous vs. Homogeneous**   
There is a distinction between highly homogeneous networks like Erdos-Renyi random networks, and highly heterogeneous networks with fat-tail or clear Power-Law distribution.

Expect to see small deviation from the mean in terms of the degree when we assume homogeneous random network.

But for real networks, the standard deviation of the degree is very large. This means they are very heterogeneous. The degree distribution is often highly heterogeneous and many networks tend to have hubs.

When the network is highly heterogeneous and whne it follows the Power-Law distribution, an interesting thing happens with the small-world phenomenon.

For random networks, the path length scales as ln(N).

What happens when the network becomes scale free and starts to have hubs, it becomes *ultra-small world* and the path length scales as ln(ln(N)) and the exponent is between two and three (2 < $\gamma$ < 3).

**The Meaning of the Exponent**
https://youtu.be/Q4hoRENRCwA?t=546

## Ultra-small Worlds
> Ultra-small world, how is it possible?<P>
So, apparently the scale-free networks can achieve "ultra-small" world. What would be conceptual mechanisms behind this phenomenon? What would be the 'shortcuts' in scale-free networks? Can you explain it in your own terms?

Hubs.

Barabasi tells us: "hubs radically reduce the distance." And the way they do this is by connecting to many others nodes with smaller degree. This in essence creates a node from which a vast number of other nodes are directly reachable, or perhaps reachable with one hop beyond the hub. If a node is directly connected to the massively connected hub or is itself one hop away from that hub, then the distance from that node to virtually every other node is drastically reduced.

### Ultra-small world: what would be the extreme case?
Given the number of nodes and edges, how small can you make the network?

If you have a lot of edges, you can create *fully connected* graph (everyone is connected to everyone, and the average path length is 1).

But, we know that *real networks* are **sparse**!

If you only have a small number of edges, what can you do? The obvious answer is to create a *star graph* where everyone is connected to a central node, a **hub**, and everyone can reach everyone else in 2 steps by going through the hub. The number of edges you need is $N - 1$, and the graph is extremely sparse and we are super efficient in reaching other nodes.

Scale-Free networks take it a step further. It is a "relaxed" version of the star graph. There are several hubs connected to many nodes, and the hubs are also connected to each other. This drastically reduces the average path length.

## Review
| Question | Answer |
| --- | --- |
| We can expect that the degree of a randomly chosen node from a network with a power-law distributed degree distribution will be comparable to the mean of the distribution.   | False  |
| Calculate the approximate N-dependent term of the distance for a random graph with N=3e10 nodes.   | 24.12  |
| Calculate the approximate N-dependent term of the distance for a scale-free graph with N=3e10 nodes and a degree exponent of 2.5.   | 3.18  |
| Scale-free graphs with degree exponents less than 2 is not well-defined, particularly in the limit where the number of nodes goes to infinity.   | True  |
