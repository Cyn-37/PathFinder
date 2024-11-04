# Pathfinding Visualizer

## Overview
The A* Pathfinding Visualizer is an interactive tool designed to demonstrate various pathfinding algorithms, including A*, Breadth-First Search (BFS), and Depth-First Search (DFS). This program allows users to visualize how these algorithms find the shortest path from a starting point to an endpoint on a grid, taking into account various costs associated with different cell types. The visualizer serves as an educational resource for understanding the principles behind pathfinding algorithms and their applications in real-world scenarios, such as robotics, gaming, and network routing.

## Features
- **Interactive Grid**: Users can click on the grid to change the type of each cell. Each cell can represent normal paths, obstacles, or higher-cost paths, enabling users to create custom scenarios for testing the algorithms.
  
- **Set Start and End Points**: Right-click to select the starting and ending points for the pathfinding process. This feature allows users to experiment with different start and end configurations to observe how the algorithms adapt to various layouts.
  
- **Pathfinding Visualization**: Once the start and end points are set, the selected algorithm (A*, BFS, or DFS) calculates and visualizes the optimal path on the grid. The visualization updates in real-time, allowing users to see the algorithm's decision-making process as it navigates through the grid.
  
- **Cost Representation**: Different cell colors represent different costs associated with traveling through them. Normal paths are shown in white, obstacles in black, and high-cost paths in red. This visual differentiation helps users understand the impact of varying costs on the pathfinding process.
  
- **Algorithm Selection**: Users can choose which algorithm to visualize (A*, BFS, or DFS) before starting the pathfinding process. This flexibility allows for direct comparison of the different algorithms and their performance under similar conditions.
  
- **Information Window**: A toggleable information window provides instructions and detailed explanations about how to interact with the program. This feature is especially useful for users who are new to pathfinding algorithms or programming in general.

## Controls
- **Left Click**: Change the cell type at the clicked position. This enables users to modify the grid dynamically and create obstacles or paths as needed.
  
- **Right Click**: Set or reset the start and end points. This allows for quick adjustments to the pathfinding scenario without needing to restart the visualizer.
  
- **Algorithm Selection**: Select the desired algorithm from the dropdown menu. This allows users to switch between A*, BFS, and DFS with ease, encouraging exploration of each algorithm's mechanics.
  
- **Show Info Button**: Click the "Show Info" button to toggle the information window. This keeps the user informed about the program’s features and how to use them effectively.

## How It Works
- A* Algorithm: A* is a popular pathfinding algorithm that combines the strengths of Dijkstra's algorithm and a heuristic. It efficiently finds the shortest path by evaluating the cost of moving to each neighbor node, while also considering the estimated cost to reach the destination from that node. The heuristic used in this visualizer is the Manhattan distance, which provides a straightforward method for estimating costs based on grid positions.

- Breadth-First Search (BFS): BFS is a fundamental search algorithm that explores all neighbors at the present depth prior to moving on to nodes at the next depth level. This method ensures that the shortest path is found in an unweighted grid. BFS operates by maintaining a queue of nodes to explore, making it ideal for scenarios where all paths have equal cost.

- Depth-First Search (DFS): DFS is another fundamental search algorithm that explores as far down a branch as possible before backtracking. While DFS can be less efficient in terms of pathfinding, as it may not always yield the shortest path, it can be beneficial in scenarios where space efficiency is critical. DFS operates using a stack, making it a straightforward implementation for exploring complex grid layouts.

Overall, the A* Pathfinding Visualizer serves as a comprehensive tool for understanding and experimenting with pathfinding algorithms. Whether for educational purposes, programming practice, or just for fun, this visualizer helps users gain valuable insights into how these algorithms function in various scenarios.
