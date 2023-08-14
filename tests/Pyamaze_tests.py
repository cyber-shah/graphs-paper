import re

from algorithms import Dijkstra
from view.lib.pyaMaze.pyamaze.pyamaze import maze, agent, COLOR
import algorithms.Dijkstra
import algorithms.DFS
import algorithms.BFS
import algorithms.A_star
from model.GraphMakers import graph_from_csv

import time
import threading
from PIL import ImageGrab


def extract_list_of_tuples(shortest_path, custom_graph):
    shortest_path_list = ""
    for index in shortest_path:
        shortest_path_list += custom_graph.get_node_via_index(index).__str__()
    # Extract row and column values using regular expressions
    matches = re.findall(r'\((\d+), (\d+)\)', shortest_path_list)
    # Convert the extracted matches into a list of tuples
    shortest_path = [(int(match[0]), int(match[1])) for match in matches]
    return shortest_path


def start_recording():
    global recording, frame_array
    recording = True
    while recording:
        screenshot = ImageGrab.grab(bbox=None)  # Capture the entire screen
        frame = screenshot.convert("RGB")
        frame_array.append(frame)
        time.sleep(0.1)  # Adjust the sleep time to control frame rate


def stop_recording():
    global recording
    recording = False


def pymaze():
    global shortest_path, explored_nodes_indexes
    goal_row = 15
    goal_col = 17
    maze_row_size = 20
    maze_col_size = 20
    source_row = 5
    source_col = 3
    algorithm = 'BFS'

    # create explored_agent maze of size 20 x 20
    custom_maze = maze(maze_row_size, maze_col_size)
    # set the goal at 4 , 4
    # loop percent means multiple paths in the maze
    custom_maze.CreateMaze(goal_row, goal_col, loopPercent=30, loadMaze='../tests/20x20-RandomMaze.csv')

    custom_graph = graph_from_csv('20x20-RandomMaze.csv')

    if algorithm == 'Dijkstra':
        explored_nodes_indexes, shortest_path = Dijkstra.dijkstra_path(
            custom_graph, '(5, 3)', '(15, 17)')
    elif algorithm == 'DFS':
        explored_nodes_indexes, shortest_path = algorithms.DFS.dfs_destination(
            custom_graph, '(5, 3)', '(15, 17)')
    elif algorithm == 'BFS':
        explored_nodes_indexes, shortest_path = algorithms.BFS.bfs_destination(
            custom_graph, '(5, 3)', '(15, 17)')
    elif algorithm == 'A*':
        explored_nodes_indexes, shortest_path = algorithms.A_star.a_star_destination(
            custom_graph, '(5, 3)', '(15, 17)')

    # extract a list of tuples _____________________________________
    shortest_path_list = extract_list_of_tuples(shortest_path, custom_graph)
    explored_nodes_list = extract_list_of_tuples(explored_nodes_indexes, custom_graph)

    # create an explored_agent
    explored_agent = agent(custom_maze, source_row, source_col, filled=True,
                           footprints=True, color=COLOR.dark_blue)
    explored_nodes = explored_nodes_list

    # create an path_agent
    path_agent = agent(custom_maze, source_row, source_col, filled=True,
                       footprints=True, color=COLOR.pink)
    shortest_path = shortest_path_list

    # # trace the explored_nodes
    # # key is the agent, value is the explored_nodes
    custom_maze.tracePath({explored_agent: explored_nodes}, delay=25)
    custom_maze.tracePath({path_agent: shortest_path}, delay=25)

    # Run the maze
    custom_maze.run()

    # TODO : create a md table
    #        distance of shortest path, explored nodes and time taken


def main():
    recording = True

    if recording:
        global frame_array
        # Start recording the maze ________________________________________________
        frame_array = []
        recording_thread = threading.Thread(target=start_recording)
        recording_thread.start()
        # Create the maze
        pymaze()
        # Stop the recording when the maze window is closed
        stop_recording()
        recording_thread.join()
        # Save the frames as a GIF using Pillow
        frame_array[0].save(
            'maze_recording.gif',
            save_all=True,
            append_images=frame_array[1:],
            duration=100,  # Duration between frames in milliseconds
            loop=0  # 0 means an infinite loop
        )
    else:
        # Create the maze
        pymaze()


if __name__ == '__main__':
    main()
