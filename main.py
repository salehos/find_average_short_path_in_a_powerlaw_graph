import traceback
from networkx.utils import powerlaw_sequence
from networkx.generators import expected_degree_graph
import networkx as nx
from multiprocessing import Pool
from numpy import average

def calculate_average_shortest_path_in_random_graph(n_and_e:str):
    try:
        # set lambda and node_numbers
        number_of_nodes, exponent= n_and_e.split("_")
        number_of_nodes = int(number_of_nodes)
        exponent = float(exponent)
        # initialize nodes
        nodes = powerlaw_sequence(n = number_of_nodes ,exponent = exponent)

        # initialize graph
        G = expected_degree_graph(nodes)

        # remove isolated nodes from graph
        G.remove_nodes_from(list(nx.isolates(G)))

        # find Giant component
        G0 = G.subgraph(max(nx.connected_components(G), key=len))

        # show how many giant component has nodes and  edges
        # print(G0)
        # nx.draw(G)

        # find average shortest path length in giant components
        c = nx.average_shortest_path_length(G0)
        return c
    except Exception as e:
        traceback.print_exc()
        print(e)
        pass

if __name__ == "__main__":
    # running code for 10**2 nodes and difrent lambda and also 10**4 nodes ...
    must_be_calculate  = {
        (10**2, 2) : None,
        (10**2, 2.5): None,
        (10**2, 3): None,
        (10**2, 5): None,
        (500, 2) : None,
        (500, 2.5): None,
        (500, 3): None,
        (500, 5): None,
        (10**3, 2) : None,
        (10**3, 2.5): None,
        (10**3, 3): None,
        (10**3, 5): None,
        (2*10**3, 2) : None,
        (2*10**3, 2.5): None,
        (2*10**3, 3): None,
        (2*10**3, 5): None,
        (4*10**3, 2) : None,
        (4*10**3, 2.5): None,
        (4*10**3, 3): None,
        (4*10**3, 5): None,
        (6*10**3, 2) : None,
        (6*10**3, 2.5): None,
        (6*10**3, 3): None,
        (6*10**3, 5): None,
    }
    for key in must_be_calculate:
        res = []
        with Pool(10) as p:
            res = p.map(calculate_average_shortest_path_in_random_graph, [str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1]), str(key[0])+"_"+str(key[1])])
        must_be_calculate[key] = average(res)
        print("for node and lambda:",key, ' <d> in 10 times try:', res, " average <d> is:", average(res))
    print(must_be_calculate)