# Distributions

## Introduction

## Overview
- [Binomial Distribution](binomial-distribution.md)
- [Poisson Distribution](poisson-distribution.md)
- [Power-Law Distribution](power-law-distribution.md)

## Discussion
In Binomial, Poisson, and Gaussian distributions we expect a certain scale. The tail will taper off very fast, and after a certain point we do not expect anything.

In the case of Power-Law distribution, it is different: the tail does not taper off to zero (within sight, but probably eventually?) and you cannot ignore outliers in the tail. There is also no characteristic scale in the distribution.

Reference: [barabasi, chapter 4]

## Binomial, Poisson, Gaussian
Looking at connections and similarities of these distributions.
- these are more or less similar
- they share properties
- they quickly decay

### Binomial
$$f(k; n, p) = Pr(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k}$$

Consider a coin toss:
- the probability of *Heads* = P
- the probability of *Tails* = 1 - P

In the network context we consider a *node* and a collection of other nodes, and consider each edge as a coin toss. We connect to other nodes based on the result of the coin toss. The number of edges a node will get will follow the Binomial Distribution.

With a large *N*, we can consider is as a Poisson Distribution.

### Poisson
$$P\left ( k\, events\, in\, interval \right ) = \frac{\lambda ^{k}e^{-\lambda}}{k!}$$

The Poisson Distribution describes events in a given interval.

> Bus example:<P>
> If you are waiting for a bus in a station, and on average two busses arrive each hour.<P>
> Given that, what is the *expected* number of busses during an hour of waiting time?

If *N* is much larger than average degree \<k\>, then this can be considered as continuous time. There are so many nodes as candidates, and the event -- link --  only happen occasionally. Continuous event with fixed expected rate (e.g., arrival of bus, or connection of a node).

Poisson is easier to work with compared to Binomial because of the tricky combinatorial factor in the Binomial. For Poisson, we can simply plug in the numbers.

### Gaussian (Normal)
$$f(x\,|\,\mu , \sigma ^{2}) = \frac{1}{\sqrt{2\sigma ^{2}\pi}}e^{-\frac{(x-\mu)^2}{2\sigma ^{2}}}$$

How is Poisson similar to Gaussian? (They look very different.)

When there are a lot of events across an interval it can be considered Gaussian.

The reasoning: the interval can be counted as smaller intervals, then add up each of the smaller intervals and consider it the larger interval. That means *The Central Limit Theorem* is in place and we can now think of this as a Gaussian (or Normal) distribution.

The formula looks complicated. But reducing and simplifying we can "remove" the standard deviation, the variance, the mean value... Essentially we can reduce to:

$$\sim e^{-x^2}$$

If we increase *x*, $\mu$ will decrease as $\sim e^{-x^2}$, so it will decrease very fast and quickly reach zero.

## More Details
https://www.johndcook.com/blog/normal_approx_to_poisson/
