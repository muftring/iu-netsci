# <p style="text-align: center;">Exploring Robustness in Dynamic Graphs</p>
<br>
<p style="text-align: center;">
<i>
Michael Uftring<br>
Indiana University<br>
INFO-I606-32299 - Network Science<br>
Spring, 2018
</i>
</p>
<br>
<p style="padding-left:40px;"><b>Abstract.</b> A <i>dynamic graph</i> is a graph "in motion;" it changes over time. A static graph is one which never changes. A dynamic graph may be additive in nature, where vertices or edges are added to the graph. Or, a dynamic graph may be subtractive in nature, where elements are removed. These natures are not mutually exclusive, as a dynamic graph may demonstrate both additive and subtractive behaviors. The <i>robustness</i> of a graph is a measure of how well the graph maintains its structure, form, and integrity when undergoing drastic unexpected change. The measures generally used to reflect robustness are related to connectivity, path length, and clustering. This project aims to examine robustness in dynamic graphs by constructing models of behavior (both normal and unexpected), building an application which will realize the models and have them act on graphs, and implementing a means to maintain accurate measures for critical characteristics like shortest path lengths.
</p>

## Introduction
The objective of this project is to learn and present the basic theory behind dynamic graphs, understand the interaction between dynamic graph behavior and characteristics, construct models for this behavior, and to observe and measure the robustness of dynamic graphs under duress.

A simple model will be constructed which describes the natural additive and subtractive behavior of dynamic graphs. Also, a threat model will be developed to facilitate testing and measuring the network's robustness while under siege: either by random or fatigued failure, or by intentional and malicious attack. Note that both vertices and edges may exhibit dynamic behavior; the models will specify the strategy for action (add, subtract, modify or distort elements and values) and also specify on which graph elements to act.

An **Explorable Notebook Application** will be developed which allows interactive exploration of this topic and the algorithms and models developed, while presenting a visual depiction of the dynamic graph with animated activity.

The aim is to:
- provide a definition for *dynamic graphs*, both conceptually and mathematically
- describe the different dynamic natures
- describe and illustrate the temporal element of a dynamic graph
- examine some means of representing dynamic graphs, including but not necessarily limited to:
  - sequence of adjacency matrices
  - stream of events
- develop a mechanism for specifying and modeling the dynamic nature and behavior
  - this includes the natural change of a dynamic graph
  - and also the threat models for unexpected change
- add robustness monitoring by lively tracking of critical graph characteristics
- explore these concepts and techniques with existing and developed tools on
  - constructed networks using Erdos-Renyi, and Barabasi-Albert models
  - real networks (TBD)
- report the outcome from a period of model execution

## Related Work
The related work in this space roughly breaks down into the following categories:

- <u>Theory</u>
- <u>Data Structures and Algorithms</u>
- <u>Tools and Techniques</u>
- <u>Applied Topics</u>

### Theory
- [F. Harary, G. Gupta, *Dynamic Graph Models*](https://ac.els-cdn.com/S0895717797000502/1-s2.0-S0895717797000502-main.pdf?_tid=23705148-1961-11e8-b0c7-00000aacb35f&acdnat=1519476751_90ed82f52a37b694b2e9b3b658737b04)
- [Arnaud Casteigts, Paola Flocchini, Walter Quattrociocchi, Nicola Santoro, *Time-Varying Graphs and Dynamic Networks*](http://people.scs.carleton.ca/~santoro/Reports/CFQS11.pdf)
- [Petter Holme, Jari Saramäki, *Temporal networks*]()
- [A. A. Kochkarov, R. A. Kochkarov, and G. G. Malinetskii, *Issues of Dynamic Graph Theory*]()
- [*Graph dynamical system* (Wikipedia)](https://en.wikipedia.org/wiki/Graph_dynamical_system)
- [*Dynamic connectivity* (Wikipedia)](https://en.wikipedia.org/wiki/Dynamic_connectivity)

### Data Structures and Algorithms
- [Camil Demetrescu and Pino Italiano, *Dynamic graphs, Handbook on Data Structures and Applications*, Chapter 36. Dinesh Mehta and Sartaj Sahni (eds.), CRC Press Series, in Computer and Information Science, January 2005.](http://www.diku.dk/PATH05/CRC-book1.pdf)
  - [Link to text at CRC Press](https://www.crcpress.com/Handbook-of-Data-Structures-and-Applications/Mehta-Mehta-Sahni/p/book/9781584884354)
- [Deepak Garg, Megha Tyagi, *Comparative Analysis of Dynamic Graph Techniques and Data Structure*](https://arxiv.org/pdf/1209.6486.pdf)
- [T.Ramraja, R.Prabhakar, *Frequent Subgraph Mining Algorithms – A Survey*]()
- [G. Cattaneo, P. Faruolo, U. Ferraro Petrillo, G.F. Italiano, *Maintaining dynamic minimum spanning trees: An experimental study*]()

### Tools and Techniques
- [Sudipto Guha, Andrew McGregor, David Tench, *Vertex and Hyperedge Connectivity in Dynamic Graph Streams*](https://people.cs.umass.edu/~mcgregor/papers/15-pods.pdf)
- [Ann E. Sizemore, Danielle S. Bassett, *Dynamic graph metrics: Tutorial, toolbox, and tale*](https://www.ncbi.nlm.nih.gov/pubmed/28698107)
- [Ming Gao, Ee-Peng Lim, David Lo, *R-energy for Evaluating Robustness of Dynamic Networks*](https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=2893&context=sis_research)

### Applied Topics
- [Khambhati, Sizemore, Betzel, Bassett, *Modelling and Interpreting Mesoscale Network Dynamics*](https://www.ncbi.nlm.nih.gov/pubmed/28645844)
- [Yaron Singer, *Dynamic Measure of Network Robustness*](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=4115313)
- [Jianxi Gao, Baruch Barzel & Albert-László Barabási, *Universal resilience patterns in complex networks*](https://www.nature.com/articles/nature16948)
- [Logan Collins, *Notes on: Universal resilience patterns in complex networks, Gao et al. 2016*](https://logancollinsblog.com/2017/11/26/notes-on-universal-resilience-patterns-in-complex-networks-gao-et-al-2016/)
- [Arnaud Casteigts, Swan Dubois, Franck Petit, John Michael Robson, *Robustness in Highly Dynamic Networks*]()
- [Gouhei Tanaka, Kai Morino & Kazuyuki Aihara, *Dynamical robustness in complex networks: the crucial role of low-degree nodes*](https://www.nature.com/articles/srep00232)
- [Till Becker, Mirja Meyer, Katja Windt, *A network theory approach for robustness measurement in dynamic manufacturing systems*](http://www.psls.uni-bremen.de/fileadmin/Upload/Downloads/Artikel/Becker_A_network_theory_approach_for_robustness_measurement_in_dynamic_manufacturing_systems_2013.pdf)
