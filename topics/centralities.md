# Centralities
*Measuring Importance*

## Introduction

- why and when do we want to characterize nodes, links, and other objects in networks?
- what are the key ideas behind network centralities?
- Degree-based centralities:
  - Degree
  - Eigenvector
  - Katz
- Random-walk based centralities: PageRank
- Distance-based centralities: Closeness
- Communication-based centralities: Betweenness

*How can we operationalize 'importance'?*
- degree is just one way
- in many cases degree can become useless
  - social media: following and followers
  - accounts/users/people who simply try to obtain large numbers
  - there is no content
  - concern is on quantity of followers, not quality

**Why?**
- why do we want to measure centralities?
- why do we want to find important nodes or links in a network?

**Basic Ideas**
- what are the fundamental ideas behind these measures?
- often then are really simple ideas
- sometimes those simple ideas can give a lot of information about the network
  - and individual nodes and edges

**How to apply?**

## Discussion

**What does it mean to be important?**
> So, the question is, what does it mean to be **important** in a network? Why do we want to define and identify those important nodes, links, and so on? Please share your thoughts by picking a couple of networks and suggesting several ways to think about the importance of a node, an edge, or any network object. Feel free to discuss how you could define measures of importance.

The human organ network is perhaps a very interesting example to consider here, and it is also a very tricky network to provide a definitive answer to importance.

At a high level, some of the nodes in the human organ network would be: the brain, heart, lungs, stomach, intestines, liver, kidneys, and so on. The links might be blood vessels (arteries and veins), lymph nodes, and some portions of the digestive tract (esophagus, intestines).

Which is most important?

A quick thought might be to answer the brain. After all, this organ is what controls almost everything; without it a human cannot function.

However, the brain cannot function without oxygen which is provided by blood flow. The blood is oxygenated by the lungs and the heart is the pump which circulates blood throughout the body.
So, is the heart or are the lungs more important?

What about all of the complicated mechanisms in the digestive and related organs? Without ingestion of food and water, there is no energy to propel cells to function... in every organ, and in every far reaching place of the human body.

In the case of the human organ network, importance must take on several different measures relative to necessity of function relative to the different aspects of survival.

Ultimately, the brain is probably the most important organ because it does control both voluntary actions (eating, drinking, social contact, awareness of surroundings) and involuntary actions (breathing, heart beating, metabolism, survival instinct) of the human which are necessary for survival. The brain is dependent on many other organs, and there is a multifaceted symbiotic relationship, but ultimately they cannot function without the brain's "orders."
