# Ex3-OOP
## directed  weighted graph:
### The project was about a weighted directed graph,

#### our class represents a directed graph who is made of nodes and edges every edge has a source node and a destination node, which means this edge creates a path from source to destination (the opposite path may not exist). every edge has a weight filed that represents the "cost" of using this edge during a path, we would like to think about this cost as the time it takes  to get from source node to destination node. that is why non positive weight is not possible.


## DiGraph class:
### main methods:

**add_edge**- Adds an edge to the graph, True if the edge was added successfully, False o.w.  
 (If the edge already exists or one of the nodes dose not exists the functions will do no).O(1)
**add_node**- Adds a node to the graph, True if the node was added successfully, False o.w. ( if the node id already exists the node will not be added)O(1)
**all_out_edges_of_node(self, id1: int)**- return a dictionary of all the nodes connected from node_id , each node is represented using a pair  
(other_node_id, weight) O(1)
**get_all_v**- return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data). O(1)
**all_in_edges_of_node(self, id1: int)**- return a dictionary of all the nodes connected to (into) node_id , each node is represented using a pair (other_node_id, weight). O(1)
**remove_node(self, node_id: int)**- Delete the node (with the given key) from the graph -and removes all edges which starts or ends at this node.(True if the node was removed successfully, False o.w, if the node id does not exists the function will do nothing) O(E) E= edges
**remove_edge(self, node_id1: int, node_id2: int)**- delete the edge from the graph (the one from start to end). (True if the edge was removed successfully, False o.w ,If such an edge does not exists the function will do nothing) O(1)
**v_size**- Returns the number of vertices in this graph O(1)
**e_size**- Returns the number of edges in this graph O(1)
**get_mc(self)**- return the number of changes of the graph O(1)

## GraphAlgo class

### main methods:

**get_graph(self)**- Return the directed graph of which this class works.O(1)
**connected_component(self, id1: int)**- Finds the Strongly Connected Component(SCC) that node id1 is a part of. If the graph is None or id1 is not in the graph, the function should return an empty list []. O(V+E)
**connected_components(self)**- Finds all the Strongly Connected Component(SCC) in the graph. If the graph is None the function should return an empty list []
**shortest_path(self, id1: int, id2: int)**-Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm.(The function returns the distance of the path and  a list of the nodes ids that the path goes through). 
If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[]). O(E*LOG2(V))
**save_to_json(self, file_name: str)**- Saves this weighted (directed) graph in JSON format to a file.(True if the save was successful, False o.w.) O(v+e)
**load_from_json(self, file_name: str)**-This method Loads a graph from a json file.(True if the loading was successful, False o.w.) O(v+e)
**plot_graph(self)**-This method Plots the graph.  
If the nodes have a position, the nodes will be placed there.  
Otherwise, they will be placed in a random but elegant manner. O(v+e)



In the **first part** of the task we had to implement `GraphInterface`
In the **second part** of the task we had to implement `GraphAlgoInterface`.
In the **third part** of the task we were asked to Compare the code we wrote in Python, java and compare with NetworkX on certain algorithms such as: `shortest_path`, `connected_component` and `connected_components`.


