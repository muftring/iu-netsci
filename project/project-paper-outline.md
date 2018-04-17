# Exploring Robustness in Dynamic Graphs

**Suggested outline:**
- Abstract
- Introduction
  - Motivation and review
  - Hypothesis, research questions, etc.
- Methods
- Results
- Discussion
- Conclusion
- References
- (Optional) Appendix

**Outline (WIP):**
1. Introduction
  - objectives
  - background material on graphs / networks / complex systems
  - approach
2. about Robustness
3. about Dynamic graphs
4. Exploration
  - Robustness in Dynamic Graphs
  - approach / techniques / tools
5. Results
6. Conclusion

-----

# Sections

## Abstract
(lifted from proposal - may need modification)

**Abstract.** A *dynamic graph* is a graph "in motion;" it changes over time. A static graph is one which never changes. A dynamic graph may be additive in nature, where vertices or edges are added to the graph. Or, a dynamic graph may be subtractive in nature, where elements are removed. These natures are not mutually exclusive, as a dynamic graph may demonstrate both additive and subtractive behaviors. The *robustness* of a graph is a measure of how well the graph maintains its structure, form, and integrity when undergoing drastic unexpected change. The measures generally used to reflect robustness are related to connectivity, path length, and clustering. This project aims to examine robustness in dynamic graphs by constructing models of behavior (both normal and unexpected), building an application which will realize the models and have them act on graphs, and implementing a means to maintain accurate measures for critical characteristics like shortest path lengths.


## Introduction

**Motivation**

To understand ... how dynamic graphs respond to different "threats" under their normal dynamic behavior (how can we model this? how can we apply the model programmatically? how can we see the model in action?) and how models can be created (augmented) to cope with various threats.


**Questions to answer**

What is a dynamic graph (network)? Provide a basic definition, provide some mathematical foundation,

What is robustness? Define robustness at a high-level. What are threats? Define two types of threats: failure, attack.

Need to bring in **Epidemics** and the models we studied (and additional models), and the concepts and types of immunization, and Epidemiology.

Is this bringing us towards *Network Medicine*?

## Methods

Incremental approach:
- be able to construct a simple dynamic network
- be able to observe simple changes
- can we model this? (with existing tools and libraries, or DIY)

- looking at DyNetX
- looking at NDlib
- looking at Cubix

- Python code to emit events to Gephi:
  - http://www.eecs.wsu.edu/~yyao/DirectedStudyII/src/Citation/GephiJsonClient.py
