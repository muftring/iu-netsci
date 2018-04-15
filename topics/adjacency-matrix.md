# Adjacency Matrix
An adjacency matrix is a means for representing a graph. It is a two-dimensional matrix where each vertex is present along the horizontal and vertical. The value in each matrix position indicates whether there is an edge connecting the two vertices.

Simple connectedness between two vertices can be represented using binary values: 0 = no, and 1 = yes. For weighted graphs the value in the each matrix position represents the weight of the edge, with zero again indicating that no relation exists.

This mechanism can be applied to both undirected and directed graphs. In the case where the graph is directed, the order of indexing the matrix indicates the direction of the vertex-to-vertex relationship (i.e., which vertex is connected to the other by the edge).

A vertex's degree can be calculated from an adjacency matrix. In the case of an undirected graph, simply sum the row or column corresponding to the vertex. For a directed graph, sum the vertex's row to obtain in degree, and some the vertex's column to obtain the out degree.

$A_{ij}$ where $i$ identifies the row and $j$ identifies the column

# Examples

(see Reference below)

## Undirected Network

For an *undirected* network, the entries in the Adjacency Matrix will be symmetric: if there is a connection between two nodes then there will be an entry for both row-column combinations.

$A_{ij}$ = 0, if there is no link between $i$ and $j$

$A_{ij}$ = 1, if there is a link connecting $i$ and $j$

|     |  1  |  2  |  3  |  4  |
| --- | --- | --- | --- | --- |
|**1**|  0  |  1  |  1  |  0  |
|**2**|  1  |  0  |  1  |  1  |
|**3**|  1  |  1  |  0  |  0  |
|**4**|  0  |  1  |  0  |  0  |


## Directed Network

For a *directed* network we read the subscripts "backwards":

$A_{ij}$ = 1, if there is a link pointing from $j$ to $i$

$A_{ji}$ = 1, if there is a link pointing from $i$ to $j$

Looking into the Adjacency Matrix, however, we still use the first subscript to identify the row and the second subscript to identify the column.

- $A_{ij}$ for $A_{13} = 1$
- indicates that node **3** is connected to node **1** (there is a link from 3 to 1)
- look at the entry at **row 1** and **column 3**

|     |  1  |  2  |  3  |  4  |
| --- | --- | --- | --- | --- |
|**1**|  0  |  0  |  1  |  0  |
|**2**|  1  |  0  |  1  |  1  |
|**3**|  0  |  0  |  0  |  0  |
|**4**|  0  |  1  |  0  |  0  |

# Reference

Barabasi, *Network Science*, chapter 2.5 (p.52)

![](http://networksciencebook.com/images/ch-02/figure-2-5.jpg)

**Image 2.5**

*The Adjacency Matrix*

The labeling of the elements of the adjacency matrix.
The adjacency matrix of an undirected network. The figure shows that the degree of a node (in this case node 2) can be expressed as the sum over the appropriate column or the row of the adjacency matrix. It also shows a few basic network characteristics, like the total number of links, L, and average degree, ‹k›, expressed in terms of the elements of the adjacency matrix.
The same as in (b) but for a directed network.
