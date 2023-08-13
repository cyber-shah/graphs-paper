import csv
import random
import time

from algorithms import Dijkstra, DFS, BFS, A_star
from model.GraphMakers import graph_from_csv


def run_all_algos(csv_files, algos):
    # csv_files is a list of csv file names
    # algos is a list of algorithm names
    # create a dictionary that maps the algorithm names to the corresponding functions
    algo_dict = {
        "Dijkstra": Dijkstra.dijkstra_path,
        "DFS": DFS.dfs_destination,
        "BFS": BFS.bfs_destination,
        "A*": A_star.a_star_destination
    }

    # create an empty list to store the results
    results = []

    # loop through the csv files
    for csv_file in csv_files:
        # create a graph from the csv file
        graph = graph_from_csv(csv_file)

        # end_node = get_end_node_as_last_node(csv_file)
        end_node = get_end_node_as_random(csv_file)

        # loop through the algorithms
        for algorithm in algos:
            # get the algorithm function from the dictionary using the algorithm name as a key
            algo_function = algo_dict.get(algorithm)

            # check if the algorithm function is valid
            if algo_function is not None:
                # start a timer
                start = time.time()

                # run the algorithm function on the graph and get the path, explored nodes
                explored_nodes_indexes, shortest_path = (
                    algo_function(graph, '(1, 1)', end_node))

                # stop the timer and get the elapsed time
                end = time.time()
                elapsed = end - start

                # get the length of the path
                path_length = len(shortest_path)
                explored_length = len(explored_nodes_indexes)

                # append a row to the results with the csv file name, algorithm name, time, path length and nodes
                # explored
                results.append([csv_file, algorithm, elapsed, path_length, explored_length])
            else:
                print("Invalid algorithm name")

    # create a csv file name for the output
    output_file = "results.csv"

    # open the output file in write mode
    with open(output_file, "w") as f:
        # create a csv writer object
        writer = csv.writer(f)

        # write a header row with the column names
        writer.writerow(["CSV File", "Algorithm", "Time", "Path Length", "Nodes Explored"])

        # write the results to the output file
        writer.writerows(results)

    # return the output file name
    return output_file


def get_end_node_as_last_node(csv_file):
    # split the file name by the '-' character and get the last element
    last_int = csv_file.split('-')[-1]
    # remove the '.csv' extension from the last element
    last_int = last_int.replace('.csv', '')
    # convert the last element to an integer
    last_int = int(last_int)
    # create a string that represents the destination node using the last integer
    return f'({last_int}, {last_int})'


def get_end_node_as_random(csv_file):
    # get the size of the maze from the file name
    last_int = (csv_file.split('-')[4])
    size = int(last_int.replace('.csv', ''))

    # generate a random end node within the size of the maze
    end_x = random.randint(1, size)
    end_y = random.randint(1, size)
    return f'({end_x}, {end_y})'
