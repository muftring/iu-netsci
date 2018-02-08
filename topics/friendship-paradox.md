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

-----

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
