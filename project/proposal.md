# <p style="text-align: center;"> Exploring Robustness in Dynamic Graphs</p>
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
<p style="padding-left:40px;">
<b>Abstract.</b>
(Answer the following) What is a dynamic graph? What is robustness, and how do we measure/evaluate it? Why is this interesting (how/where is it or could it be applied)? What will this project do and/or show?
</p>

## Introduction
This project is about *Exploring Robustness in Dynamic Graphs* (networks, complex systems).

We aim to
- define what a *dynamic graph* is
- describe the different dynamic natures:
  - add
  - sub
  - both
- describe and illustrate the temporal element of a dynamic graph
- examine some means of representing dynamic graphs
  - array of adjacency matrices
  - stream of events (add, subtract)
  - and maybe others
- develop a means of specifying and modeling the dynamic nature
  - is this a use of information theory and entropy?
- explore these concepts and with existing and developed tools on
  - constructed networks using Erdos-Renyi, and Barabasi-Albert models
  - real networks (TBD)
- measure the outcome
  - the "usual metrics"
  - how to maintain accurate shortest path knowledge (without having to re-compute everything after each change)
- consider topics like:
  - characterizing time-evolving patterns of connectivity
  - characterizing time-evolving patterns of activity
  - characterizing how activity occurs atop connectivity

## Related Work



-----

**References**

- [F. Harary, G. Gupta, *Dynamic Graph Models*](https://ac.els-cdn.com/S0895717797000502/1-s2.0-S0895717797000502-main.pdf?_tid=23705148-1961-11e8-b0c7-00000aacb35f&acdnat=1519476751_90ed82f52a37b694b2e9b3b658737b04)
- [Camil Demetrescu and Pino Italiano, *Dynamic graphs, Handbook on Data Structures and Applications*, Chapter 36. Dinesh Mehta and Sartaj Sahni (eds.), CRC Press Series, in Computer and Information Science, January 2005.](http://www.diku.dk/PATH05/CRC-book1.pdf)
  - [Link to text at CRC Press](https://www.crcpress.com/Handbook-of-Data-Structures-and-Applications/Mehta-Mehta-Sahni/p/book/9781584884354)
- [Deepak Garg, Megha Tyagi, *Comparative Analysis of Dynamic Graph Techniques and Data Structure*](https://arxiv.org/pdf/1209.6486.pdf)
- [Arnaud Casteigts, Paola Flocchini, Walter Quattrociocchi, Nicola Santoro, *Time-Varying Graphs and Dynamic Networks*](http://people.scs.carleton.ca/~santoro/Reports/CFQS11.pdf)
- [Sudipto Guha, Andrew McGregor, David Tench, V*ertex and Hyperedge Connectivity in Dynamic Graph Streams*](https://people.cs.umass.edu/~mcgregor/papers/15-pods.pdf)
- [Khambhati, Sizemore, Betzel, Bassett, *Modelling and Interpreting Mesoscale Network Dynamics*](https://www.ncbi.nlm.nih.gov/pubmed/28645844)
- [Ann E. Sizemore, Danielle S. Bassett, *Dynamic graph metrics: Tutorial, toolbox, and tale*](https://www.ncbi.nlm.nih.gov/pubmed/28698107)

-----

> The proposal is a two to four page document that contains
> - Project title
> - Team members
> - Abstract: a brief summary of what your project is about.
> - Introduction: why your project is important or interesting? why should we care? What has been done? What are your questions and hypotheses?
> - Related work
> - Data or methods: what are the candidate datasets or methods?
> - Your approach and plan
>   - Potential data sources
>   - Candidate methods to develop or apply
