import networkx as nx

def tsp(graph, start):
    unvisited = list(graph.nodes())
    unvisited.remove(start)

    def tsp_helper(curr, unvisited):
        if not unvisited:
            return graph[curr][start]['weight']
        return min(graph[curr][next_node]['weight'] + tsp_helper(next_node, unvisited.copy().remove(next_node))
                   for next_node in unvisited)

    return tsp_helper(start, unvisited)

def dijkstra(graph, start, end):
    shortest_path = nx.dijkstra_path(graph, start, end)
    shortest_distance = nx.dijkstra_path_length(graph, start, end)
    return shortest_path, shortest_distance

# Contoh penggunaan
G = nx.Graph()
G.add_edge('A', 'B', weight=12)
G.add_edge('A', 'C', weight=10)
G.add_edge('A', 'G', weight=12)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'D', weight=12)
G.add_edge('C', 'D', weight=10)
G.add_edge('C', 'E', weight=3)
G.add_edge('C', 'G', weight=9)
G.add_edge('D', 'E', weight=11)
G.add_edge('D', 'F', weight=10)
G.add_edge('E', 'F', weight=6)
G.add_edge('E', 'G', weight=7)
G.add_edge('F', 'G', weight=9)

# Pilihan pengguna
algorithm = input("Pilih algoritma (TSP atau Dijkstra): ")

if algorithm.lower() == "tsp":
    # Menghitung shortest path dengan TSP
    tsp_shortest_path = tsp(G, 'A')
    print("Shortest path using TSP:", tsp_shortest_path)
elif algorithm.lower() == "dijkstra":
    # Menghitung shortest path dengan Dijkstra
    start_node = input("Masukkan simpul awal: ")
    end_node = input("Masukkan simpul akhir: ")
    dijkstra_shortest_path, dijkstra_shortest_distance = dijkstra(G, start_node, end_node)
    print("Shortest path using Dijkstra:", dijkstra_shortest_path)
    print("Shortest distance using Dijkstra:", dijkstra_shortest_distance)
else:
    print("Pilihan algoritma tidak valid.")