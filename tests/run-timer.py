# import the run_all_algos function
import glob

from tests.emperical_timer import run_all_algos

# get a list of all the csv files that start with "maze" and end with ".csv"
csv_files = glob.glob("maze-csvs\maze*.csv")

# define a list of algorithm names that you want to use
algos = ["Dijkstra", "DFS", "BFS", "A*"]

# call the run_all_algos function with the csv files and the algorithms
output_file = run_all_algos(csv_files, algos)

# print the output file name
print(output_file)
