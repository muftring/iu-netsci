# Scale-Free Networks
Why are many real networks very different from Poisson distribution?

Why is it important to have *hubs*?

## Hubs
*Hubs* are highly connected nodes; a node that possesses an exceptionally large number of links is called a hub.

Hubs are not unique to the Web (WWW); they are encountered in most real networks.

### The Largest Hub
<u>Question</u>: How does the network size affect the size of its hubs?

To answer this we calculate the maximum degree, $k_{max}$, called the *natural cutoff* of the degree distribution $p_k$. It represents the expected size of the largest hub in a network.

For a scale-free network the natural cutoff is:

$$k_{max}=k_{min}N^\frac{1}{\gamma^-1}$$

the larger a network, the larger the degree of its biggest hub

## Scale-Free Property
There is a deeper organizing principle which is representative of *hubs*. We call this the scale-free property. The *degree distribution* of real networks thus becomes very important; it allows us to uncover and characterize scale-free networks.

## Scale-Free Network
<u>Definition</u>: a *Scale-Free Network* is a network whose degree distribution follows a [*Power Law*](power-law-distribution.md).

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

When the network is highly heterogeneous and when it follows the Power-Law distribution, an interesting thing happens with the small-world phenomenon.

For random networks, the path length scales as ln(N).

What happens when the network becomes scale free and starts to have hubs, it becomes *ultra-small world* and the path length scales as ln(ln(N)) and the exponent is between two and three (2 < $\gamma$ < 3).

[The Meaning of the Exponent](https://youtu.be/Q4hoRENRCwA?t=546)

## Ultra-small Worlds
> Ultra-small world, how is it possible?<P>
So, apparently the scale-free networks can achieve "ultra-small" world. What would be conceptual mechanisms behind this phenomenon? What would be the 'shortcuts' in scale-free networks? Can you explain it in your own terms?

Hubs.

Barabasi tells us: "hubs radically reduce the distance." And the way they do this is by connecting to many others nodes with smaller degree. This in essence creates a node from which a vast number of other nodes are directly reachable, or perhaps reachable with one hop beyond the hub. If a node is directly connected to the massively connected hub or is itself one hop away from that hub, then the distance from that node to virtually every other node is drastically reduced.

### Ultra-small world: what would be the extreme case?
Given the number of nodes and edges, how small can you make the network?

If you have a lot of edges, you can create *fully connected* graph: everyone is connected to everyone, and the average path length is 1.

But, we know that *real networks* are **sparse**!

If you only have a small number of edges, what can you do? The obvious answer is to create a *star graph* where everyone is connected to a central node, a **hub**, and everyone can reach everyone else in 2 steps by going through the hub. The number of edges you need is $N - 1$, and the graph is extremely sparse and we are super efficient in reaching other nodes.

Scale-Free networks take it a step further. It is a "relaxed" version of the star graph. There are several hubs connected to many nodes, and the hubs are also connected to each other. This drastically reduces the average path length.

### Conclusion
Considering: *Friendship Paradox and hubs...*

Because we can very quickly reach hubs, the expansion of the tree (neighbor's links, neighbor's neighbors links) becomes much larger than what you expect from $\left \langle k \right \rangle$. It actually scales much more like $\left \langle k^2 \right \rangle$, because once you traverse to a neighbor the degree you expect is proportional to the $k^2$ average. That means as you traverse each step, you reach a lot of nodes very quickly.

That is the explanation of scale-free networks, friendship paradox, and ultra-small world.

## Robustness
Scale-free networks are really robust against random failures. Evaluating $d$ (diameter) as the measure of impact to two types of faults.

**Failure**: randomly select a node and remove it

**Attack**: remove the node with the highest degree

In a *random graph* (exponential graph) the behavior is the same under both types of faults. The diameter is effectively unchanged. Pretty much every node has the same degree, so removing a random node or the node with highest degree has the same effect.

However, for *scale-free networks* the behavior is different. Under attack, the scale free network quickly breaks down. But under random failure it is very robust: the diameter does not change even after removing many nodes.

### Summary
- **Random Network** (exponential network) is fragile under both *failure* and *attack*; if you start to remove nodes you destroy the network very quickly
- **Scale-Free Network** is fragile under *attack*, by removing the hubs it quickly breaks down; but it is very robust against *failure*. Considering random failure: the likelihood that a hub is randomly selected is much smaller than the likelihood that a node with small degree is selected simply because the hubs are greatly outnumbered by the small degree nodes.

### Discussion

>Small-world and robustness in real-world<P>
In airline networks, there are "hubs" that makes the whole network "small" so that you can reach almost everywhere in the world by only few steps. Also these hubs provide robustness for the whole network (as long as they are functioning). <P>
> What would be other interesting networks that exhibit these two properties (esp. through hubs)? Explain how important it is to have the small-world property and robustness in the network that you're talking about.  

A first thought is the cargo and goods delivery network would seem to be similar to the airline network. The hubs would be the large ports in all the world's large coastal regions. In the United States cities like New York, Houston, Los Angeles, and Seattle come immediately to mind. If these ports (and the next ones in line, by size) were to stop functioning, then the movement of cargo and goods would quickly break down.

Blood delivery in the human body also seems like it could be a small-world like network. The places where arteries and veins meet would be the nodes, and the larger of those would be the hubs. The smaller connected nodes would be capillaries and such. If the larger hubs break down (or stop functioning) then the blood delivery network would break down rather quickly, and with serious consequences.

# Review
| Question | Answer |
| --- | --- |
| We can expect that the degree of a randomly chosen node from a network with a power-law distributed degree distribution will be comparable to the mean of the distribution.   | False  |
| Calculate the approximate N-dependent term of the distance for a random graph with N=3e10 nodes.   | 24.12  |
| Calculate the approximate N-dependent term of the distance for a scale-free graph with N=3e10 nodes and a degree exponent of 2.5.   | 3.18  |
| Scale-free graphs with degree exponents less than 2 is not well-defined, particularly in the limit where the number of nodes goes to infinity.   | True  |
| Scale-free networks with power-law degree distribution tend to also exhibit the small-world property.    | True  |
| If the degree distribution of a finite network follows a power-law with exponent between -2 and -3, the mean degree of the network will be larger than a random (E-R) network with the same number of nodes.    | False  |
| Assume that you find a network that follows a clear power-law degree distribution with exponent -3 (as predicted by BA model). This does NOT automatically mean that...   | [1] the network is created through the preferential attachment process. <br> [2] the network has hubs with large degree. <br> [3] the network is very likely to be a small-world. <P><P> The correct answer is [1]: <br> *Not necessarily! Even if there is a model that explains the observed result, it does not mean that the real system follows the model exactly. There can be numerous alternative mechanisms to generate a power-law degree distribution.* |

**Notes:**
1. the mean of a power-law distributed degree distribution will tend to be much larger than the degree of most randomly chosen nodes; the high degree of the *hubs* will drive the mean value up, and most nodes will have a degree much smaller than the mean
2. for the calculations in questions 2 and 3, see the *Exploring* notebook (in References)

# References
- [Barabasi, chapter 4](http://networksciencebook.com/)
- Ultra-Small World (property): Barabasi, section 4.6
- [Exploring: Power-Law (notebook)](https://github.com/muftring/iu-netsci/blob/master/exploration/power-law-explorations.ipynb)
