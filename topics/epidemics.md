# Network Epidemics
*Spreading Process*

What is an *epidemic*? The word is from Greek, and translates as:
- epi: upon
- demos: people

meaning: *something happening upon people*

An epidemic usually describes infectious disease spreading across the population.

Why do we care?

Studying epidemics helps us understand **spreading processes**:
- human disease
- computer virus, internet worm
- diffusion of information
- spreading of rumors (e.g., on social media)
- spreading ideas and information
  - collaboration
  - citation

History of human disease epidemics:
- The Great Plague (in Europe from 1347 to 1351)
- 1918 Spanish Flu
- HIV (1990s)
- SARS (early 2000s)
- H1N1 Flu

This becomes much more dangerous and important because we are getting much more connected.
- a high population density (in cities)
- plus high mobility (air travel)
- <u>equates to</u>: perfect conditions for epidemic spreading

Population density matters (a lot) because it provides the fuel where the infectious disease is the fire.
- small, separate (unconnected) population will burn the "local fuel" and cause the fire to "die out" (think: hunter-gatherer society, wild animals)
- large (highly populated) cities are strongly connected to other cities and so the chance for spread of disease is great (almost perfect)

Mobility matters (also)
- the speed of a spreading process is limited by the speed of human travel
- the faster the means of travel
- the further the reach of transportation
- <u>equates to</u>: increased mobility

Spreading always means Connections
- network structure plays important role in any spreading process
- for disease, and for information
- copy without loss

# Spreading Phenomena
(Barabasi, chapter 10)

## Introduction
*super-spreader*: an individual who is responsible for a disproportionate number of infections during an epidemic

super-spreaders are hubs in network terminology; nodes with an exceptional number of links in the contact network on which a disease spreads

*network epidemics*: a framework which offers an analytical and numerical platform to quantify and forecast the spread of infectious diseases (understand and predict the true impact of these hubs)

spreading processes obey common patterns and can be described using the same network-based theoretical and modeling framework

> The spread of a pathogen, a meme or a computer virus is determined by the network on which the agent spreads and the transmission mechanism of the responsible agent.

## Epidemic Modeling
Epidemiology has developed a robust analytical and numerical framework to model the spread of pathogens. This framework relies on two fundamental hypotheses:

**Compartmentalization**<BR>
an individual can be in one of three states or compartments:
- susceptible
- infectious
- recovered

There may be further classifications:
- immune individuals: who cannot be infected
- latent individuals: who have been exposed to the disease, but are not yet contagious (or infected)

**Homogenous Mixing**<BR>
The homogenous mixing hypothesis (also called fully mixed or mass-action approximation) assumes that each individual has the same chance of coming into contact with an infected individual.

assumption: anyone can infect anyone else

### Three Models
- **Susceptible-Infected (SI) Model**
- **Susceptible-Infected-Susceptible (SIS) Model**
- **Susceptible-Infected-Recovered (SIR) Model**

depending on the characteristics of a pathogen, we need different models to capture the dynamics of an epidemic outbreak

## Network Epidemics

## Contact Networks

## Immunization
*immunization*: a vaccine or treatment given to individuals to cure or treat a specific pathogen; how to block the spreading of a disease.

> immunization strategies aim to minimize the threat of a pandemic by most effectively distributing the available vaccines or treatments.

Immunization strategies are guided by an important prediction of the traditional epidemic models: If a pathogen’s spreading rate $\lambda$ is reduced under its critical threshold $\lambda_{c}$, the virus naturally dies out. Yet, the epidemic threshold vanishes in scale-free networks, questioning the effectiveness of this strategy.

for **random networks** a sufficiently high immunization rate can eliminate the pathogen from the population.

For a **scale-free network** with $\gamma < 3$ we have $\langle k \rangle \rightarrow \infty$, hence $g_{c} \rightarrow 1$. In other words if the contact network has a high $\langle k^2 \rangle$, *we need to immunize virtually all nodes to stop the epidemic*.

### Vaccination Strategies in Scale-Free Networks
The hubs are responsible for the large variance of heterogenous networks. Therefore if we immunize the hubs, we decrease the variance and increase the epidemic threshold. By immunizing the hubs, we are fragmenting the contact network (altering the underlying network), making more difficult for the pathogen to reach the nodes in other components.

> Hub immunization represents a perspective change in immunization protocols: instead of trying to decrease the spreading rate using random immunization, we must alter the topology of the contact network.

The problem with a hub-based immunization strategy is that for most epidemic processes we lack a detailed map of the contact network. Yet, we can still exploit the network topology to design more efficient immunization strategies. To do so, we rely on the **friendship paradox**, the fact that on average the neighbors of a node have higher degree than the node itself. By immunizing the acquaintances of a randomly selected individual, we target the hubs without having to know precisely which individuals are hubs.

### Targeted Immunization
Hubs first! This will block the main disease pathway, which is bridge to hub and then spread to the neighbors. (This is the reason why disease spreads quickly in scale-free networks.)

If we don't know the network, then rely on the **friendship paradox**. Randomly choose a node, and randomly follow an edge to a neighbor. Don't immunize the first node, but immunize the friend.

**Random Friends as Sensors** (see reading)

<u>Summary</u>: although we have a lot of mathematical models, the core idea remains the same with friendship paradox. The fact that we can identify hubs by following links, and hubs play really important role connecting the network together and spreading to the whole network.

# Network Epidemiology
- spreading means connections
- we can't ignore the network anymore; network drastically change the nature of spreading

Studying pandemics, disease can jump from one continent to another in a day through the air transportation network. Networks change the nature of spreading. The most important network to study is the air transportation network because it rapidly speeds up the spreading.

Social networks (contact networks) where disease or information can be transmitted.

What do we know about networks?
- small world: how quickly we can get to a node in the network
- clustering: how friends tend to know each other
- heterogeneous (power-law) degree distribution: there are hubs that are connected to many nodes, while most nodes only have a small number of neighbors

How do these common properties affect spreading?
- <u>clustering and communities</u>: spreading will stay within the local group (if isolated); maybe disease does not spread well in real networks, compared with the case where everything is well mixed
- remember: real networks tend to have shortcuts (bridges) to outside nodes, and that makes the network small world
- although clustering may have some impact to confining the disease or information, it may leak to the outside world
- <u>small world</u>: a small world is created through the act of the shortcuts
- the "well-mixed solution" is already a small world
- consider a solution of people, susceptible and infected individuals. Everyone can meet everyone in classical well-mixed solution setting.
- in small world, you meet people randomly
- hence the small world property may not help much
- though, in the ultra small world (when degree distribution follows a scale-free, power-law, distribution) may impact spreading of disease because the whole network is even more small meaning the disease may spread even more quickly
- <u>heavy-tailed degree distribution</u> (many real networks): how will these affect the spreading of disease?
- considering airline network: they should play a really important role due to the wide connectivity to other places
- spreading to just one airport with a lot of connections (such has Heathrow, London) will enable rapid Spreading

Striking finding: epidemic threshold vanishes in scale-free networks (making the case for network epidemiology).

The *epidemic threshold* $\lambda$ (the rate) is about how well infected nodes create another infected node. Even if the transmission rate is reduced towards zero, the scale-free network can still spread the disease! Whatever disease we are considering, if the network follows the scale-free degree distribution we cannot eradicate the disease from the network (very striking finding). This has also been found in very old computer viruses.

> epidemic spreading is all about following the edge

Summary:
1. hubs can create many infected nodes
2. you can reach the hubs really easily (because of the friendship paradox)
3. the disease can sustain itself once there are hubs in the network

Key idea: hubs play different roles in spreading -> further compartmentalization. Hubs are really important in network epidemiology, so we need to consider them in a special way. One approach: breakdown each degree, and put every node into its own degree bin/compartment, and create a model for each compartment separately and solve all of them at the same time.

SIR model and percolation
- why are we discussing percolation in network epidemics?
- there are some nice equivalence relationship
- by solving the percolation problem we can approximately solve the SIR problem

SIR model and bond (link; edge) percolation

In SIR model, an infected node becomes a recovered node and cannot spread the disease any more. A node may become infected and spread the disease across some links, but then it becomes recovered (no longer infected) and cannot spread the disease across any other links. We can color the edges beforehand to indicate that some edges transmitted the disease and some did not. This is similar to coloring the edges with some probability.

Approach:
1. mark some edges randomly (= bond percolation)
2. select a node and pick it up with all connected nodes

# Can we detect the source?
Forget about geography and spatial information. Get the tree structure centered around one point. The distance between that one point and another is dependent upon the "amount of flow" between them (and not the physical distance). This yields the disease front visualization. You can render different starting points and pick the one which shows the most clear wave front, and this identifies the most likely source of the disease spreading.

[The Hidden Geometry of Complex, Network-Driven Contagion Phenomena](http://science.sciencemag.org/content/342/6164/1337)

-----
**Review**

Question | Answer |
| --- | --- |
| What are the three most basic states or compartments in epidemic modeling?   | Infectious<BR>Susceptible<BR>Recovered  |
| A social network is an example of homogeneous mixing.   | False  |
| Everyone in the population becomes infected in the SI model as $t\rightarrow \infty$ | True  |
| An endemic state is when...   | The fraction of infected stays constant.  |
| Random immunization in practice is inefficient because:   | Scale-free social networks have vanishing epidemic threshold.  |
| Reducing the variance of the degree distribution of the network the contagion is spreading on helps improve immunization success.   | True  |
| How does the friendship paradox aid with immunization?   | It helps find hubs.  |
| A newly discovered pathogen, dubbed the bambonic-plague, has gone pandemic and infected millions across the world. The disease is transmitted through the air and shows cold-like symptoms. Almost 10% of those infected end up dying within a few weeks after exposure. The rest become immune to its effects but remain capable of spreading the disease further.<p><p>Given what you have learned about epidemic modelling, how would you model this disease?    | Susceptible-Infected-Removed-Carrier model. S+I -> I + I, I -> R, I -> C, C+S -> C+I  |
| You live in the small nation of Arstotzka. The pandemic hasn't yet spread to your country, but concerned policy makers fear the worst. Biologists have discovered a vaccine for the virus, but it is difficult to produce and our small nation has limited infrastructure and money to dedicate to its dissemination through the population. Describe how you would go about efficiently distributing the vaccine for maximum effect and make sure to justify your plan; you need to convince those policy makers.   | The best approach for vaccinating will be **Targeted Immunization**. The objective here is to vaccinate people with a high degree of contact and exposure with other people. For example, these may be elected officials, law enforcement, public safety, health officials and workers (doctors and nurses), and educators. These groups of people tend to have contact with many people, and if exposed to the disease they pose a risk of dramatically increasing the spreading rate. However, if we vaccinate these groups of people then they can effectively slow down or stop the spread of the disease.  |

-----
# Side Topics
- Institute of Disease Modeling (Bill Gates)
- The Greatest Risk of a huge tragedy: *an epidemic that is more infectious (than Spanish Flu, or Ebola) and would spread faster*.
- Drugs:
  - small molecule
  - antibodies (complex biological protein), the molecules that the immune system naturally builds to attack disease

-----
# Definitions

**heterogeneity** |ˌhedərəjəˈnēədēˌhedərəjəˈnāədē|<BR>
noun<BR>
the quality or state of <u>being diverse</u> in character or content: the genetic heterogeneity of human populations.

**homogeneity** |ˌhōməjəˈnēədēˌhōməjəˈnāədē|<BR>
noun<BR>
the quality or state of <u>being all the same</u> or all of the same kind: the cultural homogeneity of our society.

-----
# References
- [Barabasi, chapter 10](http://networksciencebook.com/)
- [Week 9, Lab Work: Configuration Model](https://github.com/muftring/iu-netsci/tree/master/week-09)
- [Week 11, Lab Work: Epidemics](https://github.com/muftring/iu-netsci/tree/master/week-11)
