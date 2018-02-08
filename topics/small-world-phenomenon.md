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

## Watts-Strogatz
See: reading

> Small-world is characterized by their distinctive combination of high clustering with short path lengths.
>
> exploration of simple models [...] where regular networks are  'rewired' to introduce increasing amounts of disorder. [...] these systems can be highly clustered, like regular lattices, yet have small path lengths, like random graphs.

The Watts-Strogatz model incorporates idea of strong ties and weak ties. The conflict between Path Length *L* and Clustering *C* can be resolved because of their different properties.

You can maintain the Clustering Coefficient because it is local. Having weak ties does not affect Clustering Coefficient very much. The benefit of weak ties creating short-cuts is that they drastically and rapidly decrease the Average Path Length.

**Review**
| Question | Answer |
| --- | --- |
| Which best describes the graph generation procedure for the Watts-Strogatz model:   | Begin with a lattice and rewire edges with probability p   |
| In Figure 2 why does path length decrease much faster than the clustering coefficient for small p?   | Rewiring just several links can connect distant neighborhoods, drastically decreasing the path lengths between all nodes in the neighborhood. But this process has only a linear effect on clustering.  |

## References
The Science of Six Degrees of Separation
- https://www.youtube.com/watch?v=TcxZSmzPw8k
