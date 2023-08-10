import imageio
import pygame
import networkx as nx

from algorithms import Dijkstra, DFS, BFS
from viz.Matplotlib_Vizs import create_grid_graph
"""
Written by : Pranchal Shah
Github : cyber-shah
For : CS-5008 Summer 2023, Final Report
Date : 8/5/2023
This file contains the visualization functions for the algorithms, using
the pygame library. The functions are called from the algorithms package.
"""
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (200, 200, 0)

NODE_RADIUS = 10
WIDTH, HEIGHT = 800, 600
ANIMATION_DELAY = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Visualization")


def plot_graph(graph):
    nx_graph = nx.Graph()

    for node in graph.nodesDictionary.values():
        nx_graph.add_node(node.get_index())

    # Calculate the number of nodes in each row and column
    grid_size = int(graph.number_of_nodes ** 0.5)

    # Calculate the spacing between nodes
    grid_spacing = min(WIDTH, HEIGHT) / grid_size

    # Calculate positions for the nodes
    pos = {}
    for i, node in enumerate(graph.nodesDictionary.values()):
        row = i // grid_size
        col = i % grid_size
        pos[node.get_index()] = (col * grid_spacing, row * grid_spacing)

    return nx_graph, pos


def draw_graph(graph, nx_graph, pos, exploration_history,
               shortest_path_indexes, current_step, current_path_step):
    screen.fill(WHITE)

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    avg_pos = [0, 0]
    for node_pos in pos.values():
        avg_pos[0] += node_pos[0]
        avg_pos[1] += node_pos[1]
    avg_pos[0] /= len(pos)
    avg_pos[1] /= len(pos)

    # Calculate offset to center the graph on the screen
    offset_x = center_x - avg_pos[0]
    offset_y = center_y - avg_pos[1]

    # Now adjust the positions using the calculated offset
    for node in graph.nodesDictionary.values():
        node_pos = pos[node.get_index()]
        adjusted_pos = (node_pos[0] + offset_x, node_pos[1] + offset_y)
        pygame.draw.circle(screen, BLACK, adjusted_pos, NODE_RADIUS)

    for i in range(len(exploration_history)):
        if i <= current_step:
            exploration_node_pos = pos[exploration_history[i]]
            adjusted_exploration_pos = (exploration_node_pos[0] + offset_x, exploration_node_pos[1] + offset_y)
            pygame.draw.circle(screen, YELLOW, adjusted_exploration_pos, NODE_RADIUS)

    for i in range(len(shortest_path_indexes) - 1):
        if i <= current_path_step:
            path_node_pos = pos[shortest_path_indexes[i]]
            adjusted_path_node_pos = (path_node_pos[0] + offset_x, path_node_pos[1] + offset_y)
            pygame.draw.circle(screen, RED, adjusted_path_node_pos, NODE_RADIUS)

    # Draw the source node in red
    start_node = graph.get_node_via_xy(3, 4)
    start_node_pos = pos[start_node.get_index()]
    adjusted_start_node_pos = (start_node_pos[0] + offset_x, start_node_pos[1] + offset_y)
    # pygame.draw.circle(screen, RED, adjusted_start_node_pos, NODE_RADIUS)

    # Draw the destination node in red
    end_node = graph.get_node_via_xy(13, 8)
    end_node_pos = pos[end_node.get_index()]
    adjusted_end_node_pos = (end_node_pos[0] + offset_x, end_node_pos[1] + offset_y)
    # pygame.draw.circle(screen, RED, adjusted_end_node_pos, NODE_RADIUS)

    pygame.display.flip()


def main():
    graph = create_grid_graph()

    nx_graph, pos = plot_graph(graph)

    start_node_name = graph.get_node_via_xy(4, 5).name
    end_node_name = graph.get_node_via_xy(12, 7).name

    distances_list, exploration_history_indexes, shortest_path_indexes = (
        Dijkstra.dijkstra_path(graph, start_node_name, end_node_name))

    # exploration_history_indexes, shortest_path_indexes = (
    #     DFS.dfs_destination(graph, start_node_name, end_node_name))

    # exploration_history_indexes, shortest_path_indexes = (
    #     BFS.bfs_destination(graph, start_node_name, end_node_name))


    # for GIF
    output_path = "output.gif"
    images = []

    running = True
    current_step = 0
    current_path_step = 0
    exploring = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if exploring and current_step < len(exploration_history_indexes):
            draw_graph(graph, nx_graph, pos, exploration_history_indexes, [],
                       current_step, current_path_step)
            pygame.time.delay(ANIMATION_DELAY)
            current_step += 5
        # all nodes have been explored
        elif current_path_step < len(shortest_path_indexes):
            exploring = False
            draw_graph(graph, nx_graph, pos, exploration_history_indexes, shortest_path_indexes,
                       current_step, current_path_step)
            pygame.time.delay(ANIMATION_DELAY * 5)
            current_path_step += 5
        else:
            running = False

        # Capture the screen as an image
        image_data = pygame.surfarray.array3d(screen)
        images.append(image_data.copy())

        pygame.display.flip()

    # Save recorded frames as a GIF
    imageio.mimsave(output_path, images, duration=0.1)

    pygame.quit()


if __name__ == "__main__":
    main()
