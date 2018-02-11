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

## Review
| Question | Answer |
| --- | --- |
| We can expect that the degree of a randomly chosen node from a network with a power-law distributed degree distribution will be comparable to the mean of the distribution.   | False  |
| Calculate the approximate N-dependent term of the distance for a random graph with N=3e10 nodes.   | 24.12  |
| Calculate the approximate N-dependent term of the distance for a scale-free graph with N=3e10 nodes and a degree exponent of 2.5.   | 3.18  |
| Scale-free graphs with degree exponents less than 2 is not well-defined, particularly in the limit where the number of nodes goes to infinity.   | True  |
