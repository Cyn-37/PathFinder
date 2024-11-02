# A* Pathfinding Visualizer

## Overview
The A* Pathfinding Visualizer is an interactive tool designed to demonstrate the A* pathfinding algorithm. This program allows users to visualize how the algorithm finds the shortest path from a starting point to an endpoint on a grid, taking into account various costs associated with different cell types.

## Features
- **Interactive Grid**: Users can click on the grid to change the type of each cell, which can represent normal paths, obstacles, or higher-cost paths.
- **Set Start and End Points**: Right-click to select the starting and ending points for the pathfinding process.
- **Pathfinding Visualization**: Once the start and end points are set, the A* algorithm calculates and visualizes the optimal path on the grid.
- **Cost Representation**: Different cell colors represent different costs. Normal paths are shown in white, obstacles in black, and high-cost paths in red.
- **Information Window**: A toggleable information window provides instructions and details about how to interact with the program.

## Controls
- **Left Click**: Change the cell type at the clicked position.
- **Right Click**: Set or reset the start and end points.
- **Show Info Button**: Click the "Show Info" button to toggle the information window.

## How It Works
The A* algorithm combines the strengths of Dijkstra's algorithm and a heuristic to efficiently find the shortest path. The heuristic used in this visualizer is the Manhattan distance, which estimates the cost from the current cell to the destination cell.

### Algorithm Steps
1. Initialize the open set and closed set.
2. While there are nodes to explore:
   - Get the node with the lowest cost from the open set.
   - If it is the target node, reconstruct the path.
   - Evaluate the neighbors of the current node and calculate their costs.
   - Add valid neighbors to the open set.
3. If no path is found, the algorithm terminates without a solution.
