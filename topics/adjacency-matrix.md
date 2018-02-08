# Adjacency Matrix
An adjacency matrix is a means for representing a graph. It is a two-dimensional matrix where each vertex is present along the horizontal and vertical. The value in each matrix position indicates whether there is an edge connecting the two vertices.

Simple connectedness between two vertices can be represented using binary values: 0 = no, and 1 = yes. For weighted graphs the value in the each matrix position represents the weight of the edge, with zero again indicating that no relation exists.

This mechanism can be applied to both undirected and directed graphs. In the case where the graph is directed, the order of indexing the matrix indicates the direction of the vertex-to-vertex relationship (i.e., which vertex is connected to the other by the edge).

A vertex's degree can be calculated from an adjacency matrix. In the case of an undirected graph, simply sum the row or column corresponding to the vertex. For a directed graph, sum the vertex's row to obtain in degree, and some the vertex's column to obtain the out degree.
