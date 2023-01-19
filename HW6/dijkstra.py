"""
Name: Alina Burlacu
ID: 109129252
Date: 12/09/2022
Assignment: HW6 - Q1 - Implementing Dijkstra's algorithm in Python
Description: Implement the algorithm in Python including your own test driver to prove your implementation.
             Then modify your code to display the entire history of the relaxation process.
"""
import sys


class Graph(object):

    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    # -------------------------------------------------------------
    #                function to create graph
    # -------------------------------------------------------------
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value
        return graph

    # -------------------------------------------------------------
    #                     getter functions
    # -------------------------------------------------------------
    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False):
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]

    # -------------------------------------------------------------
    #                     Dijkstra's Algorithm
    # -------------------------------------------------------------
    def dijkstra_algorithm(graph, start_node):
        unvisited_nodes = list(graph.get_nodes())

        shortest_path = {}
        visited = {}
        path = {}

        infinity = sys.maxsize
        inf_string = ""
        for node in unvisited_nodes:
            shortest_path[node] = infinity
            inf_string = "Infinity"

        shortest_path[start_node] = 0
        path[start_node] = 0
        with open('output_dijkstra.md', 'a') as f:
            print(f"\nNode [{start_node}] with weight: 0 is added to visited \n {path}", file=f)

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node is None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            unvisited_nodes.remove(current_min_node)

            edges = graph.get_outgoing_edges(current_min_node)
            for edge in edges:
                weight = shortest_path[current_min_node] + graph.value(current_min_node, edge)

                if shortest_path[edge] == infinity:
                    path[edge] = shortest_path[current_min_node]
                    shortest_path[edge] = weight
                    visited[edge] = current_min_node

                    with open('output_dijkstra.md', 'a') as f:
                        print(f"\nRelaxed vertex [{edge}]  OLD: {inf_string}  NEW: {weight} \n {path} ", file=f)

                        # print(f"\nPATH: {path}", file=f)

                elif weight < shortest_path[edge]:
                    path[edge] = shortest_path[current_min_node]
                    shortest_path[edge] = weight
                    visited[edge] = current_min_node

                    with open('output_dijkstra.md', 'a') as f:
                        print(f"\nRelaxed vertex [{edge}]  OLD: {shortest_path[edge]}  NEW: {weight} \n {path} ",
                              file=f)

                        # print(f"\nPATH: {path}", file=f)

                else:
                    path[edge] = shortest_path[current_min_node]
                    with open('output_dijkstra.md', 'a') as f:
                        print(f"\nNo relaxation needed for node [{edge}] \n {path}", file=f)

                        # print(f"\nPATH: {path}",file=f)

        return visited, shortest_path

    # -------------------------------------------------------------
    #             helper function to display results
    # -------------------------------------------------------------
    def print_result(visited, shortest_path, start_node, target_node):
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = visited[node]

        path.append(start_node)

        # display output in markdown file
        with open('output_dijkstra.md', 'a') as f:
            print(f"\nShortest distance from '{start_node}' to '{target_node}' is:  {shortest_path[target_node]}.",
                  file=f)
            print("\nPath: " + " -> ".join(reversed(path)), file=f)


# -------------------------------------------------------------
#                      Driver Code
# -------------------------------------------------------------
nodes = ["a", "b", "c", "d", "e", "f", "g", "h"]
init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["a"]["b"] = 3
init_graph["a"]["c"] = 4
init_graph["a"]["d"] = 7
init_graph["b"]["c"] = 1
init_graph["b"]["f"] = 5
init_graph["c"]["f"] = 6
init_graph["c"]["d"] = 2
init_graph["d"]["e"] = 3
init_graph["d"]["g"] = 6
init_graph["e"]["g"] = 3
init_graph["e"]["h"] = 4
init_graph["f"]["e"] = 1
init_graph["f"]["h"] = 8
init_graph["g"]["h"] = 2
init_graph["h"]["g"] = 2

graph = Graph(nodes, init_graph)

visited, shortest_path = Graph.dijkstra_algorithm(graph=graph, start_node="a")

Graph.print_result(visited, shortest_path, start_node="a", target_node="h")
