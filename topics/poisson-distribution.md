# Poisson Distribution
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
