### Evolving Networks

**Initial Attractiveness**:
- isolated nodes cannot acquire links, *preferential attachment* prohibits it as the likelihood will be zero
- adds a random component to the probability of attaching to a node

**Internal Links**:
- new links should not only arrive with new nodes; they should also be added on their own, attaching existing nodes
- *Double Preferential Attachment*: at each time step add m nodes, followed by n links selected with a probability (new links emerges proportional to the degree of the nodes it connects)
- *Random Attachment*: internal links are blind to the degree of the nodes they connect

**Node Deletion**:
- nodes and links can be deleted
- different rates imply different changing characteristics and categorization of the subsequent network

**Accelerated Growth**:
- instead of linear growth with number of nodes, we apply a faster growing trend usually greater than the number of nodes

**Aging**:
- nodes have a limited lifetime
- but they don't just disappear
- they fade away through an aging process, gradually reducing number of links
