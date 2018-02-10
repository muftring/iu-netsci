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

The degree distribution of a *Random Network* is characterized by the Poisson Distribution.

## Further Notes
In a Random Network highly connected nodes, or *hubs*, are effectively forbidden. 
