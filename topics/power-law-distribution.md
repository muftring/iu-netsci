# Power-Law Distribution
Plotting on a log-log scale, the curve will appear as a "straight" line decreasing linearly.

The power-law distribution:

$$p_k \sim k^{-\gamma }$$

The exponent $\gamma$ is its *degree exponent*.

Take the logarithm of this produces:

$$lm\,p_k \,\sim\, -\gamma\,lm\,k$$

$lm\,p_k\,$ is expected to depend linearly on $lm\,k$, meaning the slope of this line beig the degree exponent $\gamma$.

When *x* is small, the value is larger. As *x* grows, the distribution value decreases... (see plot)

## Zipf's Law
> Zipf's law (/ˈzɪf/) is an empirical law formulated using mathematical statistics that refers to the fact that many types of data studied in the physical and social sciences can be approximated with a Zipfian distribution, one of a family of related discrete power law probability distributions.

Reference: https://en.wikipedia.org/wiki/Zipf%27s_law

It is a discrete form of the continuous Pareto distribution, from which we get the Pareto Principle.

Reference: https://www.youtube.com/watch?v=fCn8zs912OE&ab_channel=Vsauce

## Pareto Distribution
> The Pareto distribution, named after the Italian civil engineer, economist, and sociologist Vilfredo Pareto, is a power law probability distribution that is used in description of social, scientific, geophysical, actuarial, and many other types of observable phenomena. Originally applied to describing the distribution of wealth in a society, fitting the trend that a large portion of wealth is held by a small fraction of the population, the Pareto distribution has colloquially become known and referred to as the Pareto principle, or "80-20 rule". This rule states that, for example, 80% of the wealth of a society is held by 20% of its population. However, the Pareto distribution only produces this result for a particular power value,
 $\alpha$. While $\alpha$  is variable, empirical observation has found the 80-20 distribution to fit a wide range of cases, including natural phenomena and human activities.

Reference: https://en.wikipedia.org/wiki/Pareto_distribution

### Pareto Principle
> The Pareto principle (also known as the 80/20 rule, the law of the vital few, or the principle of factor sparsity) states that, for many events, roughly 80% of the effects come from 20% of the causes.

Reference: https://en.wikipedia.org/wiki/Pareto_principle


## Discussion
Many distributions have the same or similar decay as the Power Law. What makes Power Law special?

- take the log
- plot $ln \, p(x)$ and $ln \, x$
- you get a linear function

In log scale it shows a **straight line**.

Exponential function plot has curved plot, and quicker decaying tail.

Power Law has *heavy tail* or *fat tail*. The **tail** is a really important property of the Power Law distribution. Many other distributions do not have this kind of tail. What this means is we get to see a lot of **outliers** with Power Law distribution.

> Black Swan: something so rare, but when it happens is has a tremendous effect!

In Power Law "world," there is no *Black Swan* - you can expect something extreme to happen frequently.

Example:
- income distribution or wealth distribution
- not perfect Power Law, but has Power Law tail
- there are millionaires and billionaires

The *Normal Distribution* does not have a fat tail.

Example:
- height
- median of 5'10" (170 cm)
- a few standard deviations ($\sigma$) out
- you don't often see people 2 m tall
- almost never see a 3 m tall person
- quickly approaches zero
- effectively becomes zero a few $\sigma$ out

Reference: Six Sigma (link)

The **fat tail** has significant probability to observe something large in the distribution. In normal distribution the probability is effectively zero.

Next is the **scale free** property. This means that there no characteristic scale in the distribution.

In normal distribution there is a characteristic scale which is defined by the mean ($\mu$) and the variance ($\sigma$) -- or standard deviation.

## Examples:

### Power Law
> These are some examples of distributions in nature or society that follow heavy-tailed, fat-tailed, or power-law distributions

1. <u>Taylor's law</u> which describes the spatial clustering of organisms; this law relates the variance of the number of individuals of a species per unit area of habitat to the corresponding mean by a power law relationship (ref: https://en.wikipedia.org/wiki/Taylor%27s_law)
2. <u>The Red Queen hypothesis</u> is an evolutionary hypothesis which proposes that organisms must constantly adapt, evolve, and proliferate not merely to gain reproductive advantage, but also simply to survive while pitted against ever-evolving opposing organisms in an ever-changing environment (ref: https://en.wikipedia.org/wiki/Red_Queen_hypothesis)
3. <u>Pink Noise</u> is a signal or process with a frequency spectrum such that the power spectral density (energy or power per frequency interval) is inversely proportional to the frequency of the signal. In pink noise, each octave (halving/doubling in frequency) carries an equal amount of noise energy. (ref: https://en.wikipedia.org/wiki/Pink_noise)

### Non Power Law
> And several that do not.

1. Human physical characteristics like height and weight; these tend to follow a Normal distribution
2. Data Compression: The trick is to find out the distribution pattern of the alphabets and assign the shortest code to alphabet with highest frequency of occurrence and the longest to smallest frequency of occurrence. (ref: http://www.discover6sigma.org/post/2006/10/distribution-in-real-life/)

### Discussion Remarks
> Are there any patterns in these two sets? Are there any common properties shared by each of the set?  

One difference seems to be that the power law examples do not have a real or practical bound to their values. Whereas the non power law examples are bounded in reality or practicality. Maybe there is a magnitude indicator? For example, in the case of Taylor's Law where the principle is applied to clustering of organisms, the number of different types of organisms in the world is quite large - likely in the billions or even higher. And in the case of data compression, there are real and practical sizes of alphabets and words which number in the hundreds to thousands.

## Review
| Question | Answer |
| --- | --- |
| If you have a power-law distribution, plotting it in log-log scale will ...   | Turns it into a straight line.   |
| What is the main difference between a Poisson and power-law distribution (~x^-a with 2<a<3)?   | You expect to see huge values (outliers) in a power-law distribution  |
| Are poisson distributed networks scale-free?  | No. (False)  |
