# Network Epidemics
*Spreading Process*

What is *epidemics*? It is from Greek, and translates as:
- epi: upon
- demos: people

*something happening upon people*

An epidemic usually describes infectious disease spreading across the population.

Why do we care?

Studying epidemics helps us understand spreading processes:
- human disease
- computer virus, internet worm
- diffusion of information
- spreading of rumors (e.g., on social media)
- spreading ideas and information

History:
- The Great Plague
- 1918 Spanish Flu
- HIV
- SARS
- H1N1 Flu

This becomes much more dangerous and important because we are getting much more connected.
- high population density (in cities)
- high mobility (air travel)
- <u>equates to</u>: perfect conditions for epidemic spreading

Population density matters (a lot) because it provides the fuel where the infectious disease is the fire.
- small, separate (unconnected) population will burn the "local fuel" and cause the fire to "die out" (think: hunter-gatherer society, wild animals)
- large (highly populated) cities are strongly connected to other cities and so the chance for spread of disease is great (almost perfect)

Mobility matters (also)
- limited by the speed of human travel

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
- latent individuals: who have been exposed to the disease, but are not yet contagious

**Homogenous Mixing**<BR>
The homogenous mixing hypothesis (also called fully mixed or mass-action approximation) assumes that each individual has the same chance of coming into contact with an infected individual.

assumption: anyone can infect anyone else

### Three Models
- **Susceptible-Infected (SI) Model**
- **Susceptible-Infected-Susceptible (SIS) Model**
- **Susceptible-Infected-Recovered (SIR) Model**

depending on the characteristics of a pathogen, we need different models to capture the dynamics of an epidemic outbreak


-----
**Review**

Question | Answer |
| --- | --- |
| What are the three most basic states or compartments in epidemic modeling?   | Infectious<BR>Susceptible<BR>Recovered  |
| A social network is an example of homogeneous mixing.   | False  |
| Everyone in the population becomes infected in the SI model as $t\rightarrow \infty$ | True  |
| An endemic state is when...   | The fraction of infected stays constant.  |

-----
# Side Topics
- Institute of Disease Modeling (Bill Gates)
- The Greatest Risk of a huge tragedy: *an epidemic that is more infectious (than Spanish Flu, or Ebola) and would spread faster*.
- Drugs:
  - small molecule
  - antibodies (complex biological protein), the molecules that the immune system naturally builds to attack disease

-----
# References
